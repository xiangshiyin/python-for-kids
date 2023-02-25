
**Table of Content**
- [Lecture 20: Python Libraries and How To Use Them (part III)](#lecture-20-python-libraries-and-how-to-use-them-part-iii)
- [Topics to Explore](#topics-to-explore)
  - [Reading](#reading)
  - [Coding](#coding)


# Lecture 20: Python Libraries and How To Use Them (part III)
For this class, we continued with content that we didn't get time to finish in our previous class, including 
* Fix the aspect ratio in the circle drawing example to make the circle look like a circle
* Different ways to import a python library, including patterns like
  * Import the whole library via `import package_name`
  * Import the whole python module via `import ancestor.grandparent.parent.child` where `child` represents a python module `child.py`
  * Make the object referencing string of hierarchy shorter, by
    *  Define an alias such as `import ancestor.grandparent.parent.child as c` where `child` represents a python module `child.py`
    *  Use the `from ancestor.grandparent.parent import child` pattern
  * We didn't get time to cover this, but you could also directly import an object (variable, function, class, etc.) within a python module follow the pattern below
    * `from ancestor.grandparent.parent.child import talent` where `child` represents a python module `child.py`

(*Check the notes from [Lecture 19](../2023-02-11/README.md) and [code samples](../2023-02-25/practice.ipynb) for more details*)

As we talked in class, the keys to understand why certain import statement works are
* Understand the python library/package file structure (ideal case, time consuming, but the test practice)
  * A lot of python libraries' code bases are hosted on github, such as [matplotlib](https://github.com/matplotlib/matplotlib)
* Research the python library documentation, follow the tutorials and find code samples that are close to your use case
  * Such as the documentation on [`matplotlib`](https://matplotlib.org/stable/index.html)
* Google the best practices and follow :) 

# Topics to Explore
## Reading
Same as last class, explore the following libraries (or pick one)
* `turtle`
  * Tutorial - https://realpython.com/beginners-guide-python-turtle/
  * The official doc - https://docs.python.org/3/library/turtle.html
* `pygame`
  * Introduction - https://www.pygame.org/docs/tut/PygameIntro.html
  * The official doc - https://www.pygame.org/docs/
* `music21` - http://web.mit.edu/music21/

## Coding
For this week's coding practice, I'd like you to carefully look at the code sample I shared at the end of the class to draw a moving straight line and see if you can roughly understand what it does.

Some reference you might want to check
* The `animation` module of library `matplotlib` [[*link*]](https://matplotlib.org/stable/api/animation_api.html)
* An animated line plot [[*link*]](https://matplotlib.org/stable/gallery/animation/simple_anim.html)

