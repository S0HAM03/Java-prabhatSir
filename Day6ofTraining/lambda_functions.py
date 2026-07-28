# ==========================================
# CONCEPT: Lambda Functions, Map, and Filter
# ==========================================

# IMPORTANT REMARK: Lambda Basics
# Lambda functions are anonymous, single-line functions.
# They are incredibly useful for quick operations, especially with map() and filter().

# Example 1: map() to transform data
names = ["nikhil", "ajay", "priya"]
upper = list(map(lambda x: x.upper(), names))
print("Uppercase names:", upper)

num = [3, 4, 5, 6, 7]
sqr = list(map(lambda x: x * x, num))
print("Squared numbers:", sqr)

sent = "python is easy and python is powerful"
# Getting the length of each word
word_lengths = list(map(lambda x: len(x), sent.split(' ')))
print("Word lengths:", word_lengths)

# Example 2: filter() to extract data matching a condition
g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use filter for retrieving only true values (e.g., even numbers)
gtr = list(filter(lambda x: x % 2 == 0, g))
print("Even numbers:", gtr)

namess = ["Aikhil", "Ajay", "priya"]
# Filtering names that start with "A"
upperr = list(filter(lambda x: x.startswith("A"), namess))
print("Names starting with A:", upperr)
