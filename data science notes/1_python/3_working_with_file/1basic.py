# Working with Files in Python

# 1. Opening a File
# Syntax: open(filename, mode)
# -----------------------------------------------------------
# Theory: File Modes in Python
# -----------------------------------------------------------

# "r"  - Read mode (default)
#       Opens the file for reading only.
#       The file pointer is placed at the beginning of the file.
#       If the file does not exist, an error is raised.

# "w"  - Write mode
#       Opens the file for writing only.
#       If the file exists, all previous data is erased.
#       If the file does not exist, a new file is created.

# "a"  - Append mode
#       Opens the file for writing.
#       The file pointer is at the end of the file.
#       If the file does not exist, a new file is created.
#       Data written is added after the existing content.

# "x"  - Exclusive creation
#       Creates a new file and opens it for writing.
#       If the file already exists, the operation fails with an error.

# "b"  - Binary mode
#       Opens the file in binary mode (e.g., "rb", "wb").
#       Used for non-text files like images, audio, etc.

# "t"  - Text mode (default)
#       Opens the file in text mode (e.g., "rt", "wt").
#       Used for text files (default mode).

# "+"  - Update mode (read and write)
#       Opens the file for both reading and writing (e.g., "r+", "w+", "a+").
#       The file pointer position and file creation/erasure depend on the first character ("r", "w", or "a").

# -----------------------------------------------------------
# Mode Combinations and Their Use
# -----------------------------------------------------------
# "rt"  - Read text (default)
# "rb"  - Read binary
# "wt"  - Write text
# "wb"  - Write binary
# "at"  - Append text
# "ab"  - Append binary
# "r+"  - Read and write (file must exist)
# "w+"  - Write and read (overwrites or creates file)
# "a+"  - Append and read (creates file if not exists)
# "x+"  - Create and read/write (fails if file exists)

# -----------------------------------------------------------
# Summary Table
# -----------------------------------------------------------
# | Mode | Description                                      |
# |------|--------------------------------------------------|
# |  r   | Read (default), error if file not found          |
# |  w   | Write, creates or overwrites file                |
# |  a   | Append, creates file if not exists               |
# |  x   | Create, fails if file exists                     |
# |  b   | Binary mode                                      |
# |  t   | Text mode (default)                              |
# |  +   | Read and write                                   |

# You can combine these modes as needed, e.g., "rb", "w+", "a+

# Example: Opening a file for reading
f = open("example.txt", "r")  # Opens file in read mode

# 2. Reading from a File
content = f.read()            # Reads entire file as a string
print(content)

# Or read line by line
# line = f.readline()        # Reads one line at a time
# lines = f.readlines()      # Reads all lines into a list

# Example: Different Ways of Reading a File in Python

# 1. Using read() - Reads the entire file as a single string
with open("example.txt", "r") as f:
    content = f.read()
    print("Using read():")
    print(content)

# 2. Using readline() - Reads one line at a time
with open("example.txt", "r") as f:
    print("\nUsing readline():")
    line1 = f.readline()
    print("First line:", line1.strip())
    line2 = f.readline()
    print("Second line:", line2.strip())


with open("example.txt", "r") as f:
    print("Reading lines using readline() in a loop:")
    while True:
        line = f.readline()
        if not line:  # If line is empty, end of file is reached
            break
        print(line.strip())



# 3. Using readlines() - Reads all lines into a list
with open("sample.txt", "r") as f:
    print("Read all lines into a list:")
    lines = f.readlines()
    for line in lines:
        print(line.strip())


# The strip() function in Python is used to remove any leading (spaces at the beginning)
# and trailing (spaces or newline characters at the end) whitespace characters from a string.

# Example:
line = "  Hello, world!  \n"
print(line.strip())  # Output: "Hello, world!"

# In the given examples, strip() is used to remove the newline character '\n' at the end of each line
# when printing lines read from a file, so the output looks clean

# we can also avoid this func, simply write : --> print (line)



# 3. Closing a File
f.close()                     # Always close the file when done

# 4. Writing to a File
f = open("example.txt", "w")  # Opens file in write mode (overwrites)
f.write("Hello, world!\n")
f.write("This is a new line.\n")
f.close()

# 5. Appending to a File
f = open("example.txt", "a")  # Opens file in append mode
f.write("Appended line.\n")
f.close()

# 6. Using 'with' Statement (Best Practice)
# Automatically closes the file, even if an error occurs
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

# 7. Working with Binary Files
# with open("image.png", "rb") as f:
#     data = f.read()

# 8. Checking if File Exists (optional)
import os
if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")


# seek() Function in File Handling

# The seek() function is used to change the file pointer position within an open file.
# It allows you to move to a specific byte in the file, so you can read or write from that position.

# Syntax:
# file_object.seek(offset, whence)
# - offset: Number of bytes to move the pointer.
# - whence: (optional) Reference point for offset.
#   0 = beginning of file (default)
#   1 = current file position
#   2 = end of file

# Example: Move to the beginning of the file and read again
with open("text.txt", "r") as f:
    print(f.read())      # Reads the whole file, pointer is now at the end
    f.seek(0)            # Move pointer back to the start
    print(f.read())      # Reads the whole file again

