
**Table of Content**
- [Lecture 18: Build a Tic-Tac-Toe Game (part II)](#lecture-18-build-a-tic-tac-toe-game-part-ii)
  - [Topics](#topics)
  - [Concepts](#concepts)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)
- [Practice](#practice)

# Lecture 18: Build a Tic-Tac-Toe Game (part II)

## Topics
Here are the topics we are going to cover
* [x] Modify the code for the tic-tac-toe game to cover edge cases like
  * [x] Bad input
  * [ ] Reset game
  * [ ] Quit game
* [ ] Break the code for the tic-tac-toe game to separate files
* [ ] Rewrite the code for the tic-tac-toe game in python class
* [x] Create a graphic user interface (GUI) with `tkinter`


## Concepts
* Widgets in `tkinter` [[source](https://realpython.com/python-gui-tkinter/#working-with-widgets)]
  | Widget Class | Description                                                                           |
  | ------------ | ------------------------------------------------------------------------------------- |
  | Label        | A widget used to display text on the screen                                           |
  | Button       | A button that can contain text and can perform an action when clicked                 |
  | Entry        | A text entry widget that allows only a single line of text                            |
  | Text         | A text entry widget that allows multiline text entry                                  |
  | Frame        | A rectangular region used to group related widgets or provide padding between widgets |

## Course materials
* slides [TBD]

# Suggested reading
* Online resources
  * `tkinter` [documentation](https://docs.python.org/3/library/tkinter.html)
  * [Python GUI Programming With Tkinter](https://realpython.com/python-gui-tkinter/)

# Practice
1. Modify the code in the class demo [[link](./base.py)] for the tic-tac-toe game such that:
   1. Player could quit the game with command "q" and type in "y" to confirm and quit the game
   2. If the player regrets and types in "n" to continue the game, he could still type in "q" to try to quit the game again without being treated as invalid input
   3. Do the same to reset the game in the middle, use the command "reset"
2. Research the usage of the library `tkinter` and build a window interface, such that
   1. The window has a title "Tic Tac Toe"
   2. The window has a box entry for user to type
   3. The window has a button below the box entry
   4. When the user clicks the button, a window should pop up and display the same message the user typed in

(We haven't covered much on the library `tkinter`, so you might need some online research to figure out question 2)