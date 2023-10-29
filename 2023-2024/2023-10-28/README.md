
**Table of Content**
- [Lecture 10: Loop (part III)](#lecture-10-loop-part-iii)
  - [Topics](#topics)
  - [Exercises](#exercises)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
  - [Assignment](#assignment)
- [Suggested reading](#suggested-reading)

# Lecture 10: Loop (part III)

## Topics
Here are the topics we are going to cover
* [x] `for` loop wrap-up
* [x] Brief introduction on `list`

## Exercises
* Generate top N Fibonacci numbers with `for` loop
* Write a program to generate the Pascal's triangle [[wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)]
  * 杨辉三角形 [[wikipedia](https://zh.wikipedia.org/wiki/%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%E5%BD%A2)] 
  
    ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/83e43c795c7cba79bf4b6a4a3cdfa0f3e52b5fd5)

## Concepts
* `for` loop is used when you want to repeat a fixed number of times
* How to jump out of a `for` loop
  * Option 1: finish the last iteration
  * Option 2:
  ```python
  for i in range(N):
      <action 1>
      break
      <action 2>
  ```
  ```python
  for i in range(N):
      if <condition>:
         break
      <action>
  ```
* How to skip a `for` loop
  ```python
  for i in range(N):
      if <condition>:
        <action>
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
* slides [[link](https://docs.google.com/presentation/d/1sVdt_rDsiID9sK7AUYpSa2N4td5iPdIdzyVd0CoEnww/edit?usp=sharing)]

## Assignment
Based on what we learnt in class, write a program to print first `N` layers of the Pascal's triangle where `N` is a variable of positive integers ($N>0$).
* Hint
  * To create an empty list, you could do `layer = []`
  * To add an additional element (such as `0`) to the list, you could either do `layer = layer + [0]` or `layer.append(0)`

# Suggested reading
* TBD
* Online resources
  * TBD
