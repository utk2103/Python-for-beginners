# Contributing

Thanks for helping out. This repo exists to teach Python, so the bar for a good contribution is "would a beginner understand this without asking anyone?"

## Before you write code

1. Pick an issue — start with [good first issues](https://github.com/utk2103/Python-for-beginners/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).
2. Comment on it to get assigned. This avoids two people building the same thing.
3. No issue for your idea? Open one first and describe what you want to add. Agreeing on the shape beforehand saves a rewritten PR.

## What we accept

- **Scripts** (`scripts/`) — one self-contained `.py` file that runs from the repo root.
- **Notebooks** (`notebooks/`) — one topic, explained in order, markdown between code cells.
- **Docs** (`docs/`) — setup guides, visual explanations, indexes.
- **Fixes** — broken code, wrong output, dead links, typos. Always welcome, no issue needed for a typo.

## Style rules

These keep the repo readable for someone three weeks into Python:

- **Standard library first.** Only add a dependency when the standard library genuinely can't do it. If you do, add it to `requirements.txt` and say why in a comment at the top of your script.
- **No frameworks or classes for their own sake.** A function beats a class; a script beats a package.
- **Comment the *why*, not the *what*.** `i += 1  # move to next item` is noise. `# Why: avoids integer overflow on huge lists` earns its line.
- **Fail with a message, not a traceback.** A missing file or bad argument should print something a beginner can act on.
- **Anything destructive needs `--dry-run`.** Scripts that move, rename, or delete files must be able to print their plan without touching disk.
- **Leave one check behind.** If your script has real logic (a loop, a parser, a branch), add a few `assert` statements under `if __name__ == "__main__":` or a small `test_<name>.py`. No test frameworks needed.
- **Notebooks: clear cell outputs before committing** if they're large or contain your local paths.

## Fork → branch → PR

If you're new to Git, this is the whole flow. ([Install Git](https://docs.github.com/en/get-started/quickstart/set-up-git) first if you don't have it.)

**1. Fork** this repository using the Fork button at the top of the page. That creates your own copy.

**2. Clone your fork** — open your fork on GitHub, click the green Code button, copy the URL, then:

```bash
git clone https://github.com/<your-username>/Python-for-beginners.git
cd Python-for-beginners
```

**3. Create a branch** named after what you're doing:

```bash
git switch -c add-password-generator
```

**4. Make your changes and commit them:**

```bash
git add scripts/password_generator.py
git commit -m "Add secrets-based password generator script"
```

**5. Push to your fork:**

```bash
git push -u origin add-password-generator
```

**6. Open the pull request** — go to your fork on GitHub, click **Compare & pull request**, and describe what you added. Link the issue with `Closes #<number>`.

## Pull request checklist

- [ ] Your script runs from the repo root: `python scripts/your_script.py`
- [ ] Standard library only, or the new dependency is in `requirements.txt`
- [ ] The issue's acceptance criteria are all ticked
- [ ] One file per PR where possible — small diffs get merged faster
- [ ] No unrelated reformatting of files you didn't need to change

## Prefer a GUI?

GitHub Desktop, GitKraken, and VS Code's Source Control panel all do the same steps. GitHub's [first-contributions guide](https://github.com/firstcontributions/first-contributions#tutorials-using-other-tools) covers each one.

Happy coding.
