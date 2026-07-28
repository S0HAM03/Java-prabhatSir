# # # # # a=10
# # # # # b=20
# # # # # c=a+b
# # # # # print(c)
# # # #
# # b=10
# # g=20
# # f=b+g
# # print(f)
# #
# #
# def abc():
#       a = 10
#       b = 20
#       c = a + b
#       print(c)
# abc()
# abc()
# # # abc()
# # # # #
# # # # #
# # # # # def factorial(n): #5,4,3,2,1
# # # # #     if n == 1:
# # # # #         return 1
# # # # #     else:
# # # # #         return n * factori al(n-1)
# # #
# # # # # print(factorial(5))
# # # # # def prin )
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #without paramter function
# # # # #with parameter
# # # # #default paramter
# # # # #
# # # # #
# # # # # def greet():
# # # # #     print("Hello, welcome to Python!")
# # # # #     print("Hello, welcome to Python!")
# # # # #     print("Hello, welcome to Python!")
# # # # #     print("Hello, welcome to Python!")
# # # # #     print("Hello, welcome to Python!")
# # # # #     print("Hello, welcome to Python!")
# # # # #     print("Hello, welcome to Python!")
# # # # # greet()
# # # # # #
# # # # # #
# # # # # #
# def add(a,b):
#     return a + b
#
# result = add(3,4 )
# print(result)
#
# # # # # # # print(add(39,28))
# # # # # # # print(add(9,2))
# # # # # # print(add(3,28))
# # # # #
# # # # # print(result)
# # # # # # print(add(20,30))
# # # # # # print(add(40,40))
# # # # # # print(add(30,30))
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # a=10
# # # # # # b=20
# # # # # # print(a+b)
# # # # #
# # # # # #
# # # # # # print(add(10,20))
# # # # # d
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # print(result)
# # # # # # print(result)
# # # # # #
# # # # #
# # # # #
# # # # # # 4. Default Parameters
# # # # #
# # # # # # You can provide default values for parameters:
# # #
# def greet(name="User"):
#     print(name)
#     # print(f"Hello, {name}!")
#
#
# greet()         # Output: Hello, User!
# greet("Alice")  # Output: Hello, Alice!
# # # #
# # # # # a="nikhil"
# # # #
# # # #
# # # # # for i in range(5): #0,1,2,3,4
# # # # #     print(i)
# # # # # def print_number(n):
# # # # #     if n==0:
# # # # #         return
# # # # #     print(n)
# # # # #     print_number(n-1)
# # # # # print(print_number(6))
# # # # # # def collage(name="soni "):
# # # # # #     print(name)
# # # # # # collage()
# # # # # # collage("DY patil")
# # # # #
# # # # #
# # # # # #Default paramter
# # # # #
# # # # # #
# # # # # # def solapur(name="nikhil"):  #default para
# # # # # #     print("hellow",name)
# # # # # # solapur()
# # # #
# # # # # # solapur("pratmesh")   #with parameter
# # # # #
# # # # #
# # # # #
# # # # # #multi of two number
# # # # #
# # # # # # def check_even(number):
# # # # # #     if number%2==0:
# # # # # #         return True
# # # # # #     else:
# # # # # #         return False
# # # # # # num=4
# # # # # # if check_even(num):
# # # # # #     print(num,"is_even")
# # # # # # else:
# # # # # #     print(num,"is_false")
# # # # #
# # # # # #
# # # # # # def check_numb(abc):
# # # # # #     if abc%2==0:
# # # # # #         print("even",abc)
# # # # # #     else:
# # # # # #         print("odd",abc)
# # # # # # check_numb(4)
# # # # #
# # # # # # check_numb(3)
# # # # # # check_numb(5)
# # # # # # check_numb(6)
# # # # #
# # # # # ##map(function, iterable)
# # # # #
# # # # # # Applies a function to each element in an iterable.
# # # # # #
# # # # # # Returns a map object (convert to list/tuple to see results).
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # # check_numb(5)
# # # # # # check_numb(6)
# # # # # # check_numb(7)
# # # # # # check_numb(8)
# # # # # # check_numb(9)
# # # # #
# # # # # #string reverse using function ### IMP
# # # # #
# # # # # # li=[2,3,4,5,6]
# # # # # # for i in li:
# # # # # #       if i %2==0:
# # # # # #             print("this is odd",i)
# # # # # #       else:
# # # # # #             print("this is even ",i)
# # # # #
# # # # #
# # # # # # 4. Factorial of a Number
# # # # # # def factorial(n):
# # # # # #     result = 1
# # # # # #     for i in range(1, n + 1):
# # # # # #         result *= i
# # # # # #     return result
# # # # # #
# # # # # # print("Factorial:", factorial(int(input("Enter a number: "))))
# # # # #
# # # # #
# # # # # # 7. Find Largest of Three Numbers
# # # # # def find_largest(a, b, c,d):
# # # # #     return max(a, b, c,d)
# # # # #
# # # # # print("Largest:", find_largest(3, 7, 5,10,54))
# # # #
# # # # # # 8. Swap Two Variables
# # # # #
def swap(a, b):
    a, b = b, a
    return a, b

