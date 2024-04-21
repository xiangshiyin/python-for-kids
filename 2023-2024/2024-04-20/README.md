
**Table of Content**
- [Lecture 26: Version Control and Git (part II)](#lecture-26-version-control-and-git-part-ii)
  - [Topics](#topics)
  - [Prerequisites](#prerequisites)
  - [Concepts](#concepts)
    - [Initialize Git](#initialize-git)
    - [Common `git` commands](#common-git-commands)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)
- [Assignment](#assignment)

# Lecture 26: Version Control and Git (part II)

## Topics
Here are the topics we are going to cover
* [x] Introduction to Git & Github
* [ ] Hands-on practice with GitHub


## Prerequisites
Before our class, please install `git` and set up a github account following the instructions below:
* Install `git`
  * [**Option 1**] Stepwise instructions from github: https://docs.github.com/en/get-started/getting-started-with-git/set-up-git
  * [**Option 2**] Official instructions from `git`: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* Create a github account and set up the local connection with github
  * Check **`part 1`** of https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account

## Concepts
###  Initialize Git
* You can set some global level user information so that `git` knows who is making the code changes, some commands like 
  ```sh
  git config --global user.email "me@example.com"
  git config --global user.name "my name"
  ```
* Then you can either start a new project folder from scratch at local or clone a remote one to local
  * To start from scratch at local
    * Create a new project folder
    * Navigate to the folder location from your command line console (`Terminal` app in Mac or `Powershell`/`Command Line Prompt` in Windows)
    * Run command `git init` to let `git` start tracking all the file changes happening under the project folder
  * To clone a remote repository
    * Navigate to the remote repository page in your browser
    * Click the green color `Code` button on the page, copy the url
    * Navigate to the location where you want to land the code from your command line console, run the command `git clone <url>` to download the remote code repository (also called *`repo`*)

### Common `git` commands  
[[*reference*](http://guides.beanstalkapp.com/version-control/common-git-commands.html)]

## Course materials
* slides [[link](https://docs.google.com/presentation/d/1V3UgsJ_vXLN_qYO2Xe-VDvUkvW_6z8zKf4HqK8BzfAQ/edit?usp=sharing)]

# Suggested reading
* `git` integration in `Spyder` [[link](https://www.geeksforgeeks.org/how-to-install-git-with-spyder/)]

# Assignment
* Can you do some research online and do the following things?
  * Create a github repo
  * Push a file to the repo

