# Buffered Reading and Writing in Python 

# 1. What is Buffering
# Buffering means temporarily storing data in memory before reading or writing.
# It improves performance by reducing the number of direct disk or I/O operations.

# 2. Why Use BufferedReader and BufferedWriter
# These classes are part of the io module.
# They are used for efficient reading and writing of binary files, especially large ones.

# 3. BufferedReader – Reading Binary Data Efficiently
# BufferedReader reads chunks of data into a buffer, reducing disk access.
from io import BufferedReader

with open('large_file.bin', 'rb') as file:
    reader = BufferedReader(file)
    chunk = reader.read(1024)  # Reads 1024 bytes (1 KB) at a time
    while chunk:
        print(chunk)
        chunk = reader.read(1024)

# second method
with open("file_name","rb") as f:
    file =BufferedReader(f)
    data= file.read(1024)
    print(data)


# if we don't want to give size size 
with open("file_name","rb") as f:
    file =BufferedReader(f)
    data= file.read()
    print(data)


# 4. BufferedWriter – Writing Binary Data Efficiently
# BufferedWriter stores data in a buffer before writing to disk.
from io import BufferedWriter

with open('output.bin', 'wb') as file:
    writer = BufferedWriter(file)
    writer.write(b'First block of data/n') # here /n is newline char 
    writer.write(b'Second block of data')
    writer.flush()  # Forces writing buffered data to disk  # it is same, as we are using close func in last of program.

# 5. flush Method
# flush writes all buffered data to the file immediately.
# It is important when you want to ensure data is saved without closing the file.

# 6. buffer Size
# You can specify buffer size manually.
# Larger buffer size means fewer disk operations but more memory usage.
from io import BufferedReader

with open('file.bin', 'rb') as file:
    reader = BufferedReader(file, buffer_size=4096)  # 4 KB buffer

# 7. Combining BufferedReader with TextIOWrapper
# If you want to read text from a binary file efficiently:
from io import BufferedReader, TextIOWrapper

with open('textfile.txt', 'rb') as file:
    buffered = BufferedReader(file)
    text_reader = TextIOWrapper(buffered)
    line = text_reader.readline()
    print(line)

# 8. When to Use BufferedReader and BufferedWriter
# Use them when working with large files or when performance is critical.
# They are especially useful for binary formats like images, audio, video, and logs.

# 9. Alternative – open with buffering parameter
# Python's open function also supports buffering directly.
# Example:
with open('file.bin', 'rb', buffering=8192) as file:  # 8 KB buffer
    data = file.read()

# 10. Summary
# BufferedReader and BufferedWriter improve performance by reducing I/O operations.
# They are part of the io module and are ideal for handling large binary files.



# 11. BufferedIOBase Class
# BufferedReader and BufferedWriter are subclasses of BufferedIOBase.
# BufferedIOBase provides the base interface for buffered binary streams.

# 12. RawIOBase vs BufferedIOBase
# RawIOBase handles low-level byte I O without buffering.
# BufferedIOBase adds buffering on top of raw I O for better performance.

# 13. Using BufferedRandom
# BufferedRandom allows both reading and writing in binary mode with buffering.
from io import BufferedRandom

with open('file.bin', 'r+b') as file:
    buffered = BufferedRandom(file)
    buffered.write(b'abc')
    buffered.seek(0)
    print(buffered.read(3))

# 14. BufferedReader peek Method
# peek allows you to look ahead at the next bytes without advancing the read position.
from io import BufferedReader

with open('file.bin', 'rb') as file:
    reader = BufferedReader(file)
    preview = reader.peek(5)
    print(preview)

# 15. BufferedReader readinto Method
# readinto reads bytes directly into a pre-allocated bytearray.
buffer = bytearray(10)
with open('file.bin', 'rb') as file:
    reader = BufferedReader(file)
    reader.readinto(buffer)
    print(buffer)

# 16. BufferedWriter detach Method
# detach removes the underlying raw stream from the buffered wrapper.
from io import BufferedWriter

with open('output.bin', 'wb') as file:
    writer = BufferedWriter(file)
    raw = writer.detach()  # Now raw is the original file object

# 17. BufferedReader tell and seek
# tell returns the current position in the stream.
# seek moves the read or write pointer to a specific position.
with open('file.bin', 'rb') as file:
    reader = BufferedReader(file)
    reader.seek(5)
    print(reader.tell())

# 18. BufferedReader readline Method
# readline reads a single line from a binary file.
with open('textfile.txt', 'rb') as file:
    reader = BufferedReader(file)
    line = reader.readline()
    print(line)

# 19. BufferedWriter truncate Method
# truncate resizes the file to a given size.
with open('output.bin', 'wb') as file:
    writer = BufferedWriter(file)
    writer.write(b'1234567890')
    writer.flush()
    writer.truncate(5)  # File now contains only first 5 bytes

# 20. Performance Considerations
# Buffered I O is faster than unbuffered I O for large files.
# Use appropriate buffer sizes based on file size and memory availability.
# Avoid very small buffer sizes as they increase disk access.