# Example: Move to a specific position
with open("text.txt", "r") as f:
    f.seek(5)            # Move pointer to the 6th byte
    print(f.read())      # Reads from the 6th byte to the end

# seek() is useful for re-reading, skipping, or overwriting specific parts of a file.


# 8. finding size of file 
import os

file_path = 'example.txt'  # Replace with your file name
size_in_bytes = os.path.getsize(file_path)

print(f"Size of '{file_path}' is {size_in_bytes} bytes")


# 9. if we want to delete the file 
os.remove ("file_name")

# 10. if we want to rename the existing file
os.rename("old_file_name", "new_file_name")

# 11. if we want to copy a file
#  Importing required module
import shutil

# Source file path (the file you want to copy)
source_file = 'source.txt'  # Replace with your actual source file name

# Destination file path (the file where content will be copied)
destination_file = 'destination.txt'  # Replace with your desired destination file name

#  Using shutil.copyfile() to copy contents
# This function copies the content of source_file to destination_file and if detination_file 
# doesnot exist then it will create first and then copy it.
try:
    shutil.copyfile(source_file, destination_file)
    print(f" File copied successfully from '{source_file}' to '{destination_file}'")
except FileNotFoundError:
    print(" Source file not found. Please check the file name and path.")
except PermissionError:
    print(" Permission denied. You might not have access to read/write the file.")
except Exception as e:
    print(f" An error occurred: {e}")

#  try and except are used for error handling in Python.

#. Code that might cause an error is written inside the try block.

#  If an error occurs, Python jumps to the except block.

#  This prevents the program from crashing and allows you to handle the error.

# You can catch specific errors like FileNotFoundError, ValueError, etc.

#  You can use multiple except blocks to handle different types of errors.

#  General syntax:
#    try:
#        # risky code
#    except ErrorType:
#        # error handling code

# Example:
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("Invalid input. Please enter a number.")

#  Common exceptions:
#    - FileNotFoundError: file does not exist
#    - ZeroDivisionError: division by zero
#    - ValueError: wrong value type
#    - PermissionError: access denied

#  Using try-except makes your program more robust and user-friendly.

# Summary:
# - Always close files after use (or use 'with' statement)
# - Choose the correct mode for your operation
# - Use 'with' for safer


# -----------------------------------------------------------
# Important Concepts about Writing to Files in Python
# -----------------------------------------------------------
# 1. When you open a file in "w" (write) mode, if the file already exists, all previous data will be erased.
#    Only the new data you write will be saved in the file.
# 2. The changes you make (writing or appending) are actually saved to the file only after you call the close() method,
#    or when the file is closed automatically (for example, using the 'with' statement).
# 3. If you open a file in "a" (append) mode, new data will be added to the end of the file without removing the existing content.
# 4. If you open a file in "w" mode again, it will clear the file and start fresh with only the new data you write.

# Example:
# f = open("data.txt", "w")
# f.write("First line\n")
# f.close()
# # Now, "data.txt" contains only "First line"

# f = open("data.txt", "w")
# f.write("Second line\n")
# f.close()
# # Now, "data.txt" contains only "Second line" (the previous content is removed)

# f = open("data.txt", "a")
# f.write("Third line\n")
# f.close()
# # Now, "data.txt" contains:
# # Second line
# # Third line

# Always remember to close the file after writing to ensure data is saved properly. 

# Using 'with' Statement for File Handling in Python

# The 'with' statement is the recommended way to work with files.
# It automatically closes the file when the block inside 'with' is exited,
# even if an error occurs. This makes your code safer and cleaner.

# Example: Writing to a file using 'with'
with open("text.txt", "w") as f:
    f.write("This file is written using the 'with' statement.")

# Example: Reading from a file using 'with'
with open("text.txt", "r") as f:
    content = f.read()
    print(content)

# You do not need to call f.close() when using 'with'.
# The file is closed automatically after the indented blocks.



# -----------------------------------------------------------
# Additional Important Points about File Handling in Python
# -----------------------------------------------------------

# 1. Exception Handling:
#    It's good practice to use try-except blocks when working with files to handle errors (like file not found).
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")

# 2. File Pointer:
#    After reading or writing, the file pointer moves to the end. You can use f.seek(0) to move it back to the start.
with open("text.txt", "r") as f:
    f.seek(0)  # Move pointer to the beginning
    print(f.read())

# 3. flush():
#    The flush() method can be used to force write data to disk without closing the file.
with open("text.txt", "a") as f:
    f.write("Flushed line.\n")
    f.flush()  # Forces data to be written to disk

# 4. Context Manager:
#    You can create your own context manager for custom file-like operations using __enter__ and __exit__ methods.

# 5. Reading/Writing Large Files:
#    For very large files, read/write in chunks or line by line to avoid memory issues.

# 6. os and shutil modules:
#    Use os and shutil modules for advanced file operations like renaming, deleting, copying, and moving files.

# 7. Encoding:
#    Specify encoding (like 'utf-8') when working with files containing special characters.
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("हैलो वर्ल्ड")