a, b = swap(10, 20)
# # # # print("a =", a, "b =", b)
# # # # #
# # # # #
# # # #
# l=[80,60,20,40,34,90]
# max=second=0
# for i in l:
#     if i>max :
#         second=max
#         max=i
#     elif i>second and i!=max:
#         second=i
# print(max)
# print(second)
#
# # # # #
# # # # # #dactorial of number 5
# # # # # #5*4*3*2*1
# # # # # # def factorial_numer(num):
# # # # # #     if num==1:
# # # # # #         return 1
# # # # # #     else:
# # # # # #         return num*factorial_numer(num-1)
# # # # # # gi=factorial_numer(5)
# # # # # # print(gi)
# # # # #
# # # # # # 9. Check for Palindrome
# # # # # # 5*4*3*2*1=120 #factorial
# # # # # # 3*2*1=6
# # # # # #nikhil
# # # # #
# # # # # # nayan #assedind
# # # # # # nayan
# # # # # #nikhil
# # # # # # def is_pali lindrome" if is_palindrome(string) else "Not Palindrome")
# # # # #
# # # # # #palindrom
# # # # # #nayan
# # # # #
# # # # # def pal(s):
# # # # #     if s==s[::-1]: ##nanw==wnaw
# # # # #         print("this is palindrom")
# # # # #     else:
# # # # #         print("not palindrom")
# # # # # print(pal("nanw"))
# # # # # #
# # # # # #
# # # # #
# # # # # # Simple Calculator
# # # # #
# # # # # # def calculator(a, b, op):
# # # # # #     if op == '+':
# # # # # #         return a + b
# # # # # #     elif op == '-':
# # # # # #         return a - b
# # # # # #     elif op == '*':
# # # # # #         return a * b
# # # # # #     elif op == '/':
# # # # # #        return a / b
# # # # # #     else:
# # # # # #         return "Invalid operation"
# # # # # # #
# # # # # # a = float(input("Enter first number: "))
# # # # # # b = float(input("Enter second number: "))
# # # # # # op = input("Enter operation (+, -, *, /): ")
# # # # # # print("Result:", calculator(a, b, op))
# # # # #
# # # # # ###################24/4/2025
# # # # # #defaulr argurment example
# # # # # # Python program to demonstrate
# # # # # # default arguments
# # # # # def myFun(x, y=50):
# # # # #     print("x: ", x)
# # # # #     print("y: ", y)
# # # # # print(myFun(30,56))
# # # # #
# # # # # # # Driver code (We call myFun() with only
# # # # # # # argument)
# # # # # # myFun()
# # # # #
# # # # # #calcuate the Area by uding default argurment
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # Keyword Arguments
# # # # # # Python program to demonstrate Keyword Arguments
# # # # # # def student(firstname, lastname):
# # # # # #     print(firstname, lastname)
# # # # # #
# # # # # #
# # # # # # # Keyword arguments
# # # # # # student('Geeks', lastname='Practice')
# # # # # # student(lastname='Practice', firstname='Geeks')
# # # # #
# # # # # #Postion RAGURMENT
# # # # #
# # # # # # def nameAge(name, age):
# # # # # #     print("Hi, I am", name)
# # # # # #     print("My age is ", age)
# # # # # #
# # # # # #
# # # # # # # You will get correct output because
# # # # # # # argument is given in order
# # # # # # print("Case-1:")
# # # # # # nameAge("Suraj", 27)
# # # # # # print("case -2")
# # # # # # # nameAge("nikhil",28)
# # # # # # nameAge(30,"pratmesh")
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # You will get incorrect output because
# # # # # # argument is not in order
# # # # # # print("\nCase-2:")
# # # # # # nameAge(27, "Suraj")
# # # # #
# # # # #
# # # # #
# # # # # # def is_prime(num):
# # # # # #     if num <= 1:
# # # # # #         return False
# # # # # #     for i in range(2, num):
# # # # # #         if num % i == 0:
# # # # # #             return False
# # # # # #     return True
# # # # # #
# # # # # # n = int(input("Enter a number: "))
# # # # # # print("Prime" if is_prime(n) else "Not Prime")
# # # # #
# # # # # # def is_prime(num):
# # # # # #     if num <= 1:
# # # # # #         return False
# # # # # #     for i in range(2, num):
# # # # # #         if num % i == 0:
# # # # # #             return False
# # # # # #     return True
# # # # # #
# # # # # # result = is_prime(4)
# # # # # # print("Prime" if result else "Not Prime")
# # # # #
# # # # # ## square of avlue
# # # # # # def square(x):
# # # # # #     return x * x
# # # # # #
# # # # # # print(square(4))  # Output: 16
# # # # #
# # # # # #=================================================
# # # # # #Default Parameters
# # # # # # def greet(name="Guest"):
# # # # # #     print(f"Hello, {name}!")
# # # # # #
# # # # # #
# # # # # # greet()          # Output: Hello, Guest!
# # # # # # greet("John")    # Output: Hello, John!
# # # # #
# # # # #
# # # # # # def nik(name="Nikhil"):
# # # # # #     print("this is name",name)
# # # # # # print(nik())
# # # # #
# # # # # # def nik(name="Nikhil"):
# # # # # #     print("this is name",name)  # default name
# # # # # # nik()
# # # # # # nik(name="Krishana")
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # #==========================================
# # # # # # Keyword Arguments
# # # # # #
# # # # # # def student_info(name, age):
# # # # # #     # print(f"Name: {name}, Age: {age}")
# # # # # #     print("this is name",name,"and age is ",age)
# # # # # #
# # # # # # student_info(age=20, name="Amit")
# # # # # #
# # # # # #
# # # # # # #0. Variable Number of Arguments
# # # # #
# # # # # # *args for variable number of positional arguments.
# # # # # # def 5,7,5)
# # # #
# def sum_all(*numbers):
#     return sum(numbers)
#
# print(sum_all(1, 2, 3, 4,20,30,4, 0,203,54,342,23423))# Output: 10
# # # # #
# # # #
# # # # # # *args (Non-Keyword Arguments)
# # # # # #
# # # # # # *args lets you pass a variable number of positional arguments to a function.
# # # # # #
# # # # # # Inside the function, args will be a tuple containing all the arguments.
# # # # #m
# def sum_all(*numbers):
#     return sum(numbers)
# #
# print(sum_all(1, 2, 3, 4,20,30,40,203,54,342,234234,23423,4234234))

