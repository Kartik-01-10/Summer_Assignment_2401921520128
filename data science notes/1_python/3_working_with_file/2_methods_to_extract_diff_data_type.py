
###### JSON  ############


# 1. JSON stands for JavaScript Object Notation.

# 2. It is a lightweight data format used for storing and exchanging data.

# 3. JSON is easy to read and write for humans, and easy to parse for machines.

# 4. JSON data is written as key-value pairs.(in created file)

# 5. Example of JSON data:
{
    "name": "Kartik",
    "age": 20,
    "skills": ["C++", "Python", "JavaScript"],
    "isStudent": True
}

# 6. JSON supports:
#    - Strings: "text"
#    - Numbers: 123, 45.6
#    - Booleans: true, false
#    - Null: null
#    - Arrays: [1, 2, 3]
#    - Objects: {"key": "value"}

# 7. In Python, you can work with JSON using the json module.

# 8. Example: Reading JSON from a file
import json   #    - This imports the built-in JSON module in Python. bcz first we have to import it

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

# 9. Example: Writing JSON to a file
import json

data = {
    "name": "Kartik",
    "age": 20
}

with open('data.json', 'w') as file:
    json.dump(data, file)

# 10. Common functions:
#     - json.load(): read JSON from a file
#     - json.loads(): read JSON from a string
#     - json.dump(): write JSON to a file
#     - json.dumps(): convert Python object to JSON string


### example of all function

import json

# json.load(file)
#    - Reads JSON data from a file object and converts it into a Python object.
#    - Used when reading JSON from a file.

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# json.loads(string)
#    - Reads JSON data from a string and converts it into a Python object.
#    - Useful when you have JSON data as a string (e.g., from an API).

json_string = '{"name": "Kartik", "age": 20}'
data = json.loads(json_string)
print(data)

# json.dump(obj, file)
#    - Writes a Python object to a file as JSON.
#    - Used when saving data to a file.

data = {"name": "Kartik", "age": 20}
with open('data.json', 'w') as f:
    json.dump(data, f)

# json.dumps(obj)
#    - Converts a Python object into a JSON string.
#    - Useful for printing or sending JSON over a network.

data = {"name": "Kartik", "age": 20}
json_string = json.dumps(data)
print(json_string)

# Optional Parameters for dump() and dumps():
#    - indent: adds indentation for readability
#    - sort_keys: sorts keys alphabetically
#    - separators: custom separators for items

# Example with formatting:
data = {"name": "Kartik", "age": 20, "skills": ["C++", "Python"]}
json_string = json.dumps(data, indent=4, sort_keys=True)
print(json_string)

# json.JSONDecodeError
#    - Raised when JSON decoding fails (e.g., invalid JSON format)

try:
    bad_json = '{"name": "Kartik", "age": 20'  # Missing closing brace
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)



# -----------------------------------------------------------# -------------
# -----------------------------------------------------------

# 1. CSV stands for Comma-Separated Values.

# 2. It is a simple file format used to store tabular data (like spreadsheets or databases).

# 3. Each line in a CSV file represents a row of data.

# 4. Values in each row are separated by commas.

# 5. CSV files are plain text files with a .csv extension.

# 6. Example of CSV content:
#    Name,Age,City
#    Kartik,20,Meerut
#    Amit,22,Delhi

# 7. CSV is widely used for:
#    - Data exchange between applications
#    - Importing/exporting data from spreadsheets
#    - Storing simple structured data

# 8. In Python, the csv module is used to read and write CSV files.

# 9. Common functions in csv module:
#    - csv.reader(): reads rows as lists
#    - csv.writer(): writes rows as lists
#    - csv.DictReader(): reads rows as dictionaries
#    - csv.DictWriter(): writes rows as dictionaries

# 10. CSV files are easy to create, edit, and process using any text editor or spreadsheet software.

import csv

#  Reading CSV using csv.reader()
#    - Reads data from a CSV file line by line.
#    - Returns each row as a list of values.

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#  Writing CSV using csv.writer()
#    - Writes data to a CSV file.
#    - Each row should be a list of values.

