# # =================================================
# # TOP 30 PYTHON INTERVIEW OBJECTIVE QUESTION BANK
# # =================================================
# # ( Data Types, Functions, Lambda, Decorators,
# #   Generators, OOP, Exception Handling,
# #   Stack, Queue, Searching )
# # =================================================
# #
# # SECTION 1: DATA TYPES
# # ------------------------------ -------------------
# # 1. What is the output?
a = [1, 2, 3]
b = a
b.append(4)
print(a)
# #
# # 2. Which data type is immutable?
# # A) list
# # B) set
# # C) dictionary
# # D) tuple
# #
# # 3. What is the output?
# # print(type({}))
# #
# # 4. What is the output?
# # print(type((1)))
# #
# # 5. What is the output?
# # print(bool([]), bool(0), bool(1))
# #
# # 6. What is the output?
# # print(10 == 10.0)
# #
# # -------------------------------------------------
# # SECTION 2: FUNCTIONS
# # -------------------------------------------------
# # 7. What is the default return value of a function?
# # A) 0
# # B) False
# # C) None
# # D) Error
# #
# # 8. What is the output?
# # def func(x=[]):
# #     x.append(1)
# #     return x
# #
# # print(func())
# # print(func())
# #
# # 9. What is the output?
# # def test(a, b=5):
# #     return a + b
# #
# # print(test(3))
# #
# # 10. Which keyword is used to define a function?
# # A) define
# # B) def
# # C) function
# # D) fun
# #
# # -------------------------------------------------
# # SECTION 3: LAMBDA FUNCTIONS
# # -------------------------------------------------
# # 11. What is the output?
# # x = lambda a, b: a * b
# # print(x(2, 3))
# #
# # 12. Lambda functions can contain how many expressions?
# # A) 0
# # B) 1
# # C) 2
# # D) Unlimited
# #
# # -------------------------------------------------
# # SECTION 4: DECORATORS
# # -------------------------------------------------
# # 13. What is the main purpose of a decorator?
# # A) Modify function behavior
# # B) Delete function
# # C) Speed up Python
# # D) Reduce memory
# #
# # 14. Which symbol is used for decorators?
# # A) #
# # B) $
# # C) @
# # D) %
# #
# # -------------------------------------------------
# # SECTION 5: GENERATORS
# # -------------------------------------------------
# # 15. Which keyword is used in generators?
# # A) return
# # B) yield
# # C) break
# # D) pass
# #
# # 16. What is the output?
# # def gen():
# #     yield 1
# #     yield 2
# #
# # g = gen()
# # print(next(g))
# #
# # -------------------------------------------------
# # SECTION 6: EXCEPTION HANDLING
# # -------------------------------------------------
# # 17. Which block is always executed?
# # A) try
# # B) except
# # C) else
# # D) finally
# #
# # 18. What is the output?
# # try:
# #     print(1/0)
# # except ZeroDivisionError:
# #     print("Error")
# #
# # 19. Which exception occurs when index is out of range?
# # A) KeyError
# # B) IndexError
# # C) ValueError
# # D) TypeError
# #
# # -------------------------------------------------
# # SECTION 7: OOPS CONCEPTS
# # -------------------------------------------------
# # 20. Which concept allows one class to acquire properties of another?
# # A) Polymorphism
# # B) Encapsulation
# # C) Inheritance
# # D) Abstraction
# #
# # 21. What is the output?
# # class A:
# #     def show(self):
# #         print("A")
# #
# # class B(A):
# #     pass
# #
# # obj = B()
# # obj.show()
# #
# # 22. What does self represent?
# # A) Class
# # B) Object
# # C) Function
# # D) Module
# #
# # 23. Which concept hides internal implementation?
# # A) Inheritance
# # B) Polymorphism
# # C) Encapsulation
# # D) Overloading
# #
# # -------------------------------------------------
# # SECTION 8: STACK & QUEUE
# # -------------------------------------------------
# # 24. Stack follows which principle?
# # A) FIFO
# # B) LIFO
# # C) FILO
# # D) Random
# #
# # 25. Queue follows which principle?
# # A) LIFO
# # B) FIFO
# # C) FILO
# # D) None
# #
# # -------------------------------------------------
# # SECTION 9: SEARCHING
# # -------------------------------------------------
# # 26. Time complexity of linear search is:
# # A) O(1)
# # B) O(log n)
# # C) O(n)
# # D) O(n²)
# #
# # 27. Binary search requires the list to be:
# # A) Random
# # B) Unsorted
# # C) Sorted
# # D) Empty
# #
# # 28. Time complexity of binary search is:
# # A) O(n)
# # B) O(log n)
# # C) O(n²)
# # D) O(1)
# #
# # -------------------------------------------------
# # SECTION 10: OUTPUT / LOGIC
# # -------------------------------------------------
# # 29. What is the output?
# # print("Python"[::-1])
# #
# # 30. What is the output?
# # print(type(None))
# #
# # =================================================
# #U
# # =================================================
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# =================================================
# TOP 30 PYTHON INTERVIEW OBJECTIVE QUESTION BANK
# WITH ANSWERS
# =================================================
# ( Data Types, Functions, Lambda, Decorators,
#   Generators, OOP, Exception Handling,
#   Stack, Queue, Searching )
# =================================================
#
# SECTION 1: DATA TYPES
# -------------------------------------------------
# 1. What is the output?
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
# Answer: [1, 2, 3, 4]
#
# 2. Which data type is immutable?
# A) list
# B) set
# C) dictionary
# D) tuple
# Answer: D) tuple
#
# 3. What is the output?
# print(type({}))
# Answer: <class 'dict'>
#
# 4. What is the output?
# print(type((1)))
# Answer: <class 'int'>
#
# 5. What is the output?
# print(bool([]), bool(0), bool(1))
# Answer: False False True
#
# 6. What is the output?
# print(10 == 10.0)
# Answer: True
#
# -------------------------------------------------
# SECTION 2: FUNCTIONS
# -------------------------------------------------
# 7. What is the default return value of a function?
# A) 0
# B) False
# C) None
# D) Error
# Answer: C) None
#
# 8. What is the output?
# def func(x=[]):
#     x.append(1)
#     return x
#
# print(func())
# print(func())
# Answer:
# [1]
# [1, 1]
#
# 9. What is the output?
# def test(a, b=5):
#     return a + b
#
# print(test(3))
# Answer: 8
#
# 10. Which keyword is used to define a function?
# A) define
# B) def
# C) function
# D) fun
# Answer: B) def
#
# -------------------------------------------------
# SECTION 3: LAMBDA FUNCTIONS
# -------------------------------------------------
# 11. What is the output?
# x = lambda a, b: a * b
# print(x(2, 3))
# Answer: 6
#
# 12. Lambda functions can contain how many expressions?
# A) 0
# B) 1
# C) 2
# D) Unlimited
# Answer: B) 1
#
# -------------------------------------------------
# SECTION 4: DECORATORS
# -------------------------------------------------
# 13. What is the main purpose of a decorator?
# A) Modify function behavior
# B) Delete function
# C) Speed up Python
# D) Reduce memory
# Answer: A) Modify function behavior
#
# 14. Which symbol is used for decorators?
# A) #
# B) $
# C) @
# D) %
# Answer: C) @
#
# -------------------------------------------------
# SECTION 5: GENERATORS
# -------------------------------------------------
# 15. Which keyword is used in generators?
# A) return
# B) yield
# C) break
# D) pass
# Answer: B) yield
#
# 16. What is the output?
# def gen():
#     yield 1
#     yield 2
#
# g = gen()
# print(next(g))
# Answer: 1
#
# -------------------------------------------------
# SECTION 6: EXCEPTION HANDLING
# -------------------------------------------------
# 17. Which block is always executed?
# A) try
# B) except
# C) else
# D) finally
# Answer: D) finally
#
# 18. What is the output?
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("Error")
# Answer: Error
#
# 19. Which exception occurs when index is out of range?
# A) KeyError
# B) IndexError
# C) ValueError
# D) TypeError
# Answer: B) IndexError
#
# -------------------------------------------------
# SECTION 7: OOPS CONCEPTS
# -------------------------------------------------
# 20. Which concept allows one class to acquire properties of another?
# A) Polymorphism
# B) Encapsulation
# C) Inheritance
# D) Abstraction
# Answer: C) Inheritance
#
# 21. What is the output?
# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     pass
#
# obj = B()
# obj.show()
# Answer: A
#
# 22. What does self represent?
# A) Class
# B) Object
# C) Function
# D) Module
# Answer: B) Object
#
# 23. Which concept hides internal implementation?
# A) Inheritance
# B) Polymorphism
# C) Encapsulation
# D) Overloading
# Answer: C) Encapsulation
#
# -------------------------------------------------
# SECTION 8: STACK & QUEUE
# -------------------------------------------------
# 24. Stack follows which principle?
# A) FIFO
# B) LIFO
# C) FILO
# D) Random
# Answer: B) LIFO
#
# 25. Queue follows which principle?
# A) LIFO
# B) FIFO
# C) FILO
# D) None
# Answer: B) FIFO
#
# -------------------------------------------------
# SECTION 9: SEARCHING
# -------------------------------------------------
# 26. Time complexity of linear search is:
# A) O(1)
# B) O(log n)
# C) O(n)
# D) O(n²)
# Answer: C) O(n)
#
# 27. Binary search requires the list to be:
# A) Random
# B) Unsorted
# C) Sorted
# D) Empty
# Answer: C) Sorted
#
# 28. Time complexity of binary search is:
# A) O(n)
# B) O(log n)
# C) O(n²)
# D) O(1)
# Answer: B) O(log n)
#
# -------------------------------------------------
# SECTION 10: OUTPUT / LOGIC
# -------------------------------------------------
# 29. What is the output?
# print("Python"[::-1])
# Answer: nohtyP
#
# 30. What is the output?
# print(type(None))
# Answer: <class 'NoneType'>
#
# =================================================
# END OF FILE
# =================================================
#