# def f(**kwargs):
#     print(kwargs)
# f(greet="hello",name="chirag",subject="CSE")
# # # # # #

# # # # #
# # # # # ###2. **kwargs (Keyword Arguments)
# # # # #
# # # # # # **kwar the function, kwargs will be a dictionary containing all the arguments.
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # #
# # # # # def name(na):
# # # # #     print(na)
# # # # # name("nk","jkjefnwe","sfjifenfe","jfbsjfbf","bejujhe","gdhdqwuid","fgvufgugvuff","kshdbhd")
# # # # #
# # # # # # def abc(name):
# # # # # #     print(name)
# # # # # # abc("a","b")
# # # # # # def functino(*args):
# # # # # #     print(type(args))
# # # # # #     print(args)
# # # # # # str="i am coader "
# # # # # # functino(str)
# # # # #
# # # # # # def name(l):   # second option
# # # # # #     print(l)
# # # # # # l=["nikhil",'solapue',"bmit","jkbej"]
# # # # # # name(l)
# # # # #
# # # # #
# # # # # # def abc(x,y):
# # # # # #     print("x",x)
# # # # # #     print("y",y)
# # # # # # abc(10,20,30,30,39)
# # # # #
# # # #
# # # #
# # # # # def fib(n):
# # # # #     if n==0:
# # # # #         return 0
# # # # #     elif n==1:
# # # # #         return 1
# # # # #     else:
# # # # #         return fib(n-1)+fib(n-2)
# # # # # print(fib(6))
# # # # # **kwargs for variable number of keyword arguments
# # # # # def show_i  e="Alice", age=25, course="Python",name1="nikhil",city='pune')
# # # # # # # di={"name":"Alica","a ge":20,"city":"USA"}
# # # # # # show_info(**di)
# # # # # print(show_info())
# # # # #
# # # # # # def show_info(a, b):
# # # # # #     print(a, b)
# # # # # #
# # # # # # di = {"name": "nikhil", "city": "solapur"}
# # # # # # show_info(di["name"], di["city"])
# # # # #
# # # # #
# # # # #
# # # # # a=20 # this is global varibale
# # # # # def function():
# # # # #       #local variable
# # # # #       global a
# # # # #       # b=10+20
# # # # #       b=a+20   #LOCAL
# # # # #       print(b)
# # # # # function()
# # # # # # print(b)
# # # # # # print(a)
# # # # # # print(b)
# # # # #
# # # # # #
# # # # # #
# a=10   #global variable
# def my_function():
#     global a  #10
#     b=10+a  #30# local
#     print(b)
# my_function()
# print(a)
# print(b)
# # # # #
# # # # #
# # # # #
# # # # # def my_function():
# # # # #     y = 5  # Local variable
# # # # #     print(y)
# # # # #
# # # # # d=my_function()
# # # # # print(y)
# # # # # print(d)
# # # # # Error! 'y' is not defined outside the function
# # # # #
# # # # #
# # # # # # is_logged_in = False  # Global variable
# # # # # #
# # # # # # def login(username, password):
# # # # # #     is_logged_in = True  # Local variable (different)
# # # # # #     print(f"User {username} logged in.")
# # # # # #     # print(is_logged_in)
# # # # # #
# # # # # # login("admin", "1234")
# # # # # # # print(is_logged_in)  # Still False, because the change inside function was local
# # # # #
# # # # #
# # # # #
# # # # # #2)Student attendance mark
# # # # total_students = 50  # Global variable
# # # #
# # # # def mark_attendance(present):
# # # #     absent = total_students - present  # Local variable
# # # #     print(f"Present: {present}, Absent: {absent}")
# # # #
# # # # mark_attendance(45)
# # # # # print(absent)  #
# # # # print(total_students)
# # #
# # #
# # #
# # # # #
# # # # #
# # # # # #3)cart_items = []  # Global list
# # # # # # cart_items = []
# # # # # # def add_to_cart(item):
# # # # # #     cart_items.append(item)  # Modifying global variable
# # # # # #     # print(f"{item} added to cart.")
# # # # # #     print("added to cart",item)
# # # # # #
# # # # # # add_to_cart("Laptop")
# # # # # # add_to_cart("Mouse")
# # # # # # print(f"Final Cart: {cart_items}")
# # # # #
# # # # #
# # # # #
balance = 1000  # Global variable
#
def withdraw(amount):
    global balance
    if amount <= balance:
        balance-=amount
        print(f"Withdrawal successful. Remaining balance: {balance}")
    else:
        print("Insufficien  t balance.")
