
**Table of Content**
- [Lecture 17: Build a Tic-Tac-Toe Game](#lecture-17-build-a-tic-tac-toe-game)
  - [Topics](#topics)
  - [Questions](#questions)
  - [Flow Chart](#flow-chart)
    - [Case #1](#case-1)
    - [Case #2](#case-2)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)
- [Assignment](#assignment)

# Lecture 17: Build a Tic-Tac-Toe Game

## Topics
In this lecture, we are going to build a tic-tac-toe game together
* Reference: https://www.youtube.com/watch?v=Q6CCdCBVypg&ab_channel=CDcodes


## Questions
* What do we need to set up the game?
* What are the rules?
* What could be the possible states of the game?
* What input do we need?
* What output do we need?

## Flow Chart
### Case #1
```mermaid
graph LR;
    A[Start] --> I[Display the Board];
    I --> B[Input Position];
    B --> H[Valid Position?];
    H --> |YES| C[Update the Board];
    H --> |NO| B;
    C --> D[Display the Board];
    D --> E[Check Win];
    E --> |YES|F[End Game];
    E --> |NO|G[Check Tie];
    G --> |YES|F;
    G --> |NO|B;
```
### Case #2
```mermaid
graph LR;
    A[Start] --> B[Input];
    B --> C[Restart];
    B --> D[Quit];
    B --> E[Valid Position?];
    C --> |Reset Board|A;
    D --> F[End Game]
    E --> |NO|B;
    E --> |YES|G[Update the Board];
    G --> H[Display the Board];
    H --> I[Check Tie];
    I --> |YES|F;
    I --> |NO|J[Check Win];
    J --> |YES|F;
    J --> |NO|B;
```


## Course materials
* slides [[link](TBD)]

# Suggested reading
* (Good to read, we'll catch this up later) Build a tic-tac-toe game with GUI (graphic user interface): https://realpython.com/tic-tac-toe-python/

# Assignment
* Add additional functions to
  * Check abnormal input (invalid position)
  * Enable game reset
  * Enable existing the game
* Optimize the code we created [[code](./tic-tac-toe.py)]