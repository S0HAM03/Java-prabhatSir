# In Python, a string is an immutable sequence of characters used to store and manipulate text.
# Strings are defined by enclosing characters in single ('...'), double ("..."),
# or triple quotes ('''...''' or """...""").



# Immutable: Once created, strings cannot be modified.

# Indexed: Supports indexing and slicing.

# Iterables: Can be looped through.




# # Single quotes
# str1 = 'Hello'
#
# # Double quotes
# str2 = "World"
#
# # Triple quotes (for multi-line strings)
# str3 = """This is
# a multi-line
# string."""





# Accessing Characters
#
# text = "Python"
# print(text[0])
# print(text[-3])



#  String Slicing
#
# text = "Python"
# print(text[0:3])   #
# print(text[:3])    #
# print(text[3:])    #

#

#1 methods

# startswith() and endswith()

# text = "Python programming"
# print(text.startswith("Py"))   # True
# print(text.endswith("ing"))    # True

#2) isalpha(), isdigit(), isalnum()

# print("abc".isalpha())         # True
# print("123".isdigit())         # True
# print("abc123".isalnum())      # True

#3)Converting to String
# num = 123
# str_num = str(num)
# print(str_num, type(str_num))  # Output: 123 <class 'str'>

#4Check for Substring

# sentence = "Learning Python is fun"
# print("Python" in sentence)  # True
# print("Java" not in sentence)

#5)Immutable Nature of Strings
 


# text = "Hello"
# text[0] = 'y'
# print(text)

#6 len
# a='python'
# print(len(a))
#
# #7Uppercase
# a='python'
# print(a.upper())

#8 lower
# a='PYTHON'
# print(a.lower())

#9 replace
# a='python'
# print(a.replace('p','k'))
# print(a.replace('t','o'))

#10 count
# a='ppppython'
# print(a.count('n'))

#11split
# a='python,aanugrag,education'
# print(a.split())