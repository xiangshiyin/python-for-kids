
**Table of Content**
- [Lecture 24: File Input and Output (part II)](#lecture-24-file-input-and-output-part-ii)
  - [Topics](#topics)
  - [Concepts](#concepts)
    - [File input/output (I/O)](#file-inputoutput-io)
      - [General usage](#general-usage)
      - [Caveat](#caveat)
    - [Read from a file](#read-from-a-file)
    - [Write to a file](#write-to-a-file)
  - [Course materials](#course-materials)
- [Suggested reading](#suggested-reading)

# Lecture 24: File Input and Output (part II)

## Topics
Here are the topics we are going to cover
* [ ] The `pygame` example revisit
* [ ] The working directory problem [[link](../2024-03-16/README.md#coding)]
* [ ] Read from a file with `open()`


## Concepts
### File input/output (I/O) 
#### General usage
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

#### Caveat
- `filepath` - the parameter is expecting the full file directory of the file. However, if the file resides in the same folder where the code is executed (the so-called "working environment"), you can directly put in the file name
- `mode` - here is a list of commonly used modes

    | Character | Mode           | Description                              |
    | --------- | -------------- | ---------------------------------------- |
    | ‘r’       | Read (default) | Open a file for read only                |
    | ‘w’       | Write          | Open a file for write only (overwrite)   |
    | ‘a’       | Append         | Open a file for write only (append)      |
    | ‘r+’      | Read+Write     | open a file for both reading and writing |

### Read from a file
To read the content of a file, we need to call the function `open()` under the `read` mode, such as 
```python
with open(filepath, 'r') as file:
    # operations
```

There are different patterns to fetch the content of a file
* Pattern 1: `file.read()` - read all content as a string
* Pattern 2: `file.readlines()` - read all content as a list of strings (rows)
* Pattern 3: `file.readline()` - read one line at a time
  * You could also use the following pattern
    ```python
    for line in file:
      <operations>
    ```


### Write to a file
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


## Course materials
* slides [TBD]

# Suggested reading
* TBD
* Online resources
  * TBD
