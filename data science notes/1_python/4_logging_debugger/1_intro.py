
##### in simple word we are using this logging modude : this the module which persist the msg
#  permanetly for future investigation. so from this time instead of using print, now we use logging #####

# ----------------------------------------
# 1. What is Logging?
# ----------------------------------------

# Logging means recording messages about what your program is doing.
# It helps you understand the flow of your code and find errors.

# Why use logging?
# - To know what happened and when
# - To track errors without stopping the program
# - To save messages in a file for later review

# ----------------------------------------
# 2. What is Debugging?
# ----------------------------------------

# Debugging means finding and fixing errors (bugs) in your code.
# In VS Code, the debugger allows you to:
# - Pause your program at any line
# - Check the values of variables
# - Step through your code line by line

# Why We Use Logging and Debugger in Python
# Explained in simple language with comments
# Copy-paste ready

# ----------------------------------------
# 1. Why Use Logging?
# ----------------------------------------

# Logging is used to record what your program is doing.
# It helps you understand the flow of execution and find problems.

# Main reasons:
# - To track the behavior of your code (e.g., which function ran, what data was processed)
# - To detect and record errors without stopping the program
# - To save messages in a log file for future analysis
# - To help other developers understand what happened during execution

# Example:
# If a file is missing, logging can show:
# "WARNING | File not found: data.txt"
# This helps you know exactly what went wrong and where.

# ----------------------------------------
# 2. Why Use Debugger?
# ----------------------------------------

# Debugger is used to pause and inspect your code while it's running.
# It helps you find and fix bugs step by step.

# Main reasons:
# - To stop the program at a specific line (using breakpoints)
# - To check the values of variables at any point
# - To step through the code line by line and understand the logic
# - To test different conditions without changing the code

# Example:
# If your function is not returning the expected result,
# you can set a breakpoint and check the value of each variable.

# ----------------------------------------
# 3. When to Use Logging vs Debugger
# ----------------------------------------

# Use logging when:
# - You want to keep a record of events
# - You want to monitor your program without stopping it
# - You are working on a large project or production code

# Use debugger when:
# - You are actively fixing a bug
# - You want to inspect variables and flow in real-time
# - You are learning how a piece of code works

# ----------------------------------------
# 4. Summary
# ----------------------------------------

# Logging = Write messages to understand what happened
# Debugger = Pause and inspect code to fix issues

# Both are powerful tools for writing better, error-free code.
# Use them together to make your programs easier to understand and maintain.

# ---------------------------------------------------------------------------------------------
#  Logging Setup in Python #########################################
# ----------------------------------------------------------------------------------------------

# Step 1: Import the logging module
import logging

# Step 2: Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("app.log"),       # Save logs to a file
        logging.StreamHandler()               # Show logs in terminal
    ]
)

# ----------------------------------------
#  File Handling Example with Logging
# ----------------------------------------

# Function to write content to a file
def write_file(filename, content):
    logging.info("Writing to file: %s", filename)  # Info log
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        logging.debug("Wrote %d characters", len(content))  # Debug log
    except Exception as e:
        logging.exception("Error writing to file")  # Exception log with traceback

# Function to read content from a file
def read_file(filename):
    logging.info("Reading file: %s", filename)  # Info log
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        logging.debug("Read %d characters", len(data))  # Debug log
        return data
    except FileNotFoundError:
        logging.warning("File not found: %s", filename)  # Warning log
        return ""
    except Exception as e:
        logging.exception("Error reading file")  # Exception log
        return ""

# ----------------------------------------
#  Main Program
# ----------------------------------------

# Writing and reading a sample file
write_file("sample.txt", "Hello Kartik\nThis is a test file")
content = read_file("sample.txt")
logging.info("File content:\n%s", content)  # Info log showing file content



# ----------------------------------------
# 1. What are Logging Levels?
# ----------------------------------------

# Logging levels define the importance or severity of a message.
# Python has 5 standard logging levels:
# DEBUG, INFO, WARNING, ERROR, CRITICAL

# Each level has a numeric value and a purpose.

# ----------------------------------------
# 2. Logging Levels Table
# ----------------------------------------

# Level Name     | Numeric Value | Purpose
# ---------------|---------------|----------------------------------------
# DEBUG          | 10            | Detailed information for debugging
# INFO           | 20            | General information about program flow
# WARNING        | 30            | Something unexpected, but not an error
# ERROR          | 40            | A serious problem that caused failure
# CRITICAL       | 50            | A very serious error, program may crash

# ----------------------------------------
# 3. How to Use Logging Levels
# ----------------------------------------

import logging

