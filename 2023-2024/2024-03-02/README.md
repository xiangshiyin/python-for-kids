
**Table of Content**
- [Lecture 21: Python Libraries and How to Use Them (part I)](#lecture-21-python-libraries-and-how-to-use-them-part-i)
  - [Topics](#topics)
  - [Concepts](#concepts)
    - [A simple Python package](#a-simple-python-package)
    - [Things might be more complicated](#things-might-be-more-complicated)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 21: Python Libraries and How to Use Them (part I)

## Topics
Here are the topics we are going to cover
* [ ] Wrap-up the Tic-Tac-Toe game UI code
* [ ] How to import pre-built Python code


## Concepts
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
* `import` the whole package, by `import a`
* `import` a module (python script), by `import a.aa`
* `import` a object (variable, function, class, etc.) in a module, by `import a.aa.aaa`


**However**, you should keep using the `<object>` name in the `import <object>` statement in your program to reference the object you imported. **Sometimes, this could be quite inconvenient** because the `<object>` string could be pretty long due to the complicatedd file structures in the python library

**There are two ways** to solve the problem:
* `from a import aa` (use the `from` statement to reference the complicated folder relationships)
* `import a.aa as aa` (create an alias)


## Course materials
* slides [TBD]

# Suggested reading
* Online resources
  * Introduction to Python modules and packages [[link](https://realpython.com/python-modules-packages/)]
    * A bit long but a good read :)
