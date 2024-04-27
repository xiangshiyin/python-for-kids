
**Table of Content**
- [Lecture 27: Algorithm (part I) - Search](#lecture-27-algorithm-part-i---search)
  - [Topics](#topics)
  - [Concepts](#concepts)
    - [Recap of `git` commands used](#recap-of-git-commands-used)
    - [Different search algorithms (Linear Search vs. Binary Search)](#different-search-algorithms-linear-search-vs-binary-search)
    - [Bubble Sort](#bubble-sort)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)
- [Practice](#practice)

# Lecture 27: Algorithm (part I) - Search

## Topics
Here are the topics we are going to cover
* [X] Hands-on practice with Github
  * [X] Create an empty repository
  * [X] Add a new file to the repository
  * [X] Pull a remote repository
  * [x] Contribute to a remote repository
* [ ] Search algorithm - Linear vs. Binary

## Concepts
### Recap of `git` commands used
  ```
  git init
  git add
  git status
  git log -s
  git commit -m "<a commit mesage>"
  git reset HEAD~1
  git reset --hard HEAD~1
  git reset <commit_id>
  git reset --hard <commit_id>
  ```

### Different search algorithms (Linear Search vs. Binary Search)
![](./pics/search_algo.gif)
Question: Does it matter if the list is sorted or not?

### Bubble Sort
![](./pics/bubble_sort_avg.gif)


## Course materials
* slides [[link](https://docs.google.com/presentation/d/1V3UgsJ_vXLN_qYO2Xe-VDvUkvW_6z8zKf4HqK8BzfAQ/edit?usp=sharing)]

# Suggested reading
* Binary search [implementation](https://www.programiz.com/dsa/binary-search)

# Practice
* Write a program to implement binary search
  * Input: 
    * `alist`: a sorted list of integers
    * `target`: an integer
  * Output:
    * If you can find the target nubmer from the list, print the message "Found the target" and the number of steps it took
    * If you can't find the traget, print the message "Can't find the target" and the number of steps it took