# Set up logging with minimum level as DEBUG
logging.basicConfig(
    level=logging.DEBUG,  # This will show all levels from DEBUG and above
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Logging messages at different levels
logging.debug("This is a DEBUG message")       # Used for internal details
logging.info("This is an INFO message")        # Used for successful steps
logging.warning("This is a WARNING message")   # Used for recoverable issues
logging.error("This is an ERROR message")      # Used for serious failures
logging.critical("This is a CRITICAL message") # Used for fatal errors

# ----------------------------------------
# 4. When to Use Each Level
# ----------------------------------------

# DEBUG:
# - Use when you want to see variable values, function calls, or loops
# - Example: logging.debug("x = %d", x)

# INFO:
# - Use to show that something worked correctly
# - Example: logging.info("File saved successfully")

# WARNING:
# - Use when something might go wrong, but the program can continue
# - Example: logging.warning("File not found, using default")

# ERROR:
# - Use when something failed and needs attention
# - Example: logging.error("Failed to connect to database")

# CRITICAL:
# - Use when the program cannot continue
# - Example: logging.critical("System crash, shutting down")

# ----------------------------------------
# 5. Changing Logging Level
# ----------------------------------------

# You can change the level to control what gets printed
# Example: level=logging.INFO will hide DEBUG messages

# ----------------------------------------
# End of Logging Levels Notes
# ----------------------------------------

# Use logging levels to organize your messages and make debugging easier.
# They help you filter important information and track problems clearly.
# ----------------------------------------
#  Debugging in VS Code
# ----------------------------------------

# Steps to use debugger:
# - Click left of line number to set breakpoint
# - Press F5 to start debugging
# - Use F10 to step over, F11 to step into, Shift+F11 to step out
# - Hover over variables to see values
# - Use Watch panel to track variables

# ----------------------------------------
# 8. Summary
# ----------------------------------------

# Logging helps you track what your code is doing
# Debugger helps you pause and inspect your code
# Use both together to find and fix bugs easily
# Save logs in a file (app.log) to review later



# ----------------------------------------
# Logging Level Filtering in Python
# ----------------------------------------
# Copy-paste ready explanation with examples

import logging

# ----------------------------------------
# 1. Logging Level Hierarchy
# ----------------------------------------
# Each level has a numeric value.
# Messages are shown only if their level >= current logging level.

# Level Name   | Numeric Value
# -------------|---------------
# NOTSET       | 0
# DEBUG        | 10
# INFO         | 20
# WARNING      | 30
# ERROR        | 40
# CRITICAL     | 50

# ----------------------------------------
# 2. Behavior When Logging Level is Set
# ----------------------------------------

# If you set logging level to INFO:
# - DEBUG is ignored (lower than INFO)
# - INFO, WARNING, ERROR, CRITICAL are shown

# If you set logging level to WARNING:
# - DEBUG and INFO are ignored
# - WARNING, ERROR, CRITICAL are shown

# ----------------------------------------
# 3. Example: Set Level to INFO
# ----------------------------------------

logging.basicConfig(level=logging.INFO)

logging.debug("This is DEBUG")         # ❌ Not shown
logging.info("This is INFO")           # ✅ Shown
logging.warning("This is WARNING")     # ✅ Shown
logging.error("This is ERROR")         # ✅ Shown
logging.critical("This is CRITICAL")   # ✅ Shown


# ----------------------------------------
# 4. Rule of Thumb
# ----------------------------------------

# Only messages with severity >= current logging level are printed.
# Lower levels are filtered out.

# ----------------------------------------
# 5. Summary Table
# ----------------------------------------

# Set Level To | Messages Shown
# -------------|-------------------------------
# DEBUG        | DEBUG, INFO, WARNING, ERROR, CRITICAL
# INFO         | INFO, WARNING, ERROR, CRITICAL
# WARNING      | WARNING, ERROR, CRITICAL
# ERROR        | ERROR, CRITICAL
# CRITICAL     | CRITICAL only

# ----------------------------------------
# Use and Features of format in Logging
# ----------------------------------------
# Copy-paste ready explanation with examples

import logging

# ----------------------------------------
# 1. What is format in logging?
# ----------------------------------------

# The format parameter defines how each log message will look.
# It controls the structure and content of the log output.

# Example format string:
# "%(asctime)s | %(levelname)s | %(message)s"

# This means:
# - %(asctime)s   → Timestamp of the log
# - %(levelname)s → Logging level (INFO, DEBUG, etc.)
# - %(message)s   → The actual log message

# ----------------------------------------
# 2. Why use format?
# ----------------------------------------

# - To make logs easier to read and understand
# - To include useful information like time, level, filename, line number
# - To customize logs for debugging or production use

# ----------------------------------------
# 3. Common Format Fields
# ----------------------------------------

# Field Name      | Meaning
# ----------------|------------------------------------------
# %(asctime)s     | Time when the log was created
# %(levelname)s   | Logging level (e.g., INFO, ERROR)
# %(message)s     | The actual log message
# %(name)s        | Name of the logger
# %(filename)s    | Name of the file where log was called
# %(lineno)d      | Line number in the source code
# %(funcName)s    | Function name where log was called
# %(threadName)s  | Thread name (for multithreading)
# %(process)d     | Process ID

# ----------------------------------------
# 4. Example: Using format in logging
# ----------------------------------------

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
)

# Sample log messages
logging.debug("Debugging started")
logging.info("Process running")
logging.warning("Low disk space")
logging.error("File not found")
logging.critical("System crash")

# Output will look like:
# 2025-08-10 23:55:01 | DEBUG    | myscript.py:45 | Debugging started
# 2025-08-10 23:55:01 | INFO     | myscript.py:46 | Process running
# ...

# ----------------------------------------
# 5. Customizing Format
# ----------------------------------------

# You can change the format to include only what you need.
# Example: Only show level and message
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Output:
# INFO: Process running
# WARNING: Low disk space

# ----------------------------------------
# 6. Summary
# ----------------------------------------

# format helps you control how logs appear
# It makes logs more readable and informative
# You can include time, level, filename, line number, and more



# at last after completion of work we have to shutdown it i.e 
logging.shutdown()