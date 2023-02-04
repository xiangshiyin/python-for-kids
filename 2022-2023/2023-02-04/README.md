
**Table of Content**
- [Lecture 18: Python Libraries and How To Use Them](#lecture-18-python-libraries-and-how-to-use-them)
  - [What are libraries](#what-are-libraries)
  - [What can you do with Python libraries](#what-can-you-do-with-python-libraries)
  - [Examples](#examples)
  - [How do we use them (***We'll cover this in our next lecture***)](#how-do-we-use-them-well-cover-this-in-our-next-lecture)
    - [A simple Python package](#a-simple-python-package)
    - [Things might be more complicated](#things-might-be-more-complicated)
- [Course Materials](#course-materials)
- [Topics to Explore](#topics-to-explore)
  - [Reading](#reading)


# Lecture 18: Python Libraries and How To Use Them

## What are libraries

A Python library is a collection of well organized python scripts that can be reused in different programs to tackle specific problems. It is created such that you could stand on the shoulders of the giants without reinventing the wheels. It also makes Python programs more concise and let people focus on core logics instead of utility functions.
## What can you do with Python libraries

## Examples
Check the code samples [here](./practice.ipynb)
* `string`
* `math`
* `matplotlib`

## How do we use them (***We'll cover this in our next lecture***)
### A simple Python package
Assume we have a package with the following file distribution
```md
└── sample_package
    └── sample.py
    └── subpackage
        └── subsample.py
```
The content of `sample.py` is like
```python
x = 123
y = 234

def hello():
    print('Hello World')
```

The content of `subsample.py`
```python
xx = 1
yy = 2
```

### Things might be more complicated
![](./library_tree.png)

***You could***
* `import` the whole library, by `import a`
* `import` a module (python script), by `import a.aa`
* `import` a object (variable, function, class, etc.) in a module, by `import a.aa.aaa`


**However**, you should keep using the `<object>` name in the `import <object>` statement in your program to reference the object you imported. **Sometimes, this could be quite inconvenient** because the `<object>` string could be pretty long due to the complicatedd file structures in the python library

**There are two ways** to solve the problem:
* `from a import aa` (use the `from` statement to reference the complicated folder relationships)
* `import a.aa as aa` (create an alias)







# Course Materials
[*slides*](https://docs.google.com/presentation/d/1vzOVB10gz5SWs2NAn4XTrTPJgcqr2_Y8niDloIQi7-A/edit?usp=sharing)


# Topics to Explore
## Reading
* Top 10 Python libraries [[*link*](https://www.interviewbit.com/blog/python-libraries/#:~:text=With%20more%20than%20137%2C000%20libraries,data%20manipulation%2C%20and%20many%20more.)]
