
**Table of Contents**
- [Lecture 01: Introduction to Programming \& Python](#lecture-01-introduction-to-programming--python)
  - [Lecture topics](#lecture-topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
  - [Topics to explore](#topics-to-explore)


# Lecture 01: Introduction to Programming & Python

## Lecture topics
* [x] Get to know each other
* [x] Learn about computer programming in general and Pythong as a programming language
* [ ] Set up and get familiar with the coding environment
    * Have `python` installed
    * Get familiar with `IDLE`
    * Brief introduction to `replit`

## Concepts
* The `print()` function
* How to run a python code
* Sample code
  * Code 1
    ```python
    import turtle

    t = turtle.Turtle()
    t.speed(5)
    colours = ["red","blue","yellow","brown","black","purple","green"]

    t.penup(); t.left(90); t.forward(200);t.right(90);t.pendown()
    for i in range (0,18):
        t.pencolor(colours[i%7])
        t.right(20)
        t.forward(50)

    t.right(180)
    t.home()  
    turtle.done()
    ```
  * Code 2
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



## Course materials
* [slides](https://docs.google.com/presentation/d/1RcMmaIqXb1f_tszkQL703S8BBQ6OMKSMU_eVQenZsyY/edit?usp=sharing)

## Topics to explore
* Python installation
  * Follow the instructions listed [here](../../docs/coding_tools_v1.md#local-coding-tools) to install the `Python` application for our offline coding exercise in class
    * Let's start with [option 1](https://github.com/xiangshiyin/python-for-kids/blob/main/docs/coding_tools_v1.md#option-1-python-application-recommended) for now
    * If you are interested to explore `Anaconda` in [option 2](https://github.com/xiangshiyin/python-for-kids/blob/main/docs/coding_tools_v1.md#option-2-anaconda-a-package-with-python-application-and-all-commonly-used-python-libraries-for-analytics-and-modeling), feel free to do so
  * If time allows, follow the example [here](https://sites.pitt.edu/~naraehan/python3/getting_started_win_first_try.html) to get yourself familiar with `IDLE`
* General Python FAQ [[link](https://docs.python.org/3/faq/general.html#why-is-it-called-python)]
* [**In-depth research**] Philp and Jason asked in our class about how compiler works for a programming language. I did some further digging after class and thought these 2 online posts might be helpful to understand the process (there must be more helpful resources online, so please don't stop exploring if you are interested). **It could well be a good course project later to create our own programming language!!**
  * [Writing your compiler with Python](https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)
    * You don't need to dive into the details bout the code the author presented, just try to get a high level picture from this post
  * [gcc compilation under the hood](https://medium.com/@schambig/gcc-compilation-under-the-hood-c3b7c1908c92)
    * A good post to understand how `gcc` works


