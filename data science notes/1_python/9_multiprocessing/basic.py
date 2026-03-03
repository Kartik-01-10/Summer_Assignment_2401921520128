# ✅ MULTIPROCESSING IN PYTHON — COMPLETE THEORY + CODE (COPY-PASTE FRIENDLY)

# ─────────────────────────────────────────────────────────────
# 🔷 WHAT IS MULTIPROCESSING?
# Multiprocessing allows you to run multiple processes in parallel.
# Each process has its own Python interpreter and memory space.
# Unlike threads, multiprocessing bypasses the Global Interpreter Lock (GIL),
# making it ideal for CPU-bound tasks like data processing, calculations, etc.

# ─────────────────────────────────────────────────────────────
# 🔷 WHY USE MULTIPROCESSING?
# - True parallelism for CPU-bound tasks
# - Each process runs independently
# - Avoids GIL limitations
# - Better performance for heavy computations

# ─────────────────────────────────────────────────────────────
# 🔷 BASIC MULTIPROCESSING EXAMPLE USING `multiprocessing` MODULE

import multiprocessing
import time

# Function to simulate CPU-bound task
def compute_square(numbers):
    for n in numbers:
        print(f"[Process-{multiprocessing.current_process().name}] Square of {n}: {n*n}")
        time.sleep(1)  # Simulate computation delay

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    # Create process
    p1 = multiprocessing.Process(target=compute_square, args=(nums,), name="SquareProcess")

    # Start process
    p1.start()

    # Wait for process to finish
    p1.join()

    print("✅ Multiprocessing task completed.")

# ─────────────────────────────────────────────────────────────
# 🔷 MULTIPLE PROCESSES EXAMPLE

def cube(n):
    print(f"[Process-{multiprocessing.current_process().name}] Cube of {n}: {n**3}")
    time.sleep(1)

if __name__ == "__main__":
    numbers = [2, 4, 6]

    # Create multiple processes
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=cube, args=(num,), name=f"CubeProcess-{num}")
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("✅ All cube processes completed.")

# ─────────────────────────────────────────────────────────────
# 🔷 FUNCTION-BY-FUNCTION EXPLANATION

# ➤ multiprocessing.Process(target=..., args=..., name=...)
#   - Creates a new process object
#   - `target`: function to run
#   - `args`: arguments to pass to the function
#   - `name`: optional name for the process

# ➤ start()
#   - Begins execution of the process

# ➤ join()
#   - Waits for the process to complete before continuing

# ➤ multiprocessing.current_process().name
#   - Returns the name of the currently running process

# ➤ time.sleep()
#   - Simulates delay or computation time

# ─────────────────────────────────────────────────────────────
# 🔷 BEST PRACTICES

# ✅ Always use `if __name__ == "__main__"` to protect code from being run multiple times
# ✅ Use `join()` to wait for processes to complete
# ✅ Avoid sharing mutable data directly — use `Queue`, `Pipe`, or `Manager` for communication
# ✅ Use `Pool` for managing multiple worker processes efficiently

# ─────────────────────────────────────────────────────────────
# 🔷 POOL EXAMPLE (FOR PARALLEL MAP)

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        print("Squares:", results)

# ─────────────────────────────────────────────────────────────
# 🔷 SUMMARY FOR REVISION

# | Function/Method               | Purpose                                      |
# |------------------------------|----------------------------------------------|
# | multiprocessing.Process      | Creates a new process                        |
# | start()                      | Starts process execution                     |
# | join()                       | Waits for process to finish                  |
# | current_process().name       | Gets name of current process                 |
# | Pool                         | Manages multiple worker processes            |
# | map(func, iterable)          | Applies function to iterable in parallel     |
# | Queue / Pipe / Manager       | Used for inter-process communication         |

