# ---------------------------------------------------
# 📌 Why We Use Pandas in Python (Basic Explanation) : in this we have all lib used for read 
# ---------------------------------------------------

# ✅ Pandas is used to work with structured data easily, i.e working with data sets
# It helps us load, clean, analyze, and manipulate data
# in rows and columns format (like Excel or SQL tables).
# allows us to analyze big data and conclusion based on statistical operations
# ✅ It provides two main data structures:
# - Series: for 1D data (like a single column)
# - DataFrame: for 2D data (like a full table)

# ✅ Pandas makes data handling simple and fast:
# - Read data from files (CSV, Excel, SQL, etc.)
# - Filter and sort rows
# - Handle missing values
# - Group and summarize data
# - Merge and join tables

# ✅ In short:
# Pandas is the go-to tool for data analysis and
# preparation in Python. It's easy to use and saves time.

# 📦 Import the pandas library
import pandas as pd

# 🧮 Create a Series (1D labeled array)
# pd.Series() creates a one-dimensional array with labels (index)
data = [10, 20, 30, 40]
series = pd.Series(data)
print("Series:\n", series)
# Output:
# Series:
# 0    10
# 1    20
# 2    30
# 3    40  i.e index on left side and values on right side
print(series[2])  # Access element at index 2 (outputs 30  )
print(series.index)  # Outputs the index range (0 to 3)
print(series.values)  # Outputs the values as an array [10 20 30 40]
print(series.dtype)  # Outputs the data type of the series (int64)
print(series.size)  # Outputs the number of elements (4)
print(series.ndim)  # Outputs the number of dimensions (1)
print(series.head(2))  # Outputs the first 2 elements
print(series.tail(2))  # Outputs the last 2 elements
print(series.describe())  # Outputs summary statistics
# Outputs:
# count     4.000000
# mean     25.000000
# std      12.909944    
# min      10.000000
# 25%      17.500000
# 50%      25.000000
# 75%      32.500000
# max      40.000000
# dtype: float64

# we can also change the index or labelling of series
labels = ['a', 'b', 'c', 'd']
series = pd.Series(data, index=labels)
print("Series with custom index:\n", series)
# Output:
# Series with custom index: 
# a    10
# b    20
# c    30
# d    40
series = pd.Series(series, index=['b', 'c', 'd', 'e']) # here 'e' will be NaN as it is not present in original series
print("Reindexed Series:\n", series)
# Output:
# Reindexed Series:
# b    20.0
# c    30.0 
# d    40.0
# e     NaN
# NaN means Not a Number, used for missing values

cal = {"day1":300, "day2":400, "day3":250, "day4":500}
se = pd.Series(cal)
print(se)
# Output:
# day1    300
# day2    400
# day3    250
# day4    500
# dtype: int64
# if we only want s=day1 and day3
se = pd.Series(cal, index=["day1", "day3"])
print(se)
# Output:
# day1    300
# day3    250
# dtype: int64



# 📊 Create a DataFrame (2D labeled table)
# pd.DataFrame() creates a table-like structure with rows and columns
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 92, 78]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
# Output:
# DataFrame:
#       Name  Marks
# 0    Alice     85
# 1      Bob     92
# 2  Charlie     78

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]  }
df = pd.DataFrame(data)
print(df)
# Output:
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45
print(df.index)  # Outputs the index range (0 to 2)
print(df.columns)  # Outputs the column names (Index(['calories', 'duration'], dtype='object'))
print(df.values)  # Outputs the values as a 2D array
print(df.dtypes)  # Outputs the data types of each column
print(df.shape)  # Outputs the shape of the DataFrame (rows, columns) (
# Output: (3, 2) )
# print(df.size)  # Outputs the total number of elements (6)
print(df.ndim)  # Outputs the number of dimensions (2)
print(df.head(2))  # Outputs the first 2 rows   

# locate row by index label using loc[]
print(df.loc[1])  # Outputs the row at index 1
# outputs:
# calories    380
# duration     40
# Name: 1, dtype: int64

# we can also change index labels of dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 92, 78]
}
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print("\nDataFrame with custom index:\n", df)
# Output:
#       Name  Marks
# A    Alice     85
# B      Bob     92
# C  Charlie     78




# 📥 Read data from a CSV file
# pd.read_csv() loads data from a CSV file into a DataFrame
df = pd.read_csv('students.csv')  # Ensure 'students.csv' exists in your folder
print("\nFirst 5 rows:\n", df.head())  # .head() shows first 5 rows. ie index from 0 to 4 and by default it shows 5 rows
# to access all data we have to use to_string method
print("\nAll data:\n", df.to_string())  # .to_string() prints the entire DataFrame
print(df) # by default it shows first 5 and last 5 rows only
print(df.info())  # .info() gives summary of DataFrame (data types, non-null counts)
# outputs:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 4 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   Name     100 non-null    object
#  1   Age      100 non-null    int64
#  2   Marks    100 non-null    float64
#  3   Subject  100 non-null    object
# dtypes: float64(1), int64(1), object(2)
# memory usage: 3.2+ KB


