
**Table of Content**
- [Lecture 23: File Input and Output in Python (part I)](#lecture-23-file-input-and-output-in-python-part-i)
  - [File input/output (I/O)](#file-inputoutput-io)
    - [General usage](#general-usage)
    - [Caveat](#caveat)
  - [Read from a file](#read-from-a-file)
  - [Write to a file](#write-to-a-file)
- [Topics to Explore](#topics-to-explore)
  - [Reading](#reading)
  - [Coding](#coding)


# Lecture 23: File Input and Output in Python (part I)

## File input/output (I/O) 
### General usage
In Python, we normally use the `open()` function to interact with files and deal with the read and write operations
- `read` - fetch the content from a file
- `write` - write new content to a file, this could include
  - Write content to a new file
  - Overwrite a pre-existing file
  - Append content to a pre-existing file

Typically, there are two ways to interact with files with the `open()` function, in which the `open()` function returns a file object to handle the file input/output (I/O):
- Option 1
    ```python
    # Open a file
    file = open(filepath, mode)

    # Operations

    # Close the file
    file.close()
    ```
- Option 2
    ```python
    # Open a file using a with statement
    with open(filepath, mode) as file:
        # operations

    # The file object is automatically closed when the code block is finished
    ```

### Caveat
- `filepath` - the parameter is expecting the full file directory of the file. However, if the file resides in the same folder where the code is executed (the so-called "working environment"), you can directly put in the file name
- `mode` - here is a list of commonly used modes

    | Character | Mode           | Description                              |
    | --------- | -------------- | ---------------------------------------- |
    | ‘r’       | Read (default) | Open a file for read only                |
    | ‘w’       | Write          | Open a file for write only (overwrite)   |
    | ‘a’       | Append         | Open a file for write only (append)      |
    | ‘r+’      | Read+Write     | open a file for both reading and writing |

## Read from a file
To read the content of a file, we need to call the function `open()` under the `read` mode, such as 
```python
with open(filepath, 'r') as file:
    # operations
```

To fetch the content, we could run the command `file.readlines()` to load the content of the file into a `list`. Each element of the `list` represent a line of the file. Here is an example:
```python
with open(filepath, 'r') as file:
    # operations
    line = file.readline()
    print(line)
```


We could also run the command `file.readline()` to only return the content one line a time.


## Write to a file
To write some given content to a file, we need to call the function `open()` under the `write` mode, such as
```python
with open(filepath, 'w') as file:
    # operations
```

To write certain content to the given file, we could run the command `file.write(content)`. Here is an example:
```python
with open(filepath, 'w') as file:
    # operations
    line = 'This is the first line'
    file.write(line)
```

# Topics to Explore

## Reading
- Read and write to a text file from a Python program [[link](https://muzny.github.io/csci1200-notes/10/1/fileio.html#reading-from-files)]

## Coding
- Can you write a simple script to check what is the most frequently used word in `Harry Potter And The Socerer's Stone`?





