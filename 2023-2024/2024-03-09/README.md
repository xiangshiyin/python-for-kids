
**Table of Content**
- [Lecture 22: Python Libraries and How to Use Them (part II)](#lecture-22-python-libraries-and-how-to-use-them-part-ii)
  - [Topics](#topics)
  - [Concepts](#concepts)
    - [A simple Python package](#a-simple-python-package)
    - [Things might be more complicated](#things-might-be-more-complicated)
    - [`__init__.py`](#__init__py)
    - [Different ways to import python libraries](#different-ways-to-import-python-libraries)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)
- [Assignment](#assignment)

# Lecture 22: Python Libraries and How to Use Them (part II)

## Topics
Here are the topics we are going to cover
* [x] How to import pre-built Python code
* [x] Demo of `matplotlib`
  * [ ] Draw a circle
  * [ ] Draw a moving line
  * [x] Compare the trends of different math expressions
    * $y_1 = x$
    * $y_2 = x^2$
    * $y_3 = x^3$
    * $y_4 = log_2(x)$
    * $y_5 = x * log_2(x)$


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

### `__init__.py`
In Python, the `__init__.py` file is used to define a package. It's required to make Python treat the directories containing the file as packages. The `__init__.py` file can be empty, or it can contain initialization code for the package.

You might see a python package looks like this
```
my_package/
    __init__.py
    module1.py
    module2.py
```

You could 
* Leave it as empty
* Add initialization code
  ```python
  print("Initializing my_package...")

  from .module1 import *
  from .module2 import *
  ```

### Different ways to import python libraries
Just like the examples above
* Import the whole library via `import package_name`
* Import the whole python module via `import ancestor.grandparent.parent.child` where `child` represents a python module `child.py`
* Make the object referencing string of hierarchy shorter, by
  *  Define an alias such as `import ancestor.grandparent.parent.child as c` where `child` represents a python module `child.py`
  *  Use the `from ancestor.grandparent.parent import child` pattern
* We didn't get time to cover this, but you could also directly import an object (variable, function, class, etc.) within a python module follow the pattern below
  * `from ancestor.grandparent.parent.child import talent` where `child` represents a python module `child.py`

## Course materials
* slides [[link](https://docs.google.com/presentation/d/12gJBpGx0VQnQB85JdMk--SNVcTJc0zdUx3cWQDwSQSM/edit?usp=sharing)]

# Suggested reading
* Online resources
  * Introduction to Python modules and packages [[link](https://realpython.com/python-modules-packages/)]
    * A bit long but a good read :)

# Assignment
Can you solve the following math problem?
* **Q1**: Annie needs to use 1 complete candle each day. When the candles burn out, she could also melt 7 candle ends to make 1 complete candle. Given the fact that Annie has 7 complete candles at the very beginning, how many days can the candles last before she needs to go and buy new ones?
  * Assume Annie has $x$ candles at the very beginning, can you write a function `days(x)` to output the number of days the candles can last before Annie needs to buy new ones?