data = [
    ['Name', 'Age', 'City'],
    ['Kartik', '20', 'Meerut'],
    ['Amit', '22', 'Delhi']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

#  writer.writerow(row)
#    - Writes a single row to the CSV file.

with open('single_row.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])

#  writer.writerows(rows)
#    - Writes multiple rows to the CSV file.

rows = [
    ['Kartik', '20', 'Meerut'],
    ['Amit', '22', 'Delhi']
]

with open('multi_rows.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

#  Reading CSV as dictionary using csv.DictReader()
#    - Reads each row as a dictionary using the header row as keys.

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])

# /. Writing CSV as dictionary using csv.DictWriter()
#    - Writes rows using dictionaries.
#    - You must specify fieldnames (column headers).

fieldnames = ['Name', 'Age', 'City']
data = [
    {'Name': 'Kartik', 'Age': '20', 'City': 'Meerut'},
    {'Name': 'Amit', 'Age': '22', 'City': 'Delhi'}
]

with open('dict_output.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


# 11. CSV files can use other delimiters like semicolon (;) or tab (\t), but comma is most common.

# 12. If a field contains a comma, it should be enclosed in double quotes.
#     Example: "Kartik, Jr.",20,Meerut

# 13. CSV files may or may not have a header row.
#     - Header row contains column names.
#     - DictReader and DictWriter require headers.

# 14. newline='' is used when opening CSV files in Python to avoid blank lines between rows (especially on Windows).

# 15. You can customize delimiter, quote character, and line terminator using parameters in csv.reader() and csv.writer().
#     Example:
#     csv.reader(file, delimiter=';', quotechar='"')

# 16. CSV is not ideal for storing hierarchical or nested data — use JSON or XML for that.

# 17. CSV files are not type-aware:
#     - All values are stored as strings.
#     - You need to convert them manually (e.g., int(), float()).

# 18. CSV is widely supported by tools like Excel, Google Sheets, databases, and programming languages.

# 19. Python pandas library provides powerful tools for reading, writing, and analyzing CSV files.

# 20. CSV is best for simple, flat data structures — easy to read, write, and share.



# -----------------------------------------------------------# -------------
# -----------------------------------------------------------

# Binary Data Extraction in Python 

# 1. What is Binary Data
# Binary data refers to non-text data stored as bytes.
# Examples include images, audio, video, and executable files.
# It is not human-readable and must be handled using byte-level operations.

# 2. Opening a Binary File
# Use 'rb' mode to read binary files and 'wb' mode to write binary files.
with open('file.bin', 'rb') as file:
    data = file.read()  # Reads entire file as bytes

# 3. Reading Specific Number of Bytes
with open('file.bin', 'rb') as file:
    chunk = file.read(10)  # Reads first 10 bytes

# 4. Reading Byte-by-Byte in a Loop
with open('file.bin', 'rb') as file:
    while True:
        byte = file.read(1)
        if not byte:
            break
        print(byte)

# 5. Writing Binary Data to a File
binary_data = b'Hello'
with open('output.bin', 'wb') as file:
    file.write(binary_data)

# 6. Using struct Module for Binary Parsing
# struct helps unpack binary data into Python types
import struct
with open('data.bin', 'rb') as file:
    content = file.read(4)
    number = struct.unpack('i', content)[0]  # 'i' means 4-byte integer
    print(number)

# 7. Common struct Format Codes
# 'i' = integer (4 bytes)
# 'f' = float (4 bytes)
# 'd' = double (8 bytes)
# 's' = string
# Example:
# struct.unpack('2i', file.read(8))  # Reads two integers

# 8. Converting Bytes to String
byte_data = b'Hello'
text = byte_data.decode('utf-8')

# 9. Converting String to Bytes
text = 'Hello'
byte_data = text.encode('utf-8')

# 10. Copying Binary Files
with open('image.jpg', 'rb') as source:
    img_data = source.read()
with open('copy.jpg', 'wb') as target:
    target.write(img_data)

# 11. Binary vs Text Mode
# Text mode reads strings and auto-decodes.
# Binary mode reads raw bytes without decoding.
# Use 'rb' and 'wb' for binary files.

# 12. Handling Binary Streams
# Binary streams from hardware or networks can be parsed using byte buffers and the struct module.

# 13. Safety Tips
# Always use binary mode for binary files.
# Avoid decoding unless you know the encoding format.
# Use try-except blocks to handle decoding errors.

# 14. Real-World Use Cases
# Reading sensor logs from embedded systems
# Parsing binary protocols like TCP or IP
# Handling multimedia files such as images and audio
# Working with compiled formats like .exe or .bin



# 15. Reading Binary Data with MemoryView
# memoryview allows efficient slicing and manipulation of binary data without copying
data = b'abcdef'
view = memoryview(data)
print(view[1:4])  # Outputs b'bcd'

# 16. Reading Binary Data with NumPy (for scientific data)
# Useful for binary files containing arrays or matrices
# import numpy as np
# array = np.fromfile('data.bin', dtype=np.int32)
# print(array)

# 17. Reading Binary Data with bytearray
# bytearray is mutable, unlike bytes
with open('file.bin', 'rb') as file:
    raw = bytearray(file.read())
raw[0] = 65  # Modify first byte

# 18. Detecting File Type from Binary Signature
# Many binary files start with a magic number or signature
# Example: JPEG files start with bytes FF D8
with open('image.jpg', 'rb') as file:
    signature = file.read(2)
    if signature == b'\xFF\xD8':
        print('JPEG file detected')

# 19. Reading Binary Data with BufferedReader
# For large files, use buffering for performance
from io import BufferedReader
with open('large.bin', 'rb') as file:
    reader = BufferedReader(file)
    chunk = reader.read(1024)  # Read 1 KB at a time

# 20. Writing Structured Binary Data with struct
# Pack multiple values into binary format
import struct
data = struct.pack('i4s', 123, b'test')  # Integer and 4-byte string
with open('packed.bin', 'wb') as file:
    file.write(data)

# 21. Reading Binary Data from Network Socket
# Binary data is often received over sockets
import socket
sock = socket.socket()
sock.connect(('example.com', 80))
sock.send(b'GET / HTTP/1.0\r\n\r\n')
response = sock.recv(1024)  # Binary response

# 22. Binary File Compression
# Use gzip or zipfile to compress binary data
import gzip
with gzip.open('compressed.gz', 'wb') as file:
    file.write(b'Some binary content')

# 23. Binary File Encryption
# Use libraries like cryptography or PyCrypto to encrypt binary files
# Example with Fernet encryption:
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# cipher = Fernet(key)
# encrypted = cipher.encrypt(b'Secret binary data')
# decrypted = cipher.decrypt(encrypted)

# 24. Binary File Parsing Libraries
# Use third-party libraries for complex formats like PDF, MP3, PNG
# Examples: PyPDF2, Pillow, wave, struct, binascii

# 25. Binary Debugging Tools
# Use hex editors like HxD or online tools to inspect binary files
# Python's binascii module can convert binary to hex
import binascii
with open('file.bin', 'rb') as file:
    hex_data = binascii.hexlify(file.read())
    print(hex_data)