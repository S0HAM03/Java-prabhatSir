# # # What is NumPy?
# # #
# # # NumPy (Numerical Python) is a powerful Python library used for:
# # #
# # # Fast numerical computations
# # # Working with arrays & matrices
# # # Scientific computing & Data Science
# # # 🔹 Why NumPy?
# # # Faster than Python lists (optimized in C)
# # # Uses less memory
# # # Supports vectorized operations
# #
# # # pip install numpy
# #
# #
# #
# #
# # # 1D Array
# #
import numpy as np
# # #
# # arr = np.array([1, 2, 3, 4])
# # print(arr)
# # print(type(arr))
# #
# # # 2D Array
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)
# #
# # #_________
# # # 5. Array Properties
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
# # #
print(arr.shape)   # rows, columns
print(arr.ndim)    # number of dimensions
print(arr.size)    # total elements
print(arr.dtype)
# #
# # #________
# # # Indexing & Slicing
arr = np.array([10, 20, 30, 40])

print(arr[0])       # first element
print(arr[1:3])
# #
# # #__
# # # 2D Indexing
arr2 = np.array([[1,2,3],[4,5,6]])

print(arr2[0,1])    # row 0, col 1
print(arr2[:,1])    # all rows, column 1
# #
# # #_________
# # # Array Operations
# # # 🔹 Arithmetic
# #
# # # a = np.array([1,2,3])
# # # b = np.array([4,5,6])
# # #
# # # print(a + b)
# # # print(a * b)
# # # print(a - b)
# #
# # #___Mathematical Functions
# # # arr = np.array([1, 4, 9])
# # #
# # # print(np.sqrt(arr))
# # # print(np.mean(arr))
# # # print(np.sum(arr))
# # # print(np.max(arr))
# # # print(np.min(arr))
# #
# #
# # #_________
# # # Flattening Array
arr = np.array([[1,2],[3,4]])

print(arr.flatten())
# #
# # import numpy as np
# #
# # #
# A = [[2,3,4,5],
#      [5,4,5,78],
#      [7,45,6,0]]   # add dummy value
# 
# r = np.array(A)
# print(r.flatten())
# #
# #
# #
# # # import numpy as np
# #
# # # A = [[2,3,4,5],[5,4,5,78,6],[7,45,6]]
# # #
# # # r = np.concatenate(A)
# # # print(r)
# #
# # ##np.concatenate(A)
# #
# # #  This is the main logic
# # #
# # # What it does:
# # # It joins multiple arrays/lists into one single array
# #
# #
# # ##_____Mini Project: Student Marks Analysis (NumPy)
# # # 📌 Problem Statement
# # # Take student marks as input (array)
# # # Calculate:
# # # ✅ Average marks
# # # ✅ Highest marks
# # # ✅ Failed students (marks < 40)
# #
# # # import numpy as np
# #
# # # Step 1: Input marks
# marks = np.array([35, 67, 89, 23, 90, 45, 56, 38])
# # #
# # # print("Student Marks:", marks)
# # #
# # # # Step 2: Average Marks
# # # average = np.mean(marks)
# # # print("Average Marks:", average)
# # #
# # # # Step 3: Highest Marks
# # # highest = np.max(marks)
# # # print("Highest Marks:", highest)
# # #
# # # # Step 4: Failed Students (marks < 40)
# failed_students = marks[marks < 40]
# # # print("Failed Students Marks:", failed_students)
# # #
# # # # Step 5: Count of Failed Students
# print("Number of Failed Students:", len(failed_students))
# #


# from sklearn.linear_model import LinearRegression
# import numpy as np
#
# # Data
# X = np.array([20, 25, 30]).reshape(-1, 1)
# Y = np.array([100, 150, 200])
#
# # Model
# model = LinearRegression()
# model.fit(X, Y)
#
# # Prediction
# print(model.predict([[35]]))