# max_rows parameter is used to set the maximum number of rows to display of system
print(pd.options.display.max_rows) # default is 60


# read data from JSON file
df = pd.read_json('data.json')  # Ensure 'data.json' exists in your folder
print("\nData from JSON:\n", df.head())
print(df.to_string())  # Print entire DataFrame from JSON


# cleaning data : it means fixing the bad data or removing the bad data so that it can be used for analysis
# bad data includes missing values, duplicate data, inconsistent formatting, etc.
# empty cells : it will give you wrong result always so to return new data frame with no empty cells we use dropna() method
data = pd.read_csv('students_with_missing.csv')  # CSV with missing values
new_data = data.dropna()  # Drops rows with any missing values
print("\nData after dropping missing values:\n", new_data.to_string())
# if at any case you want to change the original data frame then use inplace=True parameter
# or we can also fill the missing values with some value using fillna() method

data = pd.read_csv('students_with_missing.csv')  # CSV with missing values
data.dropna(inplace=True)  # Drops rows with any missing values in original DataFrame
print("\nData after dropping missing values (inplace):\n", data.to_string())

data = pd.read_csv('students_with_missing.csv')  # CSV with missing values
filled_data = data.fillna(0)  # Fill missing values with 0
# aur data.fillna(130, inplace=True)  # Fill missing values with 130 in original DataFrame
print("\nData after filling missing values with 0:\n", filled_data.to_string())

# we also replace at specific columns
data = pd.read_csv('students_with_missing.csv')  # CSV with missing values
filled_data = data.fillna({'Marks': 0})  # Fill missing Marks with 0
print("\nData after filling missing Marks:\n", filled_data.to_string()) 


data = pd.read_csv('students_with_missing.csv')  # CSV with missing values
filled_data = data.fillna({'Marks': 0, 'Age': data['Age'].mean()})  # Fill missing Marks with 0 and Age with mean age
print("\nData after filling missing values:\n", filled_data.to_string())
# here mean() function calculates the average of the Age column and fills missing Age values with that average
# similarly we can use median() or mode() functions as per requirement

# data in wrong format : to fix this we have 2 ways 




# 📈 Get summary statistics
# .describe() gives count, mean, std, min, max, and quartiles for numeric columns
print("\nSummary statistics:\n", df.describe())

# 🔍 Filter rows based on condition
# df[condition] selects rows where the condition is True
high_scores = df[df['Marks'] > 80]
print("\nStudents with Marks > 80:\n", high_scores)

# 🧹 Handle missing values
# .dropna() removes rows with any missing values
# .fillna(value) replaces missing values with the given value
df_cleaned = df.dropna()
df_filled = df.fillna(0)
print("\nData after dropping missing values:\n", df_cleaned)
print("\nData after filling missing values with 0:\n", df_filled)

# 🔗 Merge two DataFrames
# pd.merge() combines DataFrames based on a common column (like SQL JOIN)
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Marks': [85, 92]})
merged_df = pd.merge(df1, df2, on='ID')
print("\nMerged DataFrame:\n", merged_df)

# 📅 Convert column to datetime
# pd.to_datetime() converts string dates to datetime objects
df['Date'] = pd.to_datetime(df['Date'])  # 'Date' column must exist in CSV
print("\nDate column type:\n", df['Date'].dtype)

# 📊 Plotting data (requires matplotlib)
# .plot() creates a quick plot; kind='bar' makes a bar chart
import matplotlib.pyplot as plt
df['Marks'].plot(kind='bar')  # Plot Marks as a bar chart
plt.title('Student Marks')    # Set chart title
plt.xlabel('Index')           # Label x-axis
plt.ylabel('Marks')           # Label y-axis
plt.show()                    # Display the plot

# ---------------------------------------------------------------
# 📘 Pandas Function Summary Table (Function | Purpose | Example)
# ---------------------------------------------------------------

# ✅ Data Loading & Saving
# # Function                  | Purpose                          | Example
# pd.read_csv()              | Load CSV file                    | pd.read_csv('data.csv')
# df.to_csv()                | Save DataFrame to CSV            | df.to_csv('output.csv')
# pd.read_excel()            | Load Excel file                  | pd.read_excel('data.xlsx')
# df.to_excel()              | Save DataFrame to Excel          | df.to_excel('output.xlsx')

