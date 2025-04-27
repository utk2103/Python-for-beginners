# Python-for-beginners

Welcome! This repository is designed for anyone starting with Python, offering hands-on practice with core concepts, data types, and essential libraries like Matplotlib, Pandas, and NumPy. It also includes useful real-world topics such as file handling, serialization, exception handling, and more.

#### Refer this blog for every single resource

[Blog](https://shorturl.at/CVc5c)

---

## 📁 Repository Structure

To make it easy for you to find what you need, here’s how the files and folders are organized:

```
Python-for-beginners/
│
├── notebooks/      # Jupyter notebooks for interactive learning (Numpy, Pandas, Seaborn, etc.)
├── scripts/        # Standalone Python scripts for algorithms, demos, and exercises
├── resources/      # PDF books, cheat sheets, and other learning materials
├── docs/           # Documentation and extra guides
├── data/           # Sample data files for practice
├── .github/        # GitHub configuration files
├── README.md       # You are here! Main guide for the repo
└── requirements.txt# (Add your dependencies here if needed)
```

### What you’ll find in each folder:
- **notebooks/**: Interactive, step-by-step explanations and code for each topic. Great for experimentation!
- **scripts/**: Ready-to-run Python files for algorithms (searching, sorting, etc.), examples, and small projects.
- **resources/**: Handy PDFs, notes, and cheat sheets for quick reference.
- **docs/**: Extra documentation or guides (e.g., how to use a package).
- **data/**: Small datasets or files for practicing file handling and data analysis.

---

## Installation

Additionally, the project utilizes several external libraries, including Matplotlib, Pandas, and NumPy. These libraries can be installed using pip, the Python package manager. Run the following command to install the dependencies:

```shell
pip install matplotlib pandas numpy
```


## Data Types

The project covers various data types in Python, including:

- Numeric types: int, float
- Boolean type: bool
- Sequence types: str, list, tuple
- Mapping type: dict
- Set types: set

## Libraries

1. Matplotlib: A popular data visualization library that provides a wide range of plotting options, enabling the creation of various charts, graphs, and visualizations.

2. Pandas: A powerful library for data manipulation and analysis. Pandas provides data structures and functions to efficiently handle structured data, perform data cleaning, filtering, aggregation, and more.

3. NumPy: A fundamental library for numerical computing in Python. NumPy provides support for handling large, multi-dimensional arrays and a collection of mathematical functions for efficient numerical operations.

4. Seaborn: A data visualization library that provides a wide range of plotting options and also require less line of code than matplotlib with more number of plotting options like heatmap etc.

## For Contribution


_If you're not comfortable with command line, [here are tutorials using GUI tools.](#tutorials-using-other-tools)_


#### If you don't have git on your machine, [install it](https://docs.github.com/en/get-started/quickstart/set-up-git).

## Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

## Clone the repository

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

For example:

```
git clone git@github.com:this-is-you/Python-for-begineers.git
```

where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd Python-for-begineers
```

Now create a branch using the `git switch` command:

```
git switch -c your-new-branch-name
```

For example:

```
git switch -c add-alonzo-church
```

## Make necessary changes and commit those changes

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```
git add <file-name>
```

Now commit those changes using the `git commit` command:

```
git commit -m "Add appropriate message"
```

## Push changes to GitHub

Push your changes using the command `git push`:

```
git push -u origin your-branch-name
```

replacing `your-branch-name` with the name of the branch you created earlier.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

Now submit the pull request.

**Happy coding!**
