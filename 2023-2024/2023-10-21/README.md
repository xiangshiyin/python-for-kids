
**Table of Content**
- [Lecture 09: Loops (part II)](#lecture-09-loops-part-ii)
  - [Topics](#topics)
  - [Exercises](#exercises)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)
- [Coding assingment](#coding-assingment)

# Lecture 09: Loops (part II)

## Topics
Here are the topics we are going to cover
* [x] Recap on `while` loop
* [x] `for` loop in Python
* [ ] ~~Brief introduction on `list` in Python~~ (didn't get time to cover)

## Exercises
* Generate top N Fibonacci numbers [[wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence)]
* Write a program to generate the Pascal's triangle [[wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)]
  * 杨辉三角形 [[wikipedia](https://zh.wikipedia.org/wiki/%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%E5%BD%A2)] 
  
    ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/83e43c795c7cba79bf4b6a4a3cdfa0f3e52b5fd5)

## Concepts
* `break` statement in loops
* `for` loop is used when you want to repeat a fixed number of times
* `while` loop vs. `for` loop - instead of controling the loop via a "*conditio*n", we can control the loop via a precise "*counter*"
    ```mermaid
    ---
    title: while loop
    ---
    stateDiagram-v2
        Condition_check: If condition == True
        Plan_A: Plan A
        Plan_B: Plan B
        [*] --> Condition_check
        Condition_check --> Plan_A: True/Yes
        Plan_A --> Condition_check
        Condition_check --> Plan_B: False/No
    ```

    ```mermaid
    ---
    title: for loop
    ---
    stateDiagram-v2
        Condition_check: Is this the "last iteration"
        Plan_A: Plan A
        Plan_B: Plan B
        [*] --> Condition_check
        Condition_check --> Plan_A: True/Yes
        Plan_A --> Condition_check
        Condition_check --> Plan_B: False/No
    ```
* `list` is a data type used to store multiple items in one variable
  * It is *mutable*
  * It is of *sequential* type - items in a list follows certain order
  * It shares many characeristics with `string`
    * Same way `len()` to measure length
    * Same indexing pattern to reference a subset
    * Same way to append new data
    * Same way to check if a subset exists


## Course materials
* slides [[link](https://docs.google.com/presentation/d/1UMjtWnDGFoZwY2U8wfDYdsg3_xRSMHi-VMYg5rTNa1g/edit?usp=sharing)]

# Suggested reading
* Online resources
  * `for` loop [[Python Wiki](https://wiki.python.org/moin/ForLoop)]

# Coding assingment
* Finish the in-class coding problem of generating first N Fibonacci numbers where N could be any positive integer.
* Now that we've got some basic understanding on writing Python code inside a `*.py` file with `IDLE`, I think it is a good time to move on to a more advanced code editor (you might also hear people call them `IDE` which stands for *integrated development environment*) - **Visual Studio Code**.
  * To get yourself prepared, you can download and install **visual studio code (vscode)** follow the link https://code.visualstudio.com/