# # ✅ Data Inspection
# df.head()                  | First 5 rows                     | df.head()
# df.head(3)                 | first 3 rows and give naming to  | df.head(3)
#                               rows starting with 0
# df.tail()                  | Last 5 rows                      | df.tail()
# df.shape                   | Rows and columns count           | df.shape
# df.info()                  | Data types & memory usage        | df.info()
# df.describe()              | Summary statistics               | df.describe()

# # ✅ Data Selection
# df['col']                  | Select single column             | df['name']
# df[['col1', 'col2']]       | Select multiple columns          | df[['name', 'age']]
# df.loc[]                   | Select by label/index            | df.loc[0]
# df.iloc[]                  | Select by position               | df.iloc[0]

# # ✅ Filtering & Conditions
# df[cond]                   | Filter rows                      | df[df['age'] > 18]
# df[(cond1) & (cond2)]      | Multiple conditions              | df[(df['age'] > 18) & (df['marks'] > 80)]

# # ✅ Data Cleaning
# df.isnull().sum()          | Count missing values             | df.isnull().sum()
# df.dropna()                | Drop missing rows                | df.dropna()
# df.fillna(val)             | Fill missing values              | df.fillna(0)
# df.duplicated()            | Check for duplicates             | df.duplicated()
# df.drop_duplicates()       | Remove duplicates                | df.drop_duplicates()

# # ✅ Data Transformation
# df.rename()                | Rename columns                   | df.rename(columns={'old':'new'})
# df.sort_values()           | Sort by column                   | df.sort_values('marks')
# df.apply()                 | Apply function to column         | df['marks'].apply(lambda x: x+5)

# # ✅ Grouping & Aggregation
# df.groupby().mean()        | Group and average                | df.groupby('class')['marks'].mean()
# df.groupby().agg()         | Multiple aggregations            | df.groupby('class').agg({'marks':'max', 'age':'mean'})

# # ✅ Merging & Joining
# pd.concat()                | Combine vertically               | pd.concat([df1, df2])
# pd.merge()                 | Merge on common column           | pd.merge(df1, df2, on='id')

# # ✅ Indexing & Resetting
# df.set_index()             | Set column as index              | df.set_index('id')
# df.reset_index()           | Reset to default index           | df.reset_index()

# ------------------------------------------------------------------
# 📘 Extended Pandas Function Summary Table (Function | Purpose | Example)
# ------------------------------------------------------------------

# # ✅ Column Operations
# df['new'] = df['old'] * 2         # Create new column from existing
# df.drop('col', axis=1)            # Drop column
# df.insert(1, 'new', value)        # Insert column at position

# # ✅ Row Operations
# df.append(row, ignore_index=True) # Append row (deprecated, use pd.concat)
# df.drop(index)                    # Drop row by index
# df.loc[len(df)] = [val1, val2]    # Add new row manually

# # ✅ Value Counts & Unique
# df['col'].value_counts()          # Frequency of unique values
# df['col'].unique()                # List of unique values
# df['col'].nunique()               # Count of unique values

# # ✅ Replace & Map
# df['col'].replace({'A':'X'})      # Replace values
# df['col'].map({'A':'X', 'B':'Y'}) # Map values using dict

# # ✅ String Operations
# df['col'].str.lower()             # Convert to lowercase
# df['col'].str.contains('abc')     # Check substring
# df['col'].str.strip()             # Remove whitespace

# # ✅ Date & Time Handling
# pd.to_datetime(df['date'])        # Convert to datetime
# df['date'].dt.year                # Extract year
# df['date'].dt.month               # Extract month
# df['date'].dt.day                 # Extract day

# # ✅ Reshaping Data
# df.pivot(index, columns, values)  # Pivot table
# df.melt(id_vars, value_vars)      # Unpivot (wide to long)
# df.stack()                        # Stack columns into rows
# df.unstack()                      # Unstack rows into columns

# # ✅ Categorical Data
# df['col'] = df['col'].astype('category')  # Convert to category
# df['col'].cat.codes                       # Get category codes
# df['col'].cat.categories                  # List categories

# # ✅ Rolling & Window Functions
# df['col'].rolling(3).mean()       # Moving average (window=3)
# df['col'].expanding().sum()       # Cumulative sum

# # ✅ Sampling & Shuffling
# df.sample(n=5)                    # Random sample of rows
# df.sample(frac=0.1)               # Sample 10% of data
# df.sample(frac=1).reset_index(drop=True)  # Shuffle rows

# # ✅ Query Method
# df.query('age > 18 & marks > 80') # Filter using query string

# # ✅ Memory Optimization
# df.astype('float32')              # Convert data type to save memory
# df.memory_usage(deep=True)        # Memory usage per column