# #
withdraw(200)
print(f"Balance outside function: {balance}")
# # #
# # # # # #
# # # # # # Find Second Largest Number in List
# # # # # # def second_largest(nums):
# # # # # #     return sorted(set(nums))[-2]
# # # # # #
# # # # # # print(second_largest([10, 20, 4, 45, 99]))  # 45
# # # # #
# # # # # ##
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # #map filter and reduce
# # # # # # mark=[77,97,64,85,55]
# # # # # # a=mark[0]
# # # # # # print(a)
# # # # # #
# # # # # # print(
# # # # # #     mark
# # # # # # )
# # # # #
# # # # # # mark=[77,97,64,85,55]
# # # # # # def grade(mark):
# # # # # #     if mark>=90:
# # # # # #         return "A"
# # # # # #     elif 80<=mark<90:
# # # # # #         return 'B'
# # # # # #     elif 70<=mark <80:
# # # # # #         return 'C'
# # # # # #     elif 60<=mark<70:
# # # # # #         return 'D'
# # # # # #     else:
# # # # # #         return 'F'
# # # # # # grade=map(grade,mark)
# # # # # # print("Exam score",mark)
# # # # # # print("grade",next(grade))
# # # # # # print("grade",next(grade))
# # # # # # print("grade",next(grade))
# # # # #
# # # # #
# # # # # # print("grade",list(grade)) # one time access all element
# # # # #
# # # # #
# # # # # #square of number
# # # # # # Function to square a number
# # # # # def squ [1, 2, 3, 4, 5]
# # # # # # #
# # # # # # # Use map to apply square function to each number
# # # # # # # squared_numbers = list(map(square, numbers))
# # # # # # squared_numbers=map(square,numbers)
# # # # # # print(next(squared_numbers))  # Output: [1, 4, 9, 16, 25]
# # # # # # print(next(squared_numbers))
# # # # # # print(next(squared_numbers))
# # # # #
# # # # #
# # # # # #3)Example 3: Converting Strings to Integers
# # # # # # string_numbers = ['1', '2', '3', '4']
# # # # # #
# # # # # # # Convert each string to an integer
# # # # # # int_numbers = list(map(int, string_numbers))
# # # # # #
# # # # # # print(int_numbers)  # Output: [1, 2, 3, 4]
# # # # #
# # # # # # a=int(input("enter a number" ))
# # # # #
# # # # # # break
# # # for i in range(10):  #  0,1,2,3,4.........9
# # #     if i == 5:
# # #         break  # Exit the loop when i is 3
# # #     print(i,end=" ")
# # # # Output:
# # # # # # 0
# # # # # # 1
# # # # # # 2
# # # # #
# # # # # #continue
# # # # # # for i in range(5):
# # # # # #     if i == 2:
# # # # # #         continue  # Skip printing when i is 2
# # # # # #     print(i,end=" ")
# # # # # # Output:
# # # # # # 0
# # # # # # 1
# # # # # # 3
# # # # # # 4
# # # # #
# # # # #
# # # # #
# # # # # #pass
def my_function():
    pass
     # Placeholder for future implementation
