balance = 1000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    print("Please collect your cash.")
    balance -= withd raw
else:
    print( "Insufficient balance .")

#2)Password Str ength Checker
# password = input("Enter password: ")
# if len(password) >= 8 and any(c.isdigit() for c in password):
#     print("Strong Password")
# else:
#     print(" Weak Password")


#3)Contact Search in Phone Book (Dictionary)
# contacts = {"Nikhil": "9876543210", "Amit": "8888888888"}
# name = input("Enter name: ")
# if name in contacts:
#     print("Contact Number:", contacts[name])
# else:
#     print("Contact not found.")


#4Login Authentication (If-Else + Function)
# def login(username, password):
#     if username == "admin" and password == "1234":
#         return "Login Successful"
#     else:
#         return "Invalid credentials"
#
# print(login("admin", "1234"))


#4). Check Palindrome Word (Basic Logic + Condition)
# word = in
#5) Count Vowels in a Sentence (Loop + Condition)
# sentence = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in sentence:
#     if char in vowels:
#         count += 1
# print("Vowel count:", count)

#count owels in string
# a="nikhilaeio"
# b="aeiou"
# c=0
# for i in a:
#     if i in b:
#         c=c+1
# print("owels in string",c)



#6Reverse Each Word in a Sentence (Loop + List)
# sentence = input("Enter sentence: ")
# words = sentence.split()
# reversed_words = [word[::-1] for word in words]
# print(" ".join(reversed_words))


#or
# a="nikhil"
# b=a[::-1]
# print(b)

#find max number in lsit

# numbers = [12, 45, 23, 67, 34]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print("Maximum number is:", max_num)




# v=[12,3,4,567,54]
# h=v[0]
# for i in v:
#     if i >=h:
#         h=i
# print(h)


# Prime Number Checker (Loop + Condition)
# num=int(input('enter a number'))
# if num>=1:
#     for i in range(2,num):
#         if i%2==0:
#             print('not a prime')
#         else:
#             print('reaming all prime number')
# else:
#     print('pl enter more then one number'or 'not a prime number')

# create a calcuator
# def calculator(a, b, op):
#     try:
#         if op == '+': return a + b
#         elif op == '-': return a - b
#         elif op == '*': return a * b
#         elif op == '/': return a / b
#         else: return "Invalid Operator"
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
#
# print(calculator(10, 5, '/'))


# password avalidation 
# def is_valid(password):
#     return (
#         len(password) >= 8 and
#         any(c.isdigit() for c in password) and
#         any(c.isalpha() for c in password)
#     )
#
# pwd = input("Enter password: ")
# print("Valid" if is_valid(pwd) else "Invalid")


#  Sort a List Without sort()
# numbers = [5, 2, 9, 1, 7]
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] > numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
# print(numbers)

# fiizbuz
# def fizzBuzz(n):
#     result = []
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#
#         else:
#             result.append(str(i))
#     return result
# print(fizzBuzz(15))
#


#
# def lengthOfLastWord(s):
#     return len(s.strip().split()[-1])
# print(lengthOfLastWord("nikhil"))


#
# import copy
#
# original = [[1, 2, 3], [4, 5, 6]]
# shallow = copy.copy(original)
#
# shallow[0][0] = 99
#
# print(original)  # [[99, 2, 3], [4, 5, 6]]
# print(shallow)   # [[99, 2, 3], [4, 5, 6]]


     

###Deep
# import copy
#
# original = [[1, 2, 3], [4, 5, 6]]
# deep = copy.deepcopy(original)
#
# deep[0][0] = 99
#
# print(original)  # [[1, 2, 3], [4, 5, 6]]
# print(deep)      # [[99, 2, 3], [4, 5, 6]]
#














