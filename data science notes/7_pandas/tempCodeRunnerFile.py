# 📊 Create a DataFrame (2D labeled table)
# # pd.DataFrame() creates a table-like structure with rows and columns
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Marks': [85, 92, 78]
# }
# df = pd.DataFrame(data)
# print("\nDataFrame:\n", df)

# # 📥 Read data from a CSV file
# # pd.read_csv() loads data from a CSV file into a DataFrame
# df = pd.read_csv('students.csv')  # Ensure 'students.csv' exists in your folder
# print("\nFirst 5 rows:\n", df.head())  # .head() shows first 5 rows

# # 📈 Get summary statistics
# # .describe() gives count, mean, std, min, max, and quartiles for numeric columns
# print("\nSummary statistics:\n", df.describe())

# # 🔍 Filter rows based on condition
# # df[condition] selects rows where the condition is True
# high_scores = df[df['Marks'] > 80]
# print("\nStudents with Marks > 80:\n", high_scores)

# # 🧹 Handle missing values
# # .dropna() removes rows with any missing values
# # .fillna(value) replaces missing values with the given value
# df_cleaned = df.dropna()
# df_filled = df.fillna(0)
# print("\nData after dropping missing values:\n", df_cleaned)
# print("\nData after filling missing values with 0:\n", df_filled)

# # 🔗 Merge two DataFrames
# # pd.merge() combines DataFrames based on a common column (like SQL JOIN)
# df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
# df2 = pd.DataFrame({'ID': [1, 2], 'Marks': [85, 92]})
# merged_df = pd.merge(df1, df2, on='ID')
# print("\nMerged DataFrame:\n", merged_df)

# # 📅 Convert column to datetime
# # pd.to_datetime() converts string dates to datetime objects
# df['Date'] = pd.to_datetime(df['Date'])  # 'Date' column must exist in CSV
# print("\nDate column type:\n", df['Date'].dtype)

# # 📊 Plotting data (requires matplotlib)
# # .plot() creates a quick plot; kind='bar' makes a bar chart
# import matplotlib.pyplot as plt
# df['Marks'].plot(kind='bar')  # Plot Marks as a bar chart
# plt.title('Student Marks')    # Set chart title
# plt.xlabel('Index')           # Label x-axis
# plt.ylabel('Marks')           # Label y-axis
# plt.show()                    # Display the plot
