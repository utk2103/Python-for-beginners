# Python-for-beginners


Here i'm learning the basics of Python programming and exploring various data types and essential libraries such as Matplotlib, Pandas, and NumPy. I also added some short but yet very useful in development like file handling serialization and deserialization, exception handling, decorators and namespaces.
The project aims to provide hands-on experience with Python's core concepts and commonly used data manipulation and visualization libraries.


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
