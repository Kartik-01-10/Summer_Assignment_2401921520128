# ✅ MySQL connection and table setup using mysql-connector-python
# this how we connect to database 

import mysql.connector
from mysql.connector import Error

try:
    # Step 1: Connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='kartik2004',
        database='test_sc'
    )

    if conn.is_connected():
        print("✅ Connection successful!")

        cursor = conn.cursor()

        # Step 2: Create 'student' table if it doesn't exist 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
        """)
        print("✅ Table 'student' is ready.")

        # Step 3: Check if table is empty
        cursor.execute("SELECT COUNT(*) FROM student")
        count = cursor.fetchone()[0]

        if count == 0:
            # Step 4: Insert sample data
            cursor.execute("INSERT INTO student (id, name, age) VALUES (1, 'Kartik', 20)")
            cursor.execute("INSERT INTO student (id, name, age) VALUES (2, 'Aarav', 21)")
            cursor.execute("INSERT INTO student (id, name, age) VALUES (3, 'Riya', 19)")
            conn.commit()
            print("✅ Sample data inserted.")

        # Step 5: Fetch and display data
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()

        print("\n📋 Student Table Data:")
        for row in rows:
            print(row)

except Error as e:
    print(f"❌ Error: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("🔒 Connection closed.")

# ✅ mysql-connector-python: Function & Method Reference

# 1. mysql.connector.connect(...)
# → Establishes connection to MySQL database
# → Returns a connection object
# → Parameters:
#    - host: MySQL server address (e.g., 'localhost')
#    - user: MySQL username (e.g., 'root')
#    - password: Password for the user
#    - database: Name of the database to connect to

# 2. conn.is_connected()
# → Checks if the connection to MySQL is active
# → Returns True if connected, False otherwise

# 3. conn.cursor()
# → Creates a cursor object for executing SQL queries
# → Returns a cursor instance tied to the connection

# 4. cursor.execute(sql_query)
# → Executes a SQL statement (e.g., CREATE, INSERT, SELECT)
# → Accepts a string containing the SQL command

# 5. cursor.fetchone()
# → Fetches the next row of a query result set
# → Returns a single tuple (e.g., (3,) for COUNT(*))

# 6. cursor.fetchall()
# → Fetches all rows from the result of a query
# → Returns a list of tuples, each tuple is a row

# 7. conn.commit()
# → Saves changes made during the session to the database
# → Required after INSERT, UPDATE, DELETE operations

# 8. cursor.close()
# → Closes the cursor object
# → Frees up resources used by the cursor

# 9. conn.close()
# → Closes the database connection
# → Best practice to avoid memory leaks or locked connections

# 10. from mysql.connector import Error
# → Imports the Error class for handling MySQL-related exceptions
# → Used in try-except blocks to catch and print error messages

# ✅ Additional Functions & Methods in mysql-connector-python

# 1. conn.get_server_info()
# → Returns the version of the MySQL server
# → Useful for logging or compatibility checks
# Example:
#     print("MySQL Server version:", conn.get_server_info())

# 2. conn.database
# → Returns the name of the currently connected database
# Example:
#     print("Connected to database:", conn.database)

# 3. cursor.rowcount
# → Returns the number of rows affected by the last executed query
# → Useful after INSERT, UPDATE, DELETE
# Example:
#     cursor.execute("DELETE FROM student WHERE id = 1")
#     print("Rows deleted:", cursor.rowcount)

# 4. cursor.lastrowid
# → Returns the ID of the last inserted row (if auto-increment is used)
# Example:
#     cursor.execute("INSERT INTO student (name, age) VALUES ('Maya', 22)")
#     print("Last inserted ID:", cursor.lastrowid)

# 5. conn.rollback()
# → Reverts changes made during the current transaction
# → Useful in exception handling when commit should be avoided
# Example:
#     try:
#         cursor.execute("INSERT INTO student VALUES (...)")
#         conn.commit()
#     except Error:
#         conn.rollback()

# 6. cursor.description
# → Returns metadata about columns in the result set
# → Each item includes column name, type, etc.
# Example:
#     cursor.execute("SELECT * FROM student")
#     for column in cursor.description:
#         print("Column:", column[0])  # column[0] is the name

# 7. conn.set_charset_collation(charset='utf8mb4')
# → Sets character set and collation for the connection
# → Useful for handling Unicode data
# Example:
#     conn.set_charset_collation(charset='utf8mb4')

# 8. conn.autocommit = True
# → Enables auto-commit mode (no need to call conn.commit())
# → Useful for simple scripts or read-only operations
# Example:
#     conn.autocommit = True
