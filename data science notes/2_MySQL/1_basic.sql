-- Active: 1754845396214@@127.0.0.1@3306@testdb
create DATABASE test_sc;

-- ✅ SINGLE-LINE COMMENT
-- Use two hyphens (--) to write a single-line comment.
-- Everything after -- on the same line is ignored by SQL engine.

-- ✅ MULTI-LINE COMMENT
/*
-- Use /* ... */ --to write multi-line comments.
-- Useful for longer explanations or temporarily disabling code blocks.
-- */

-- ✅ EXAMPLE: COMMENTING IN SQL
-- This query selects all rows from the 'employees' table
SELECT * FROM employees;

-- This query creates a table named 'test_sc' with 5 columns
CREATE TABLE test_sc (
    c1 INT,           -- Integer column
    c2 VARCHAR(50),   -- String column with max 50 characters
    c3 FLOAT,         -- Floating point number
    c4 INT,           -- Another integer column
    c5 VARCHAR(30)    -- String column with max 30 characters
);

-- ❌ ISSUE: If you run the above CREATE TABLE again, you'll get an error:
-- ERROR: Table 'test_sc' already exists

-- ✅ SOLUTION: Use IF NOT EXISTS to avoid error if table already exists
CREATE TABLE IF NOT EXISTS test_sc (
    c1 INT,
    c2 VARCHAR(50),
    c3 FLOAT,
    c4 INT,
    c5 VARCHAR(30)
);
-- Now, if the table already exists, SQL will skip creation without error.

-- 📘 SQL COMPLETE QUERY GUIDE WITH COMMENTS – COPY-PASTE FRIENDLY

-- 🔷 DDL: Data Definition Language – Table Structure

-- 1. CREATE TABLE – Define a new table with various data types and constraints
CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY,           -- Unique student ID (Primary Key)
    name VARCHAR(50),             -- Student name (max 50 characters)
    marks FLOAT,                  -- Marks scored (floating point)
    grade CHAR(1),                -- Grade (A/B/C etc.)
    dob DATE                      -- Date of birth
);

-- 2. ALTER TABLE – Modify table structure
ALTER TABLE student ADD email VARCHAR(100);         -- Add a new column
ALTER TABLE student MODIFY marks DOUBLE;            -- Change data type of 'marks'
ALTER TABLE student RENAME COLUMN name TO full_name;-- Rename column 'name' to 'full_name'

-- 3. DROP TABLE – Delete the entire table structure and data
DROP TABLE IF EXISTS student;                       -- Safe deletion if table exists

-- 4. TRUNCATE TABLE – Quickly delete all rows but keep structure
TRUNCATE TABLE student;                             -- Faster than DELETE for large tables

-- 🔷 DML: Data Manipulation Language – Insert, Update, Delete

-- 5. INSERT INTO – Add new rows to the table
INSERT INTO student (id, full_name, marks, grade, dob)
VALUES (1, 'Kartik Sharma', 92.5, 'A', '2002-05-14');-- Insert one row

INSERT INTO student (id, full_name, marks, grade, dob)
VALUES 
(2, 'Anjali Verma', 85.0, 'B', '2001-11-22'),       -- Insert multiple rows
(3, 'Ravi Kumar', 78.5, 'C', '2003-03-10');

-- 6. UPDATE – Modify existing data
UPDATE student
SET marks = 95.0, grade = 'A'
WHERE id = 2;                                       -- Update row with id = 2

-- 7. DELETE – Remove rows from the table
DELETE FROM student WHERE id = 3;                   -- Delete row with id = 3
-- DELETE FROM student;                             -- ⚠️ Deletes all rows (use with caution)

-- 🔷 DQL: Data Query Language – Retrieve Data

-- 8. SELECT – Fetch data from the table
SELECT * FROM student;                              -- Select all columns
SELECT id, full_name FROM student;                  -- Select specific columns
SELECT * FROM student WHERE marks > 80;             -- Filter rows with condition
SELECT * FROM student ORDER BY marks DESC;          -- Sort rows by marks descending

-- 9. WHERE, AND, OR, LIKE, IN – Filtering techniques
SELECT * FROM student WHERE grade = 'A' AND marks > 90; -- Multiple conditions
SELECT * FROM student WHERE full_name LIKE 'Kar%';      -- Name starts with 'Kar'

