# Introduction to NumPy and Pandas

## Overview

[NumPy](https://numpy.org/doc/stable/user/whatisnumpy.html) and [Pandas](https://pandas.pydata.org/docs/index.html) are popular libraries in Python used by data scientists/engineers for day-to-day numerical and mathematical operations on datasets.

The aim of this lesson is to expose learners to NumPy and Pandas at an introductory level, guiding them to the first-step should they decide to pursue to advance in Python and Data Science related skills.

## Lesson Objectives

By the end of this lesson, learners should be able to:

1. Tell the difference between list (out of the box) and array (by NumPy).
1. Use array slicing
1. Use simple calculation functions by NumPy such as:
    - sum
    - mean
1. Load excel to Python code using Pandas
1. Read subset of excel using dataframes
1. Commonly used dataframes manipulations from Pandas such as:
    - iloc
    - query()
    - groupby

## Installing Dependencies

MacOS:
```sh
pip3 install numpy pandas openpyxl
```

Windows:
```sh
pip install numpy pandas openpyxl
```

## Lesson

[NumPy](./src/numpy-array.py)
[Pandas](./src/pandas-df.py)

## Exercises

1. Given an array `[1,2,3,4,5,6,7,8,9,10,11,12]`, find the following using NumPy:

    1. sum of the array
    1. average of the array
    1. a slice of the array with double digits value


2. Given the `Salary Info.xlsx`, find the following using Pandas:

    1. Employees with more than $10k monthly salary excluding the company
    1. The salary burn rate of the respective company (hint: use `groupby`)
    1. Top 5 highest paying employee and their company