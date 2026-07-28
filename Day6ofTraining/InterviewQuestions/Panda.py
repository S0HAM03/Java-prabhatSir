# # . What is Pandas?
# #
# # Pandas is a powerful Python library used for:
# #
# # Data analysis
# # Data cleaning
# # Data manipulation
# #
# # Built on top of NumPy
# #
# #  2. Why Pandas?
# # Handles large datasets easily
# # Works like Excel (tables)
# # Fast and flexible
# # Used in Data Science & Machine Learning
#
#
# # import pandas as pd
#
# # CORE DATA STRUCTURES
# # Series (1D Data)
#
# #Like a single column
#
# # import pandas as pd
# #
# # data = [10, 20, 30, 40]
# #
# # s = pd.Series(data)
# # print(s)
#
# #__________
# # DataFrame (2D Data)
#
# # 👉 Like Excel table
import pandas as pd
data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)


df["Marks"] = df["Marks"].apply(lambda x: x + 10)
print(df)
# #______
# # Reading Data
# # 🔹 From CSV
#
# # df = pd.read_csv("pan.csv")
# # print(df)
#
#
# #____From Excel
# # df = pd.read_excel("data.xlsx")
#
# #___
# # print(df.head())   # first 5 rows
# # print(df.tail())   # last 5 rows
# # print(df.info())   # structure
# # print(df.describe())  # statistics
#
# #______
# # Selecting Data
# # print(df["Name"])        # single column
# # print(df[["Name","Maks"]])  # multiple columns
#
# ##Filtering
# print(df[df["Marks"] > 80])
#
# ##ADD new coloum
# # df["Result"] = ["Pass", "Pass", "Pass"]
# # print(df)
#
# ##Update
# # Updating Data
# df.loc[0, "Marks"] = 95
# print(df)
# #_________
# ###Group by
# #Find the mean salary of Dept wise
# # data = {
# #     "Dept": ["IT", "IT", "HR", "HR"],
# #     "Salary": [50000, 60000, 45000, 40000]
# # }
# #
# # df = pd.DataFrame(data)
#
# # print(df.groupby("Dept")["Salary"].mean())
#
# ##Merge / Join
# # df1 = pd.DataFrame({"ID":[1,2], "Name":["A","B"]})
# # df2 = pd.DataFrame({"ID":[1,2], "Marks":[90,80]})
# #
# # merged = pd.merge(df1, df2, on="ID")
# # print(merged)
#
# #Applay function
# #Add 10 value in marks
# # df["Marks"] = df["Marks"].apply(lambda x: x + 10)
# # print(df)
#
#
#
# ##Basic
# # Create DataFrame with Name & Age
# # Print first 3 rows
# # 🔹 Intermediate
# # Filter students with marks > 70
# # Add Grade column
# # 🔹 Advanced
# # Group data by department
# # Merge two DataFrames
#
#
# #_____INTERVIEW QUESTION
# # 🐼 PANDAS DATAFRAME – COMPLETE INTERVIEW QUESTIONS
#
# # ---
#
# ## 📌 BASIC LEVEL
#
# ### 1. What is a DataFrame?
#
# # A DataFrame is a 2-dimensional labeled data structure with rows and columns, similar to an Excel table.
# #
# # ---
# #
# # ### 2. Difference between Series and DataFrame
# #
# # * Series → 1D data
# # * DataFrame → 2D data
# #
# # ---
# #
# # ### 3. Create a DataFrame
# #
# # ```python
# # import pandas as pd
# # data = {"Name": ["A", "B"], "Marks": [90, 80]}
# # df = pd.DataFrame(data)
# # ```
# #
# # ---
# #
# # ### 4. Read CSV file
# #
# # ```python
# # df = pd.read_csv("file.csv")
# # ```
# #
# # ---
# #
# # ### 5. View top rows
# #
# # ```python
# # df.head()
# # ```
# #
# # ---
# #
# # ### 6. What does df.info() do?
# #
# # * Shows column names
# # * Data types
# # * Null values
# #
# # ---
# #
# # ### 7. Select a column
# #
# # ```python
# # df["Marks"]
# # ```
# #
# # ---
# #
# # ### 8. loc vs iloc
# #
# # * loc → label-based
# # * iloc → index-based
# #
# # ---
# #
# # ## 📌 INTERMEDIATE LEVEL
# #
# # ---
# #
# # ### 9. Filter data
# #
# # ```python
# # df[df["Marks"] > 50]
# # ```
# #
# # ---
# #
# # ### 10. Handle missing values
# #
# # ```python
# # df.fillna(0)
# # df.dropna()
# # ```
# #
# # ---
# #
# # ### 11. Add new column
# #
# # ```python
# # df["Result"] = "Pass"
# # ```
# #
# # ---
# #
# # ### 12. Update value
# #
# # ```python
# # df.loc[0, "Marks"] = 95
# # ```
# #
# # ---
# #
# # ### 13. Delete column
# #
# # ```python
# # df.drop("Marks", axis=1)
# # ```
# #
# # ---
# #
# # ### 14. Sort data
# #
# # ```python
# # df.sort_values("Marks")
# # ```
# #
# # ---
# #
# # ### 15. GroupBy
# #
# # ```python
# # df.groupby("Dept")["Marks"].mean()
# # ```
# #
# # ---
# #
# # ### 16. Apply function
# #
# # ```python
# # df["Marks"].apply(lambda x: x + 5)
# # ```
# #
# # ---
# #
# # ## 📌 ADVANCED LEVEL
# #
# # ---
# #
# # ### 17. Merge vs Concat
# #
# # * merge → SQL join
# # * concat → stacking
# #
# # ---
# #
# # ### 18. Internal working
# #
# # Pandas uses NumPy arrays internally for fast computation.
# #
# # ---
# #
# # ### 19. Indexing
# #
# # Labeling rows and columns for fast access.
# #
# # ---
# #
# # ### 20. Find duplicates
# #
# # ```python
# # df.duplicated()
# # ```
# #
# # ---
# #
# # ### 21. Remove duplicates
# #
# # ```python
# # df.drop_duplicates()
# # ```
# #
# # ---
# #
# # ### 22. Pivot table
# #
# # ```python
# # df.pivot_table(values="Marks", index="Dept", aggfunc="mean")
# # ```
# #
# # ---
# #
# # ### 23. map vs apply
# #
# # * map → Series only
# # * apply → DataFrame
# #
# # ---
# #
# # ### 24. Rename columns
# #
# # ```python
# # df.rename(columns={"Marks": "Score"})
# # ```
# #
# # ---
# #
# # ### 25. Export Data
# #
# # ```python
# # df.to_csv("file.csv")
# # ```
# #
# # ---
# #
# # ## 📌 SCENARIO-BASED QUESTIONS
# #
# # ---
# #
# # ### 26. Failed students (<40)
# #
# # ```python
# # df[df["Marks"] < 40]
# # ```
# #
# # ---
# #
# # ### 27. Find topper
# #
# # ```python
# # df.loc[df["Marks"].idxmax()]
# # ```
# #
# # ---
# #
# # ### 28. Average by department
# #
# # ```python
# # df.groupby("Dept")["Marks"].mean()
# # ```
# #
# # ---
# #
# # ### 29. Count pass/fail
# #
# # ```python
# # df["Result"].value_counts()
# # ```
# #
# # ---
# #
# # ### 30. Fill missing with average
# #
# # ```python
# # df["Marks"].fillna(df["Marks"].mean(), inplace=True)
# # ```
# #
# # ---
# #
# # ## 📌 TRICKY QUESTIONS
# #
# # ---
# #
# # ### Why is Pandas fast?
# #
# # Because it uses optimized C code and NumPy arrays.
# #
# # ---
# #
# # ### Mixed data types?
# #
# # Column becomes object type (slower).
# #
# # ---
# #
# # ### Shallow vs Deep Copy
# #
# # * Shallow → reference
# # * Deep → independent copy
# #
# # ---
# #
# # ## 📌 PRACTICAL INTERVIEW QUESTION
# #
# # "You have 1 lakh student records. How will you process?"
# #
# # Answer:
# #
# # * Use Pandas DataFrame
# # * Handle null using fillna()
# # * Use groupby() for analysis
# #
# # ---
# #
# # ## 📌 IMPORTANT TOPICS TO FOCUS
# #
# # * Filtering
# # * GroupBy
# # * Merge
# #
# # 👉 These are MOST asked in interviews
# #
# # ---
# #
# # # 🚀 END OF FILE
