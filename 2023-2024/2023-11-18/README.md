
**Table of Content**
- [Lecture 13: Function (part I)](#lecture-13-function-part-i)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 13: Function (part I)

## Topics
Here are the topics we are going to cover
* [ ] Dictionary and examples
  * [ ] Find the birthday by name
  * [ ] Count the letter frequency
* [ ] Brief introduction on `tuple` and `set`
* [ ] Function and examples
  * [ ] Convert Fahrenheit temperature to Celsius temperature `C = (F - 32) x 5/9`
  * [ ] A calculator to support `+`, `-`, `*`, `/`
  * [ ] Coin flip with `random.randint(0,1)`
  * [ ] Sum of a `list`


## Concepts
* `Set` operations
  | Operation            | Python Code                            |
  | -------------------- | -------------------------------------- |
  | union                | `A \| B` or `A.union(B)`               |
  | intersect            | `A & B` or `A.intersection(B)`         |
  | difference           | `A - B` or `A.difference(B)`           |
  | symmetric difference | `A ^ B` or `A.symmetric_difference(B)` |
* Define a `function`
  ```python
  def function_name():
      <logic>
  ```
  or
  ```python
  def function_name():
      <logic>
      return <output>
  ```
  or
  ```python
  def function_name(param1, param2, ...):
      <logic>
  ```
  or
  ```python
  def function_name(param1, param2, ...):
      <logic>
      return <output>
  ```
* Call a function
  ```python
  function_name()
  ```
  or
  ```python
  function_name(param1=value1, param2=value2)
  ```




## Course materials
* slides [[link](https://docs.google.com/presentation/d/1rCKOl24JqiOFymqJ7BYfN1H1CTf-8pifW5ikBB29rpU/edit?usp=sharing)]

# Suggested reading
* Online resources
  * `Function` in Python [[link](https://www.w3schools.com/python/python_functions.asp)]