for i in range(10):
    if i % 2 == 0:
        print(i)  # Do nothing if i is even
    else:
        pass
        # print(i)
my_function()
# # # # # # #v
# # # # # # # # Output:
# # # # # # 1
# # # # #
# # # # # #######################map(function, iterable)
# # # # #
# # # # # # Applies a function to each element in an iterable.
# # # # # #
# # # # # # Returns a map object (convert to list/tuple to see results).
# # # # #
# # # # #
# # # # # # nums = [1, 2, 3, 4, 5]
# # # # # # squares = list(map(lambda x: x*x, nums))
# # # # # # print(squares)  # [1, 4, 9, 16, 25]
# # # # # #
# # # # #
# # # # #
# # # # # #Convert list of strings to uppercase:
# # # # # # names = ["nikhil", "ajay", "priya"]
# # # # # # upper = list(map(lambda x: x.upper(), names))
# # # # # # print(upper)  # ['NIKHIL', 'AJAY', 'PRIYA']
# # # # #
# # # # #
# # # # #
# # # # # #Convert list of numbers to string:
# # # # # # nums = [1, 2, 3]
# # # # # # str_nums = list(map(str, nums))
# # # # # # print(str_nums)  # ['1', '2', '3']
# # # # #
# # # # #
# # # # # # 2. filter(function, iterable)
# # # # # #
# # # # # # Filters elements based on a condition (True/False).
# # # # # #
# # # # # # Returns a filter object.
# # # # #
# # # # # # nums = [10, 15, 20, 25, 30]
# # # # # # evens = list(filter(lambda x: x % 2 == 0, nums))
# # # # # # print(evens)  # [10, 20, 30]
# # # # #
# # # # # # Filter positive numbers:
# # # # # # nums = [-5, -2, 0, 3, 7]
# # # # # # positive = list(filter(lambda x: x > 0, nums))
# # # # # # print(positive)  # [3, 7]
# # # # #
# # # # #
# # # # # ##Filter names starting with “A”:
# # # # # # names = ["Amit", "Raj", "Anita", "Ravi"]
# # # # # # a_names = list(filter(lambda x: x.startswith("A"), names))
# # # # # # print(a_names)  # ['Amit', 'Anita']
# # # # #
# # # # #
# # # # # # 3. reduce(function, iterable)
# # # # # #
# # # # # # 👉 (must import from functools)
# # # # # #
# # # # # # Repeatedly applies the function to the iterable and reduces it to a single value.
# # # # # #
# # # # # # from functools import reduce
# # # # # #
# # # # # # nums = [1, 2, 3, 4, 5]
# # # # # # total = reduce(lambda a, b: a + b, nums)
# # # # # # print(total)  # 15
# # # # #
# # # # # #find vowels in string
# # # # def xyz(str):
# # # #     vowesl='aeiouAEIOU'
# # # #     count=0
# # # #     for i in str:
# # # #         if i in vowesl:
# # # #             count+=1
# # # #     return count
# # # # print(xyz("nIkhil"))
# # # # #
# # # # # #
# # # # def vovel_counter(String):
# # # #     v="AEIUOaeiou"
# # # #     count=0
# # # #     for i in String:
# # # #         if i ==v :
# # # #             count =+1
# # # #         else :
# # # #             pass
# # # #     print(count)
# # # # vovel_counter("ALICE")
# # #
# # # #
# # # # #lambda function
# # # # # Lambda Function in Python
# # # # #
# # # # # A lambda function is an anonymous (nameless) function written in a single line.
# # # # #
# # # # # 👉 Why use Lambda?
# # # # #
# # # # # For short and simple logic
# # # # #
# # # # # For temporary functions
# # # # #
# # # # # Commonly used with map(), filter(), and reduce()
# # # #
# # # # #syntex lambda arguments : expression
# # # #
# # # #
# # # # # 1)Square of a number
# # square = lambda x: x * x
# # print(square(5))
# # # #
# # # # #2)lambda vs normal function
# # # # # def add(a, b):
# # # # #     return a + b
# # # #
# # # #
# # # # # add = lambda a, b: a + b
# # # #
# # # # #3)Limitations of Lambda
# # # #
# # # # # Only one expression allowed
# # # # #
# # # # # No loops (for, while)
# # # # #
# # # # # No assignments
# # # # #
# # # # # Not suitable for complex logic
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # # a=lambda x:x+y
# # # # # print(5)
# # # # #
add=lambda x,y:x+y
print(add(5,3))
# # # #
# # # # #pass multipal value return in lambda function
# # # # # add=lambda x,y:(x+y,x-y)
# # # # # a,s=add(4,5)
# # # # # print(a)
# # # # # print(s)
# # # #
# defalult keywaord arg



