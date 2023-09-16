
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
  * [ ] Alignment format ([read more](https://www.geeksforgeeks.org/python-string-ljust-rjust-center/))
      * `"Test".ljust(10, '*')`
      * `"Test".rjust(10, '*')`
      * `"Test".center(10, '*')`
  * [ ] Practice
    * Introduce a person based on input from the keyboard
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
    * Can you bake me a cake like this?
        ```
                                                0000000000                                             
                                                0000000000                                             
                                                0000000000                                             
                                           00000000000000000000                                        
                                           00000000000000000000                                        
                                           00000000000000000000                                        
                                 0000000000000000000000000000000000000000                              
                                 0000000000000000000000000000000000000000                              
                                 0000000000000000000000000000000000000000         
        ```
* [ ] Boolean - `True/False`
  * [ ] Comparison is the most common way to generate `True/False` values
    | Operator | Meaning                         |
    | -------- | ------------------------------- |
    | A > B    | A is greater than B             |
    | A < B    | A is smaller than B             |
    | A == B   | A is equal to B                 |
    | A != B   | A is not equal to B             |
    | A >= B   | A is greater than or equal to B |
    | A <= B   | A is smaller than or equal to B |
  * Evaluating if a `fact` is (`equal to`) `True` could also generate `True/False` values
    * `'ab' in 'abc'`
  * [ ] Logical operators - Consider multiple scenarios
    | Operator   | Meaning |
    | ---------- | ------- |
    | `and`, `&` | AND     |
    | `or`, `\|` | OR      |
    | `not`, `!` | NOT     |
  * [ ] Practice
    * Check if the input number is divisible by number 3
    * Check if the input number is divisible by number 6
    * Check if the input number is divisible by either 3 and 6
    * Check if the input number is divisible by either 3 or 6


## Course materials
* [slides](https://docs.google.com/presentation/d/1_tSq05rTBsNlgAnTkXC-PN_KMQmqDj5xYVHZIDz3m6w/edit?usp=sharing)

## Topics to explore
### Read
* TBD

### Exercise
* TBD
