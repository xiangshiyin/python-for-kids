**Table of Content**
- [Introduction](#introduction)
  - [Schedule (课程安排)](#schedule-课程安排)
  - [Course materials](#course-materials)
  - [Download course materials](#download-course-materials)
  - [Topics](#topics)
- [References](#references)
- [Contact](#contact)
- [Miscellaneous](#miscellaneous)
  - [Github integration with Colab](#github-integration-with-colab)
  - [Dependency management (advanced setting)](#dependency-management-advanced-setting)
  - [Fun stuff](#fun-stuff)

# Introduction
This is a beginner level class for young kids (Grade 6+). The goal is to introduce Python programming basics and help the young folks build the mind set of solving real life problems with the computer programming framework.

这是一门针对青少年的Python编程课，旨在普及基本的Python编程知识，帮助学生培养通过计算机编程解决实际问题的思维方式。课程内容涵盖基本的数据结构，模块控制，基本算法，基本数学和统计应用，以及常用的编程工具和package介绍。每节课会有相应的实际操作环节，同时课后也会安排相应的阅读和调研任务，激发学生独立研究问题的能力


## Schedule (课程安排)
General schedule: 
* School Year 2023-2024 - Saturday from 10:30AM to 12:00PM (每周六上午 10:30-12:00)
  * 地点: 5850 Peachtree Industrial Blvd, Norcross, GA 30071
* School Year 2022-2023 - Saturday from 9:30AM to 10:20AM (每周六上午 9:30-10:20)
  * 地点: 5300 Spalding Dr, Norcross, GA 30092

## Course materials
- [**2023-2024 学年课程安排 (School Year 2023-2024)**](./2023-2024/README.md)
- [**2022-2023 学年课程安排 (School Year 2022-2023)**](./2022-2023/README.md)

## Download course materials
You can follow the instruction [here](./docs/access_course_materials.md)

## Topics
* [x] Data types and computations
* [x] Conditional statements
* [x] Loops and control statements
* [x] String processing
* [x] Basic data structures
* [x] Functions
* [x] Python libraries
* [x] Git and version control
* [x] Classes and objects
* [x] File input and output
* [x] Basic algorithms (search, ranking, etc.)
* [x] Applications in math (geometry, probability, linear algebra, etc.)

More fun stuff to come :-) 

# References
There are many resources from both online and offline for Python learning, below are some examples. You don't necessarily need to buy the books listed here, we'll cover all the necessary content in our class and keep introducing corresponding reading materials as the course proceeds.

针对学习Python编程，您可以找到很多相应的书籍以及网上资源，下面罗列的是一些例子，仅供参考。我们也会随着课程推进针对不同的话题不断推荐一些网上很容易找到的阅读材料。

Example resources:
* Online resource: [Python Tutorials](https://www.w3schools.com/python/default.asp)
* Books
  * [Coding for Kids: Python: Learn to Code with 50 Awesome Games and Activities](https://www.amazon.com/Coding-Kids-Python-Awesome-Activities/dp/1641521759)
  * [Python for Kids: A Playful Introduction To Programming](https://a.co/d/agDd8MN)
  * [Introduction to Programming: A Very Brief Text for the Young and Impatient (Python Edition)](https://www.amazon.com/Introduction-Programming-Brief-Impatient-Python/dp/B09XZMPRV2/ref=sr_1_1?crid=KVSEJZAOX92P&keywords=introduction+to+programming+hong+gongbing&qid=1660940380&s=books&sprefix=introduction+to+programming+hong+gongbing%2Cstripbooks%2C84&sr=1-1)

# Contact
If you have questions with regard to this course, please feel free to follow the contact information listed [here]((https://docs.google.com/presentation/d/1Q35y-fWR4LwFnihzVuaolTxWZ5rCQaf694ZdCtju6yw/edit#slide=id.g145d4dbaba8_0_164)) to contact the instructor. If you want to open the discussion so that other students in the class could join, you could also create an issue on the course site following the instructions listed in the above link.

如果您有问题，可以通过[这里的 Google Slides](https://docs.google.com/presentation/d/1Q35y-fWR4LwFnihzVuaolTxWZ5rCQaf694ZdCtju6yw/edit#slide=id.g145d4dbaba8_0_164) 所列的联系方式和老师沟通。如果问题是关于编程本身并且希望能和其他同学讨论，您也可以按照上述 Google Slides 所列方式在课程网站上发问。

# Miscellaneous
## Github integration with Colab
Check this [reference](https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)

## Dependency management (advanced setting)
* `poetry`: https://python-poetry.org/docs/basic-usage/#project-setup
  * Install `poetry` following the instructions [here](https://python-poetry.org/docs/#installation)
  * If you just want to install the listed dependencies in `poetry.lock`, you can run command `poetry install --no-root` [[*reference*](https://python-poetry.org/docs/basic-usage/#installing-dependencies-only)]
  * To activate the default virtualenv, run command `poetry shell` [[*reference*](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)]

## Fun stuff
* Mermaid diagram [[*link*](https://mermaid.js.org/intro/)]