a=lambda x,y=2 :x+y
print(a(2))
# # # #
# # # #
# # # # #Map map() Function
# # # #
# # # # # The map() function applies a function to each element of an
# # #  #
# # # # # map(function, iterable)
# # # #
# # # # # Square of all elements
# # # # # numbers = [1, 2, 3, 4]
# # # # # result = list(map(lambda x: x * x, numbers))
# # # # # print(result)
# # # #
# # # # #2)
# # # # # Convert strings to uppercase
# # # # # names = ["ram", "shyam", "geeta"]
# # # # # result = list(map(lambda x: x.upper(), names))
# # # # # print(result)
# # # #
# # # # #Filter
# # # #
# # # # # filter() Function
# # # # #
# # # # # The filter() function selects elements from an iterable based on a condition.
# # # #
# # # #
# # # # # marks=[30,40,60,70,67,66]
# # # # # def feling(score):
# # # # #     return score<60
# # # # # result=filter(feling,marks)
# # # # # print("faling score",list(result))
# # # #
# # # #
# # # #
# # # # #2)
# # # # # Even numbers
# # # # # numbers = [1, 2, 3, 4, 5, 6]
# # # # # result = list(filter(lambda x: x % 2 == 0, numbers))
# # # # # print(result)
# # # #
# # # #
# # # # #3)Marks greater than 50
# # # # # marks = [45, 78, 90, 32, 60]
# #
# #
# # # # # result = list(filter(lambda x: x > 50, marks))
# # # # # print(result)
# # # #
# # # #
# # # #
# # # #
# # # # #using list (all out come in one time )other wise using next key one by one value access
# # # #
# # # #
# # # # # Short Exam Answers
# # # #
# # # # # What is Lambda?
# # # # # A lambda function is an anonymous, single-expression function.
# # # # #
# # # # # What is map()?
# # # # # Applies a function to each element of an iterable.
# # # # #
# # # # # What is filter()?
# # # # # Filters elements based on a condition.
# # # # #
# # # # # What is reduce()?
# # # # # Reduces multiple values to a single value
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
# .