# `scripts/` index

Standalone runnable `.py` files — one concern each, no shared imports.
Most need only the standard library; a few call out external packages
in their header. Run them from the repo root.

| Script | What it does | Run it |
|---|---|---|
| [`01.TwoSum.py`](../scripts/01.TwoSum.py) | LeetCode-style **Two Sum** using a sort + two-pointer pass over `(value, index)` pairs; returns the original indices of the two numbers that add up to the target. Class only — no CLI; import `Solution` to reuse. | `python -c "import importlib.util as u; m=u.spec_from_file_location('s','scripts/01.TwoSum.py'); mod=u.module_from_spec(m); m.loader.exec_module(mod); print(mod.Solution().twoSum([2,7,11,15], 9))"` or paste into a scratch file |
| [`argparse_1.py`](../scripts/argparse_1.py) | CLI arithmetic demo built on `argparse`: takes two ints and an `add`/`subtract`/`multiply` choice, prints the result. Shows `--help` and type-checked choices. | `python scripts/argparse_1.py 7 3 multiply` |
| [`BinarySearch.py`](../scripts/BinarySearch.py) | Iterative binary search on a sorted list; searches for `4` in `[3,4,5,6,7,8,9]` and prints the index. | `python scripts/BinarySearch.py` |
| [`check.py`](../scripts/check.py) | Scratch-pad demo used to learn terminal I/O in VS Code: prints "Hello world", reads one number via `input()`, and prints a movie list. | `python scripts/check.py` |
| [`csv_json_converter.py`](../scripts/csv_json_converter.py) | Converts between a CSV file and a JSON file of flat objects; auto-detects direction from the `.csv` / `.json` extension of the two path arguments. Validates the JSON is a list of dicts and wraps a lone dict into a list so `csv.DictWriter` accepts it. | `python scripts/csv_json_converter.py in.csv out.json` |
| [`enum_use_case.py`](../scripts/enum_use_case.py) | One-line `enum.Enum` demo: defines `OrderStatus` with `PENDING` / `SHIPPED` / `DELIVERED` and prints the current status value. | `python scripts/enum_use_case.py` |
| [`guess_the_number.py`](../scripts/guess_the_number.py) | Two-mode number-guessing game — (1) you guess the computer's secret in `1..100`, (2) the computer binary-searches your number in `1..1000`. Includes a `max_guesses` helper derived from `ceil(log2(n+1))` and input-validation loops. | `python scripts/guess_the_number.py` (interactive) |
| [`LinearSearch.py`](../scripts/LinearSearch.py) | Simple linear scan for a target in an unsorted list; searches for `1` in `[2,4,0,1,9]` and prints the index. | `python scripts/LinearSearch.py` |
| [`MergeSort.py`](../scripts/MergeSort.py) | In-place recursive merge sort with a comment walk-through; sorts `[6,5,12,10,9,1]` and prints the result. | `python scripts/MergeSort.py` |
| [`multithreading.py`](../scripts/multithreading.py) | Runs "square each" and "cube each" worker threads in parallel over the same list. Uses `time.sleep(1)` per item to simulate work and prints total wall-clock time to show the speedup. | `python scripts/multithreading.py` |
| [`pdf2doc.py`](../scripts/pdf2doc.py) | PDF → DOCX converter using the `pdf2docx` library. Converts a hard-coded `ListsOfInbuiltMethods.pdf` in the current working directory to `ListsOfInbuiltMethods.docx`. | `pip install pdf2docx` then `python scripts/pdf2doc.py` (from a CWD containing the PDF) |
| [`qr_code_generator.py`](../scripts/qr_code_generator.py) | CLI that turns a text string or URL into a QR code PNG; refuses to overwrite an existing output file. | `pip install "qrcode[pil]"` then `python scripts/qr_code_generator.py "https://example.com" -o qr.png` |
| [`toh.py`](../scripts/toh.py) | Towers of Hanoi: prompts for a disk count and prints each `move X to Y` step via the classic three-peg recursion. | `python scripts/toh.py` (interactive) |