select * from student where full_name like 'k%' and like 
'%a' and not like 'y%'  -- we can use like one by one, not on all togther

SELECT * FROM student WHERE id IN (1, 2);               -- Match multiple values

-- 🔷 Aggregate Functions – Summary Calculations

-- 10. COUNT, SUM, AVG, MIN, MAX – Aggregate operations
SELECT COUNT(*) FROM student;            -- Total number of rows
select full_name,COUNT(full_name) from student where count(full_name)=5;  -- classify acc to length of word 
SELECT COUNT(DISTINCT grade) FROM student;  -- Count distinct grades
                  
SELECT SUM(marks) FROM student;                     -- Total marks
SELECT AVG(marks) FROM student;                     -- Average marks
SELECT MIN(marks), MAX(marks) FROM student;         -- Minimum and maximum marks

select ROUND(AVG(marks),2) from student;            -- Rounding according to 2 decimal place 

-- 11. GROUP BY, HAVING – Grouped summaries
SELECT grade, COUNT(*) FROM student GROUP BY grade; -- Count students per grade
SELECT grade, COUNT(*) FROM student GROUP BY grade HAVING COUNT(*) > 1; -- Filter groups

-- 🔷 Constraints – Rules on Data

-- 12. CREATE TABLE with Constraints
CREATE TABLE IF NOT EXISTS course (
    course_id INT PRIMARY KEY,                      -- Unique course ID
    course_name VARCHAR(100) NOT NULL,              -- Mandatory course name
    duration INT CHECK (duration > 0),              -- Duration must be positive
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES instructor(id) -- Link to instructor table
);

-- 🔷 Joins – Combine Data from Multiple Tables

-- 13. INNER JOIN – Match rows from both tables
SELECT s.id, s.full_name, c.course_name
FROM student s
JOIN enrollment e ON s.id = e.student_id
JOIN course c ON e.course_id = c.course_id;

-- 14. LEFT JOIN – Include all students even if not enrolled
SELECT s.id, s.full_name, c.course_name
FROM student s
LEFT JOIN enrollment e ON s.id = e.student_id
LEFT JOIN course c ON e.course_id = c.course_id;

-- 15. RIGHT JOIN – Include all courses even if no students enrolled
SELECT s.id, s.full_name, c.course_name
FROM student s
RIGHT JOIN enrollment e ON s.id = e.student_id
RIGHT JOIN course c ON e.course_id = c.course_id;

-- 🔷 Views – Virtual Tables

-- 16. CREATE VIEW – Save a query as a virtual table
CREATE VIEW high_scorers AS
SELECT id, full_name, marks FROM student WHERE marks > 90;

-- 17. SELECT FROM VIEW – Use the view like a table
SELECT * FROM high_scorers;

-- 18. DROP VIEW – Remove the view
DROP VIEW IF EXISTS high_scorers;

-- 🔷 Indexes – Speed Up Queries

-- 19. CREATE INDEX – Improve search performance
CREATE INDEX idx_name ON student(full_name);

-- 20. DROP INDEX – Remove index (syntax may vary by SQL dialect)
DROP INDEX idx_name ON student;

-- 🔷 Miscellaneous Queries

-- 21. DISTINCT – Remove duplicates
SELECT DISTINCT grade FROM student;

-- 22. LIMIT – Restrict number of rows returned
SELECT * FROM student LIMIT 5;

-- 23. BETWEEN – Range filtering
SELECT * FROM student WHERE marks BETWEEN 80 AND 95;

-- 24. IS NULL / IS NOT NULL – Check for missing values
SELECT * FROM student WHERE email IS NULL;
SELECT * FROM student WHERE email IS NOT NULL;

-- 📘 ADVANCED SQL QUERIES – COPY-PASTE FRIENDLY WITH COMMENTS

-- 🔷 CONSTRAINTS – More Types

-- 1. UNIQUE – Prevent duplicate values
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,       -- No duplicate usernames
    email VARCHAR(100) NOT NULL
);

-- 2. DEFAULT – Set default value if none provided
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'Pending', -- Default status
    created_at DATE DEFAULT CURRENT_DATE  -- Default to today's date
);

-- 🔷 TRANSACTIONS – COMMIT, ROLLBACK, SAVEPOINT

-- 3. Transaction block (syntax may vary by DBMS)
BEGIN;

