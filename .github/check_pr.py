#!/usr/bin/env python3
"""PR gate: repo structure + the rules in CONTRIBUTING.md. Run from the repo root."""

import argparse
import ast
import json
import re
import subprocess
import sys
from pathlib import Path

# Every entry allowed at the repo root. Adding one is a structural change.
TOP_LEVEL = {
    ".github", ".gitignore", "CONTRIBUTING.md", "LICENSE", "README.md",
    "requirements.txt", "data", "Decorators & Namespaces", "docs",
    "notebooks", "resources", "scripts", "tests",
}
# Which extension belongs in which directory, and how deep a new file may sit.
DIR_RULES = {"scripts": ".py", "notebooks": ".ipynb", "docs": ".md", "tests": ".py"}
FREEFORM = {"data", "resources", "Decorators & Namespaces", ".github"}

IMPORT_ALIASES = {
    "cv2": "opencv-python", "PIL": "pillow", "sklearn": "scikit-learn",
    "bs4": "beautifulsoup4", "yaml": "pyyaml", "dotenv": "python-dotenv",
}
LOCAL_PATH = re.compile(r"/Users/|/home/[a-z]|[A-Z]:\\Users")
DESTRUCTIVE = re.compile(r"shutil\.(rmtree|move)|os\.(remove|unlink|rmdir|rename)|\.unlink\(|\.replace\(")

errors, warnings = [], []


def fail(path, msg):
    errors.append(f"{path}: {msg}")


def warn(path, msg):
    warnings.append(f"{path}: {msg}")


def changed_files(base):
    out = subprocess.run(
        ["git", "diff", "--name-status", "--find-renames", f"{base}...HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout
    changes = []
    for line in out.splitlines():
        parts = line.split("\t")
        changes.append((parts[0][0], parts[1:]))
    return changes


def requirement_names():
    names = set()
    for line in Path("requirements.txt").read_text().splitlines():
        line = line.split("#")[0].strip()
        if line:
            names.add(re.split(r"[<>=!\[;\s]", line)[0].lower().replace("_", "-"))
    return names


def imported_roots(tree):
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and not node.level and node.module:
            roots.add(node.module.split(".")[0])
    return roots


def check_structure(changes):
    for status, paths in changes:
        target = paths[-1]
        top = target.split("/")[0]
        if status in "AR" and top not in TOP_LEVEL:
            fail(target, f"new top-level entry '{top}'. Put it in one of: {', '.join(sorted(DIR_RULES))}")
            continue
        if status == "R":
            fail(target, f"renamed/moved from '{paths[0]}'. Open an issue first — moves break links in the docs and notebooks")
        if status == "D":
            fail(target, "deleted. Deletions need a maintainer's sign-off; open an issue instead")
        if status == "A" and top in DIR_RULES:
            bits = target.split("/")
            if len(bits) != 2:
                fail(target, f"nested under {top}/. One flat file per contribution, no subdirectories")
            elif not target.endswith(DIR_RULES[top]):
                fail(target, f"{top}/ holds only {DIR_RULES[top]} files")


def test_sources(_cache={}):
    # Why: a script counts as checked if a test file names it
    if not _cache:
        files = list(Path("tests").glob("test_*.py")) + list(Path("scripts").glob("test_*.py"))
        _cache["text"] = "\n".join(p.read_text(errors="replace") for p in files)
    return _cache["text"]


def check_script(path, reqs, repo_modules):
    source = Path(path).read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as exc:
        fail(path, f"does not parse: line {exc.lineno}: {exc.msg}")
        return

    for root in sorted(imported_roots(tree)):
        if root in sys.stdlib_module_names or root in repo_modules:
            continue
        pkg = IMPORT_ALIASES.get(root, root).lower().replace("_", "-")
        if pkg not in reqs:
            fail(path, f"imports third-party '{root}' — add '{pkg}' to requirements.txt and say why in a comment")

    if DESTRUCTIVE.search(source) and "--dry-run" not in source:
        fail(path, "moves or deletes files but has no --dry-run flag")

    has_logic = any(isinstance(n, (ast.For, ast.While, ast.FunctionDef)) for n in ast.walk(tree))
    stem = Path(path).stem
    tested = Path(f"tests/test_{stem}.py").exists() or stem in test_sources()
    if has_logic and "assert" not in source and not tested:
        warn(path, "real logic but no check — add a few asserts under `if __name__ == \"__main__\":`")


def check_notebook(path):
    try:
        nb = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(path, f"is not valid notebook JSON: {exc}")
        return
    size = 0
    for cell in nb.get("cells", []):
        blob = json.dumps(cell.get("outputs", []))
        size += len(blob)
        if LOCAL_PATH.search(blob):
            fail(path, "output contains a local filesystem path — clear the outputs before committing")
            return
    if size > 1_000_000:
        warn(path, f"{size // 1000} KB of saved output — clear the outputs to keep clones small")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default="origin/main", help="branch or ref to diff against")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        selftest()
        return 0

    if not Path("CONTRIBUTING.md").exists():
        print("Run this from the repo root.", file=sys.stderr)
        return 2

    try:
        changes = changed_files(args.base)
    except subprocess.CalledProcessError:
        print(f"Cannot diff against '{args.base}'. Fetch it first: git fetch origin main", file=sys.stderr)
        return 2

    if not changes:
        print(f"No changes against {args.base}.")
        return 0

    check_structure(changes)
    reqs = requirement_names()
    # Why: sibling scripts and the scripts/ and tests/ packages are local, not PyPI
    repo_modules = {p.stem for p in Path("scripts").glob("*.py")} | set(DIR_RULES)
    for status, paths in changes:
        target = paths[-1]
        if status == "D" or not Path(target).exists():
            continue
        if target.endswith(".py"):
            check_script(target, reqs, repo_modules)
        elif target.endswith(".ipynb"):
            check_notebook(target)

    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"error:   {line}")
    print(f"\n{len(changes)} changed file(s), {len(errors)} error(s), {len(warnings)} warning(s).")
    if errors:
        print("See CONTRIBUTING.md for the rule behind each error.")
    return 1 if errors else 0


def selftest():
    tree = ast.parse("import os, numpy as np\nfrom pathlib import Path\nfrom . import x")
    assert imported_roots(tree) == {"os", "numpy", "pathlib"}
    assert re.split(r"[<>=!\[;\s]", "pdf2docx>=0.5")[0] == "pdf2docx"
    assert LOCAL_PATH.search("/Users/someone/data.csv")
    assert not LOCAL_PATH.search("data/sample.txt")
    assert DESTRUCTIVE.search("shutil.rmtree(p)") and not DESTRUCTIVE.search("os.listdir(p)")
    errors.clear()
    check_structure([("A", ["tools/x.py"]), ("A", ["scripts/deep/x.py"]), ("A", ["scripts/a.txt"]), ("D", ["README.md"])])
    assert len(errors) == 4, errors
    errors.clear()
    check_structure([("A", ["scripts/ok.py"]), ("M", ["README.md"])])
    assert not errors, errors
    print("selftest ok")


if __name__ == "__main__":
    sys.exit(main())
