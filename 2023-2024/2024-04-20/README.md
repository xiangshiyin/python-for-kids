
**Table of Content**
- [Lecture 26: Version Control and Git (part II)](#lecture-26-version-control-and-git-part-ii)
  - [Topics](#topics)
  - [Concepts](#concepts)
    - [Install Git](#install-git)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 26: Version Control and Git (part II)

## Topics
Here are the topics we are going to cover
* [ ] Introduction to Git


## Concepts
###  Install Git
* [Official doc](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - installation options for different operation systems (Linux, Mac, Windows, etc.)
* Initialize `git`
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

* Common `git` commands  [[*reference*](http://guides.beanstalkapp.com/version-control/common-git-commands.html)]


## Course materials
* slides [[link](https://docs.google.com/presentation/d/1V3UgsJ_vXLN_qYO2Xe-VDvUkvW_6z8zKf4HqK8BzfAQ/edit?usp=sharing)]

# Suggested reading
* TBD
* Online resources
  * TBD
