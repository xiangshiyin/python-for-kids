
**Table of Contents**
- [Lecture 02: Variable and Data](#lecture-02-variable-and-data)
  - [Lecture topics](#lecture-topics)
  - [Concepts](#concepts)
    - [Variable](#variable)
  - [Course materials](#course-materials)
  - [Topics to explore](#topics-to-explore)
    - [Read](#read)
    - [Exercise](#exercise)


# Lecture 02: Variable and Data

## Lecture topics
* [x] Different ways to run Python code
  * `IDLE` [[link](https://docs.python.org/3/library/idle.html)] - Python's integrated development and learning environment
    * **THIS WILL BE THE PRIMARY CODING TOOL IN OUR CLASS**
  * The `Python Interpreter` [[link](https://docs.python.org/3/tutorial/interpreter.html)]
    * Run a `*.py` script from command line
  * `ipython` [[link](https://ipython.readthedocs.io/en/stable/)] - An interactive Python interpreter (it should come with the Anaconda installation)
  * `replit` - https://replit.com
* [x] Variables
* [x] Hands-on practice

## Concepts
### Variable
* In computer programming, a variable is a symbolic name or identifier that represents a storage location in memory. 
* It's used to store and manage data that can change during the execution of a program. 
* Variables allow programmers to work with data, perform calculations, and create dynamic and interactive programs.


## Course materials
* [slides](https://docs.google.com/presentation/d/1IkAT-Y9Cx9ex4Q9LlYHwt2LdG7eD0CgCqt6WebD_7uY/edit#slide=id.p)

## Topics to explore
### Read
* The *Von Neumann architecture* [[wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_architecture)]
* Jason had some questions about the usage of indentations in python, [here](https://www.askpython.com/python/python-indentation) is a good read
### Exercise
* Run the following code and see if you can understand what it does in each line of the code
  ```python
  import turtle

  t = turtle.Turtle()

  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  turtle.done()
  ```
