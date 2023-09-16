
**Table of Contents**
- [Lecture 05: Primitive Data Types and Practices (part III)](#lecture-05-primitive-data-types-and-practices-part-iii)
  - [Lecture topics](#lecture-topics)
  - [Course materials](#course-materials)
  - [Topics to explore](#topics-to-explore)
    - [Read](#read)
    - [Exercise](#exercise)


# Lecture 05: Primitive Data Types and Practices (part III)

## Lecture topics
* [ ] String Data
  * [ ] String indexing
    * Each character of the string is assigned a index number representing its position in the string, and index number starts from 0
    * General indexing format - `StringValue[<lower_index>:<upper_index>]`
      * `<lower_index>` is inclusive
      * `<upper_index>` is exclusive
      * Negative indexing
  * [ ] `f-string` vs. `format()` - You could make the string value dynamic!!
    * ```python
      a = 3
      b = 2
      c = a + b
      print(f'{b} plus {a} is {c}')      
      ```
    * ```python
      a = 3
      b = 2
      c = a + b
      print('{} plus {} is {}'.format(b, a, c))
      print('{B} plus {A} is {C}'.format(B=b, A=a, C=c))
      ```
  * [ ] Alignment format
    * `"{:>10}".format("Test")`
    * `"{:<10}".format("Test")`
    * `"{:^10}".format("Test")`
    * A different approach
      * `"Test".ljust(10, '*')`
      * `"Test".rjust(10, '*')`
      * `"Test".center(10, '*')`
  * [ ] Practice
    * Introduce a person based on information input from keyboard
        ```
        Type in your first name: xx
        Type in your last name: xxxx
        >> Output: Your full name is xx xxxx
        ```
    * Check if a string is a part of another string
        ```
        Type in the 1st string: ab
        Type in the 2nd string: abc
        >> Output: The 1st string ab is in the 2nd string abc
        ```
        ```
        Type in the 1st string: ab
        Type in the 2nd string: bcd
        >> Output: The 1st string ab is not in the 2nd string bcd
        ```
    * What is the first occurrence?
        ```
        Type in the 1st string: ab
        Type in the 2nd string: bcabcdabcde
        >> Output: The 1st string ab is in the 2nd string bcabcdabcde
        >> Output: The first occurrence of string ab in the 2nd string bcabcdabcde is at position 2
        ```
    * Bake a cake!!
  


## Course materials
* [slides](TBD)

## Topics to explore
### Read
* TBD

### Exercise
* TBD