UPDATE student SET marks = marks + 5 WHERE grade = 'B'; -- Boost marks
SAVEPOINT before_bonus;

UPDATE student SET marks = marks + 10 WHERE grade = 'A'; -- Extra bonus

ROLLBACK TO SAVEPOINT before_bonus; -- Undo second update only

COMMIT; -- Finalize changes

-- 🔷 SUBQUERIES – Nested Queries

-- 4. Subquery in WHERE
SELECT * FROM student
WHERE marks > (SELECT AVG(marks) FROM student); -- Above average students

-- 5. Subquery in FROM
SELECT avg_table.grade, avg_table.avg_marks
FROM (
    SELECT grade, AVG(marks) AS avg_marks
    FROM student
    GROUP BY grade
) AS avg_table;

-- 🔷 CASE STATEMENT – Conditional Logic

-- 6. Assign remarks based on marks
SELECT id, full_name, marks,
CASE
    WHEN marks >= 90 THEN 'Excellent'
    WHEN marks >= 75 THEN 'Good'
    WHEN marks >= 60 THEN 'Average'
    ELSE 'Needs Improvement'
END AS remarks
FROM student;

-- 🔷 SET OPERATIONS – Combine Results

-- 7. UNION – Combine and remove duplicates
SELECT full_name FROM student
UNION
SELECT instructor_name FROM instructor;

-- 8. UNION ALL – Combine and keep duplicates
SELECT full_name FROM student
UNION ALL
SELECT instructor_name FROM instructor;

-- 9. INTERSECT – Common rows (may not be supported in all DBMS)
SELECT full_name FROM student
INTERSECT
SELECT full_name FROM alumni;

-- 10. EXCEPT – Rows in first but not in second
SELECT full_name FROM student
EXCEPT
SELECT full_name FROM alumni;

-- 🔷 TEMPORARY TABLES – Session-based tables

-- 11. Create temporary table
CREATE TEMPORARY TABLE temp_topper (
    id INT,
    name VARCHAR(50),
    marks FLOAT
);

-- 12. Insert into temporary table
INSERT INTO temp_topper VALUES (1, 'Kartik Sharma', 98.5);

-- 🔷 DATE FUNCTIONS – Manipulate Dates

-- 13. Extract year, month, day
SELECT id, EXTRACT(YEAR FROM dob) AS birth_year FROM student;

-- 14. Add days to a date
SELECT CURRENT_DATE + INTERVAL '7 days' AS next_week;

-- 🔷 STRING FUNCTIONS – Manipulate Text

-- 15. Concatenate 
SELECT CONCAT(full_name, ' - Grade: ', grade) AS summary FROM student;

select concat(marks,'%') from student;

-- 16. Convert to upper/lower case
SELECT UPPER(full_name), LOWER(full_name) FROM student;

-- 17. Substring
SELECT SUBSTRING(full_name FROM 1 FOR 5) AS short_name FROM student;

-- 🔷 WINDOW FUNCTIONS – Row-wise Calculations

-- 18. RANK() OVER – Ranking students by marks
SELECT id, full_name, marks,
RANK() OVER (ORDER BY marks DESC) AS rank_position
FROM student;

-- 19. ROW_NUMBER() OVER – Unique row numbers
SELECT id, full_name,
ROW_NUMBER() OVER (ORDER BY dob) AS birth_order
FROM student;

-- 🔷 EXISTS – Check for existence

-- 20. EXISTS clause
SELECT full_name FROM student
WHERE EXISTS (
    SELECT 1 FROM enrollment WHERE student_id = student.id
);

-- 🔷 COALESCE – Handle NULL values

-- 21. Replace NULL with default
SELECT full_name, COALESCE(email, 'No Email') AS contact_email
FROM student;

-- 🔷 NULLIF – Compare values

-- 22. Return NULL if values match
SELECT NULLIF(marks, 0) FROM student; -- Returns NULL if marks = 0

-- 🔷 CAST / CONVERT – Change data types

-- 23. Convert float to integer
SELECT CAST(marks AS INT) AS rounded_marks FROM student;

-- 🔷 IF EXISTS / IF NOT EXISTS – Safe operations

-- 24. Drop table safely
DROP TABLE IF EXISTS temp_topper;

-- 25. Create only if not exists
CREATE TABLE IF NOT EXISTS backup_student AS
SELECT * FROM student;