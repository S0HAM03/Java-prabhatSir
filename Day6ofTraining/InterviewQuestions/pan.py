# # # import pandas as pd
# # #
# # # s = pd.Series([10, 20, 30, 40])
# # # print(s)
# #
# #
import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)
# #
# #
# #
# #
# # Creating DataFrame (Different Ways)
# # From Dictionary
#
# # pd.DataFrame({"A":[1,2], "B":[3,4]})
# #
# # # From List
# #
# # pd.DataFrame([[1,2],[3,4]], columns=["A","B"])
# # #
# #
# #
# #
# #
# #
# # # Student Marks Analysis (Basic Operations)
# # Operations used:
# #
# # # DataFrame creation
# # #
# # # View data
# # #
# # # Column selection
# # #
# # # Average calculation
# #
# import pandas as pd
#
# data = {
#     "Name": ["Amit", "Neha", "Rahul"],
#     "Marks": [85, 90, 88]
# }
#
# df = pd.DataFrame(data)
# # #
# print(df)    # case 1
# print("Average Marks:", df["Marks"].mean())     #case 2
# #
# # # DataFrame() creates table
# # #
# # # mean() gives average
# #
# # #2)Filtering & Sorting Data
# #
# # # import pandas as pd
# # #
# # # data = {
# # #     "Name": ["Amit", "Neha", "Rahul", "Pooja"],
# # #     "Marks": [85, 90, 70, 95]
# # # }
# # #
# # # df = pd.DataFrame(data)
# # #
# # # # Filter students with marks > 80
# # # high_score = df[df["Marks"] > 80]
# # #
# # # # Sort by marks descending
# # # sorted_df = high_score.sort_values("Marks", ascending=False)
# # #
# # # print(sorted_df)
# #
# # #3 Handling Missing Values (Data Cleaning)
# # # Operations used:
# # #
#
# # # isnull()   #CHECK THE MISSING VALUE
# # isnull() is used to check whether data is missing or not.
# #
# # Missing values are shown as True
# #
# # Available values are shown as False
# #True → value is missing
#
# # False → value is present
#
# # #
# # # fillna()     #fillna() is used to replace missing values (NaN / None) with a value.
# #
# # import pandas as pd
#
# data = {
#     "Name": ["Amit", "Neha", "Rahul"],
#     "Marks": [85, None, 90]
# }
#
# df = pd.DataFrame(data)
#
# # print("Before Cleaning:")
# #     Name  Marks
# # 0   Amit   85.0
# # 1   Neha    NaN
# # 2  Rahul   90.0
#
# # print(df)
# #
# # df["Marks"] = df["Marks"].fillna(0)
# #
# # print("\nAfter Cleaning:")
# # # print(df)
#
# #OUTPUT
# #     Name  Marks
# # 0   Amit   85.0
# # 1   Neha    0
# # 2  Rahul   90.0
#
# #
# # # Real-world data always has missing values
# # #
# # # fillna() avoids errors
# # import pandas as pd
# # # 1️⃣ Create DataFrame
# # data = {
# #     "Name": ["Amit", "Neha", "Rahul", "Pooja", "Karan"],
# #     "Department": ["IT", "IT", "CS", "CS", "IT"],
# #     "Marks": [85, None, 72, 90, None]
# # }
#
# # df = pd.DataFrame(data)
# #
# # print("1. Original Data")
# # print(df)
# #
# # # 2️⃣ Display first rows
# # print("\n2. First 3 Records")
# # print(df.head(3))
# #
# # # 3️⃣ Shape & Data Types   #Shap mins row,coloum foramt
# # print("\n3. Shape:", df.shape)
# # print("\nData Types:")
# # print(df.dtypes)
# #
# # # 4️⃣ Handle Missing Values  #missng value create create issue so avo null value
# # df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# #
# # print("\n4. After Filling Missing Marks")
# # print(df)
# #
# # # 5️⃣ Add Result Column
# # def result(m):
# #     return "Pass" if m >= 75 else "Fail"
# #
# # df["Result"] = df["Marks"].apply(result)
# #
# # print("\n5. Result Column Added")
# # print(df)
# #
# # # 6️⃣ Filter Passed Students
# # passed_students = df[df["Result"] == "Pass"]
# #
# # print("\n6. Passed Students")
# # print(passed_students)
# #
# # # 7️⃣ Sort by Marks (Descending)
# # sorted_df = df.sort_values("Marks", ascending=False)
# #
# # print("\n7. Sorted by Marks")
# # print(sorted_df)
# #
# # # 8️⃣ Average Marks
# # avg_marks = df["Marks"].mean()
# # print("\n8. Average Marks:", avg_marks)
# #
# # # 9️⃣ Group by Department
# # dept_avg = df.groupby("Department")["Marks"].mean()
# #
# # print("\n9. Department Wise Average Marks")
# # print(dept_avg)
# #
# # # 🔟 Save Report to CSV
# # sorted_df.to_csv("student_result_report.csv", index=False)
# #
# # print("\n10. Report saved as student_result_report.csv")
#
#
#
#
#
#
#
# ###########case studay
# import pandas as pd
#
# # ===============================
# # 1. CREATE DATAFRAME
# # ===============================
# data = {
#     "Name": ["Amit", "Neha", "Rahul", "Pooja", "Karan"],
#     "Department": ["IT", "IT", "CS", "CS", "IT"],
#     "Marks": [85, None, 72, 90, None]
# }
#
# df = pd.DataFrame(data)
#
# print("----- ORIGINAL DATA -----")
# print(df)
#
# # ===============================
# # 2. VIEW DATA
# # ===============================
# print("\n----- FIRST RECORDS -----")
# print(df.head())
#
# print("\nShape of Data:", df.shape)
# print("\nData Types:")
# print(df.dtypes)
#
# # ===============================
# # 3. HANDLE MISSING VALUES
# # ===============================
# df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
#
# print("\n----- AFTER FILLING MISSING VALUES -----")
# print(df)
#
# # ===============================
# # 4. ADD RESULT COLUMN
# # ===============================
# def get_result(marks):
#     if marks >= 75:
#         return "Pass"
#     else:
#         return "Fail"
#
# df["Result"] = df["Marks"].apply(get_result)
#
# print("\n----- AFTER ADDING RESULT COLUMN -----")
# print(df)
#
# # ===============================
# # 5. FILTER PASSED STUDENTS
# # ===============================
# passed_students = df[df["Result"] == "Pass"]
#
# print("\n----- PASSED STUDENTS -----")
# print(passed_students)
#
# # ===============================
# # 6. SORT BY MARKS
# # ===============================
# sorted_df = df.sort_values("Marks", ascending=False)
#
# print("\n----- SORTED BY MARKS -----")
# print(sorted_df)
#
# # ===============================
# # 7. AVERAGE MARKS
# # ===============================
# average_marks = df["Marks"].mean()
# print("\nAverage Marks of Class:", average_marks)
#
# # ===============================
# # 8. GROUP BY DEPARTMENT
# # ===============================
# dept_wise_avg = df.groupby("Department")["Marks"].mean()
#
# print("\n----- DEPARTMENT WISE AVERAGE -----")
# print(dept_wise_avg)
#
# # ===============================
# # 9. SAVE FINAL REPORT
# # ===============================
# sorted_df.to_csv("student_result_report.csv", index=False)
#
# print("\nReport saved as 'student_result_report.csv'")
