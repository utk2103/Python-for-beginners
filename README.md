# Python for Beginners

Learn Python by reading short notebooks and running small scripts — core syntax first, then the data stack (NumPy, Pandas, Matplotlib, Seaborn), then the real-world bits nobody teaches you: file handling, serialization, exceptions, threading, CLIs.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Good first issues](https://img.shields.io/github/issues/utk2103/Python-for-beginners/good%20first%20issue?label=good%20first%20issues&color=7057ff)](https://github.com/utk2103/Python-for-beginners/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Not sure where you stand?** Take the [level check quiz](https://pppwebapp.web.app/) first, then start at the matching step below.

---

## Quick start

```bash
git clone https://github.com/utk2103/Python-for-beginners.git
cd Python-for-beginners

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
jupyter lab                       # or: jupyter notebook
```

Scripts need no setup beyond the standard library unless their header says otherwise:

```bash
python scripts/BinarySearch.py
python scripts/argparse_1.py 7 3 multiply
```

---

## Learning path

Work top to bottom. Each notebook is self-contained, so you can also jump straight to a topic.

### 1. Core Python
| Notebook | Covers |
|--|--|
| [Python basics](notebooks/Python%20basics.ipynb) | variables, numeric/str/bool types, operators, I/O |
| [Conditionals and booleans](notebooks/Conditionals%20and%20booleans.ipynb) | `if`/`elif`/`else`, truthiness, comparison chaining |
| [Loops and iterators](notebooks/Loops%20and%20iterators.ipynb) | `for`, `while`, `range`, iterators vs iterables |
| [Functions](notebooks/Function.ipynb) | arguments, defaults, return values, scope |
| [Lambda functions](notebooks/Lambda%20function.ipynb) | anonymous functions, `map`/`filter`/`sorted(key=…)` |

### 2. Data structures
| Notebook | Covers |
|--|--|
| [Lists](notebooks/pc_list.ipynb) | indexing, slicing, list methods, comprehensions |
| [Dictionaries](notebooks/Dictionaries.ipynb) | key/value access, iteration, nesting |

### 3. Real-world Python
| Notebook | Covers |
|--|--|
| [Exception handling](notebooks/Exception%20handling%20.ipynb) | `try`/`except`/`else`/`finally`, raising, custom errors |
| [File handling + serialization (1)](notebooks/File%20Handling%20%2B%20Serialization%20%26%20Deserialization-1.ipynb) | reading/writing files, modes, context managers |
| [File handling + serialization (2)](notebooks/File%20Handling%20%2B%20Serialization%20%26%20Deserialization-2.ipynb) | JSON and `pickle` round-trips |
| [Decorators & namespaces](Decorators%20%26%20Namespaces/Decorators%20%26%20Namespaces.ipynb) | closures, `@decorator`, LEGB scope rules |

### 4. The data stack
| Notebook | Covers |
|--|--|
| [NumPy](notebooks/Numpy_Notes.ipynb) | arrays, dtypes, shapes, broadcasting, vectorised math |
| [Pandas](notebooks/Pandas_Notes.ipynb) | Series/DataFrame, selection, cleaning, grouping |
| [Matplotlib](notebooks/Matplotlib.ipynb) | figures, axes, line/bar/scatter, labels and legends |
| [Seaborn 1](notebooks/Seaborn%201.ipynb) → [2](notebooks/Seaborn%202.ipynb) → [3](notebooks/Seaborn%203.ipynb) → [4](notebooks/Seaborn%204.ipynb) | statistical plots, distributions, categorical plots, heatmaps |

### 5. Runnable scripts
Algorithms and small programs in [`scripts/`](scripts/) — searching, sorting, recursion, CLIs, threading, `enum`. A full index with one-line descriptions is [issue #15](https://github.com/utk2103/Python-for-beginners/issues/15), up for grabs.

---

## Repository structure

```
Python-for-beginners/
├── notebooks/                 # Interactive lessons, one topic per notebook
├── scripts/                   # Standalone runnable .py files
├── Decorators & Namespaces/   # Decorator + scope notebook
├── data/                      # Small sample files (txt, json, pkl) for practice
├── docs/                      # Extra guides (pdf2docx setup, Tower of Hanoi visual)
├── resources/                 # Reference PDFs, cheat sheets, notes
├── requirements.txt           # Notebook + data-stack dependencies
└── .github/                   # Issue templates
```

## Reference material

The [`resources/`](resources/) folder holds PDFs for when you want a second explanation: a Python cheat sheet, *Automate the Boring Stuff*, *Python Crash Course*, a list of built-in methods, and 52 practice Q&As.

---

## Contributing

New contributors are welcome, and this repo is a good place to make a first open-source PR.

1. Browse [good first issues](https://github.com/utk2103/Python-for-beginners/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).
2. Comment on the one you want so nobody duplicates your work.
3. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the fork → branch → PR walkthrough and the style rules.

Ideas outside the open issues are welcome too — open an issue first so we can agree on the shape before you write code.

## License

[Apache License 2.0](LICENSE).
