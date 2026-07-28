
# A for loop in Python is used for iterating over sequences like lists, tuples, strings,


# for variable in iterable:

# fruits = ["apple", "banana", "cherry"]
#
# for i in fruits:
#     print(i)


# You can iterate over each character in a string

# word = "hello"
# for char in word:
#     print(char)



# person = {"name": "John", "age": 30, "city": "New York"}
# #
# # # Iterating over keys (default behavior)
# for value in person:
#     print(value)
# #
# for value in person.values():
#     print(value)

#by using for kay:value pair get
# # Iterating over values
# for value in person.values():
#     print(value)
#
# # Iterating over both keys an  d values
# for key, value in person.items():
#     print(f"{key}: {value}")


# 2. Iterating Through a List to Modify Each Element
# my_list = [1, 2, 3, 4, 5]



 # for i in range(len(my_list)):
#     my_list[i] = my_list[i] * 2
#
# print(my_list)



# 2. Iterating Through a List of Numbers and Printing Their Squares
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num * num)

# 3. Print Only the Numbers Greater than 5 in a List

# numbers = [3, 7, 1, 9, 4, 6]
# for num in numbers:
#     if num > 5:
#         print(num)

# 5. Loop Through a List and Check for a Specific Item
# fruits = ["apple", "banana", "cherry", "orange"]
# item_to_find = "banana"
#
# for fruit in fruits:
#     if fruit == item_to_find:
#         print(fruit,"iteam found ")
#         break
# else:
#     print(f"{item_to_find} not found!")

#3. Iterating Through a List and Performing a Conditional Check
# my_list = [10 um} is odd")


# 7. Iterating Over a List to Create a New List with Squares
# my_list = [1, 2 _list)


# try:
# except
# else
# finally:


#The range() Function
# The range() function generates a sequence of numbers and is commonly used
# in for loops when you need to iterate over a sequence of numbers.


# range(start, stop, step)
#
# start: The starting number (inclusive).
# stop: The ending number (exclusive).
# step: The difference between each number in the sequence (default is 1).
# a=[1,2,3,4]
# print(a[1:3])

# a=[1,2,3,4,...........10000]
# for i in range(100):
#     print(i)

# for i in range(1, 6):
#     print(i)



#using Break,comtinue,pass
# break → Exits the loop prematurely.
# continue → Skips the current iteration.
# pass→ Executes after loop completion (if not exited by break).


# for i in range(1,6):
#     if i == 4:
#         break
#     print(i)

#continue
#
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# for i in range(10):
#     if i==5:
#         continue
#     print(i)



###sum of using for loop
# Sum of numbers using a for loop:

# total = 0
# for i in range(1, 6):
#     total=total+i
# print(total)



#Multiplying each element in a list by 2
# numbers = [1, 2, 3, 4, 5]




# doubled = []
# for number in numbers:
#     doubled.append(number * 2)
# print(doubled)


# for i in range(10):
#     print(i)


#reating a list of squares of numbers:
# squares = []
# for i in range(1, 6):
#     squares.append(i ** 2)
# print(squares)


#Creating a list of squares of numbers:

# squares = []
# for i in range(1, 6):
#     squares.append(i ** 2)
# print(squares)


#Loop over a set
# unique_numbers = {1, 2, 3, 4, 5}
# for num in unique_numbers:
#     print(num)


Flattening a list of lists
lists = [[1, 2, 3], [4, 5], [6, 7]]
# flattened = []
 # for sublist in lists:
#     for item in sublist:
#         flattened.append(item)
# print(flattened)



# calcuate the sum of number in list
# a=[10,2,30]
# h=[]
# for i in a:
#     h.append(i*2)
# print(h)

#calcuate square of number
# a=[2,3,4,5]
# h=[]
# for i in a:
#     h.append(i**2)
# print(h)



#find max number in list
#
# departments = ["HR", "Finance", "Engineering", "Marketing"]
# for dept in departments:
#     print("Generating report for " + dept + " department...")
#     # Code to generate department-specific report





# recipients = ["alice@example.com", "bob@example.com", "charlie@example.com"]
# for email in recipients:
#     print("Sending email to "+ email + "...")
    # Code to send email


# departments = ["HR", "Finance", "Engineering", "Marketing"]
# for dept in departments:
#     print("Generating report for " + dept + " department...")
    # Code to generate department-specific report




# numbers = [3, 5, 7, 2, 8, 6, 1]
# print(max(numbers))

# Initialize the max_number with the first element in the list
# max_number = numbers[0]      #3  5  7 8

# Loop through the list starting from the second element
# for num in numbers:
#     if num >= max_number:      #3>=3, 7  2
#         max_number = num      #3

# print("The maximum number is:", max_number)
