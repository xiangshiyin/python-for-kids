
**Table of Content**
- [Lecture 19: Python Libraries and How To Use Them (part II)](#lecture-19-python-libraries-and-how-to-use-them-part-ii)
  - [How do we use a python library](#how-do-we-use-a-python-library)
    - [A simple Python package](#a-simple-python-package)
    - [Things might be more complicated](#things-might-be-more-complicated)
- [Course Materials](#course-materials)
- [Topics to Explore](#topics-to-explore)
  - [Reading](#reading)
  - [Coding](#coding)


# Lecture 19: Python Libraries and How To Use Them (part II)

## How do we use a python library
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
[*slides*](https://docs.google.com/presentation/d/1To0QhYLt7tTitHHFYFsioEg2a1QCRC2IXJRTVX7sHl8/edit?usp=share_link)


# Topics to Explore
## Reading
Explore the following two libraries (or pick one)
* `turtle`
  * Tutorial - https://realpython.com/beginners-guide-python-turtle/
  * The official doc - https://docs.python.org/3/library/turtle.html
* `pygame`
  * Introduction - https://www.pygame.org/docs/tut/PygameIntro.html
  * The official doc - https://www.pygame.org/docs/
* `music21` - http://web.mit.edu/music21/

## Coding
Can you solve the following math problem?
* Q1: Annie needs to use 1 complete candle each day. When the candles burn out, she could also melt 7 candle ends to make 1 complete candle. Given the fact that Annie has 7 complete candles at the very beginning, how many days can the candles last before she needs to go and buy new ones?
* Assume Annie has $x$ candles at the very beginning, can you write a function `days(x)` to output the number of days the candles can last before Annie needs to buy new ones?
