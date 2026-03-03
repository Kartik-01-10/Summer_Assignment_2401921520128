
# ─────────────────────────────────────────────────────────────
# 🔷 WHAT IS MULTITHREADING? : by this we can call function many times by writing single line code
# Multithreading is a technique where multiple threads run concurrently within a single process.
# Each thread shares the same memory space but executes independently.
# It's ideal for I/O-bound tasks like file operations, network calls, or user input handling.

# ─────────────────────────────────────────────────────────────
# 🔷 WHY USE MULTITHREADING?
# - To improve performance for I/O-bound operations
# - To keep applications responsive (e.g., GUI, web servers)
# - To perform multiple tasks seemingly at the same time

# ─────────────────────────────────────────────────────────────
# 🔷 THREADING VS MULTIPROCESSING
# Python has a Global Interpreter Lock (GIL) which allows only one thread to execute Python bytecode at a time.
# ➤ Use threading for I/O-bound tasks
# ➤ Use multiprocessing for CPU-bound tasks (e.g., heavy computation)

# ─────────────────────────────────────────────────────────────
# 🔷 BASIC MULTITHREADING EXAMPLE USING `threading` MODULE

import threading
import time

# Function to print numbers
def print_numbers():
    for i in range(5):
        print(f"[Thread-1] Number: {i}")
        time.sleep(1)  # Simulate delay



def test(id):
    print('prog start %d' % id)

thread = [threading.Thread(target=test, args=(i,)) for i in range(5)]
for t in thread:
    t.start()
# output:
# prog start 0
# prog start 1
# prog start 2
# prog start 3
# prog start 4

# ✅ FUNCTION-BY-FUNCTION EXPLANATION OF MULTITHREADING CODE

# ─────────────────────────────────────────────────────────────
# 🔷 threading.Thread(target=...)
# ➤ Creates a new thread object.
# ➤ `target` is the function that the thread will execute.
# ➤ You can also pass arguments using `args=(...)`.

# Example:
# t1 = threading.Thread(target=print_numbers)

# ─────────────────────────────────────────────────────────────
# 🔷 start()
# ➤ Starts the thread's execution.
# ➤ Internally calls the `run()` method of the thread.
# ➤ The thread begins executing the target function in parallel.

# Example:
# t1.start()

# ─────────────────────────────────────────────────────────────
# 🔷 join()
# ➤ Waits for the thread to finish before continuing.
# ➤ Ensures that the main program doesn't exit before threads complete.

# Example:
# t1.join()

# ─────────────────────────────────────────────────────────────
# 🔷 time.sleep(seconds)
# ➤ Pauses the current thread for the given number of seconds.
# ➤ Simulates delay (e.g., network latency, file I/O).

# Example:
# time.sleep(1)

# ─────────────────────────────────────────────────────────────
# 🔷 threading.Thread(name="...")
# ➤ Optional parameter to assign a name to the thread.
# ➤ Useful for debugging and logging.

# Example:
# t1_named = threading.Thread(target=print_numbers, name="NumberThread")

# ─────────────────────────────────────────────────────────────
# 🔷 daemon = True
# ➤ Marks a thread as a daemon thread.
# ➤ Daemon threads run in the background and exit when the main thread exits.
# ➤ Use only when thread is non-critical (e.g., logging, monitoring).

# Example:
# t1.daemon = True

# ─────────────────────────────────────────────────────────────
# 🔷 concurrent.futures.ThreadPoolExecutor
# ➤ High-level API for managing a pool of threads.
# ➤ Automatically handles thread creation, execution, and cleanup.
# ➤ More readable and scalable than manually managing threads.

# Example:
# with ThreadPoolExecutor(max_workers=2) as executor:

# ─────────────────────────────────────────────────────────────
# 🔷 executor.submit(function, args)
# ➤ Submits a function to the thread pool for execution.
# ➤ Returns a Future object (can be used to track execution).

# Example:
# executor.submit(task, "Download File 1")

# ─────────────────────────────────────────────────────────────
# 🔷 print()
# ➤ Standard output function.
# ➤ Not thread-safe in complex apps — use `logging` for thread-safe output.

# Example:
# print("✅ Both threads have finished execution.")

# ─────────────────────────────────────────────────────────────
# ✅ SUMMARY OF FUNCTION PURPOSES

# | Function/Method           | Purpose                                      |
# |--------------------------|----------------------------------------------|
# | threading.Thread         | Creates a new thread                         |
# | start()                  | Starts thread execution                      |
# | join()                   | Waits for thread to finish                   |
# | time.sleep()             | Simulates delay                              |
# | name="..."               | Assigns a name to the thread                 |
# | daemon=True              | Marks thread as background (non-blocking)    |
# | ThreadPoolExecutor       | Manages multiple threads efficiently         |
# | submit()                 | Submits task to thread pool                  |
# | print()                  | Displays output (not thread-safe in general) |

# ✅ END OF FUNCTION EXPLANATION

# Function to print letters
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"[Thread-2] Letter: {letter}")
        time.sleep(1)  # Simulate delay

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("✅ Both threads have finished execution.")

# ─────────────────────────────────────────────────────────────
# 🔷 THREAD NAMING AND DAEMON THREADS

# You can name threads for easier debugging
t1_named = threading.Thread(target=print_numbers, name="NumberThread")
t2_named = threading.Thread(target=print_letters, name="LetterThread")

# Daemon threads run in background and exit when main thread exits
# Use daemon=True if you don't want to wait for thread to finish
t1_named.daemon = True
t2_named.daemon = True

# ─────────────────────────────────────────────────────────────
# 🔷 BEST PRACTICES

# ✅ Always use join() to wait for threads to finish
# ✅ Avoid shared mutable data unless using locks
# ✅ Use ThreadPoolExecutor for cleaner thread management (from concurrent.futures)
# ✅ Use logging instead of print for thread-safe output

# ─────────────────────────────────────────────────────────────
# 🔷 THREADPOOL EXAMPLE (MODERN APPROACH)

from concurrent.futures import ThreadPoolExecutor

def task(msg):
    print(f"Task started: {msg}")
    time.sleep(2)
    print(f"Task finished: {msg}")

# Create a thread pool with 2 workers
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task, "Download File 1")
    executor.submit(task, "Download File 2")

print("✅ All tasks submitted to thread pool.")

# ─────────────────────────────────────────────────────────────
# 🔷 SUMMARY FOR REVISION

# ➤ threading.Thread(target=func): Create a thread
# ➤ start(): Begin thread execution
# ➤ join(): Wait for thread to finish
# ➤ daemon=True: Run thread in background
# ➤ ThreadPoolExecutor: Cleaner way to manage multiple threads

# 🔸 Use threading for I/O-bound tasks
# 🔸 Use multiprocessing for CPU-bound tasks
# 🔸 Avoid race conditions using threading.Lock if needed

# ─────────────────────────────────────────────────────────────
