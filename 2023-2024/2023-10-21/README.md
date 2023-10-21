
**Table of Content**
- [Lecture 09: Loops (part II)](#lecture-09-loops-part-ii)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 09: Loops (part II)

## Topics
Here are the topics we are going to cover
* [ ] Recap on `while` loop
* [ ] `for` loop in Python
* [ ] Brief introduction on `list` in Python


## Concepts
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
