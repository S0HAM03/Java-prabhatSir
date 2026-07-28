#  Conditional statements in Python allow you to execute different
# blocks of code based on certain conditions.
# # They are fundamental for controlling the flow of a program.
#
# # 1. if Statement
# #
# # The if statement is used  to execute a block of code only if a condition is True
#
# # if condition:
#
age = 2
if age >= 18:  #condition 1
    print("You are eligible to vote.")
else:
    print("no ")

#
#
#
#
# #  2. if-else Statement
# #
# # Used when you want to execute one block of code if the condition is True and
# # a different block if the condition is False.
#
#
# age = 16
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
#
#
#
#
# #  3. if-elif-else Statement
# #
# # Used for multiple conditions. The elif (else if)
# # checks additional conditions if the previous ones are False.
#
# #a="nikhil
# # b=int(input("enter a string"))
# # print(b)
#
# marks = int(input("enter a number"))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# else:
#     print("Grade: c")
#
#
#
# # 4. Nested if Statements
# #
# # Using an if statement inside another if statement.
#
# # if condition1:
# #     if condition2:
#
# num =int(input("enter a number "))
# if num > 0:
#     print("Positive number")
#     if num % 2 == 0:
#         print("Even number")
#     else:
#         print("not even number")
# else:
#     print("pl enter postive number ")
#
# # Get the driver's speed and speed limit
# # sp   "$300 fine for excessive speeding.")
# # #
# # Output the fine
#
#
# # using logical operator
# #And -Both conditions must be True
# # or=any one condition must be true
#
# age = 20
# if age > 18 or age <=3:
#     print("You are a young adult.")
# else:
#     print("u r not ele")
#
# #or =At least one condition must be True.
# # day int("i am else ")
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
# #summary -==================================
#  # if for sin ocks.
#
#
# #real word example
# #1Program to Check if a Number is Positive, Negative, or Zero:
#
#
# #2 Scenario: Check if a username and password are correct to allow access
#
# username  id username or password.")
# username="nikhil"
# Pass="@"
# if username=="nikhil" and Pass=="@123 ":
#     print("iam access to insta")
# else:
#     print("pl enter correact username and pass ")
#
#
#
# #3Display actions based on the traffic light color
# # light = input("Enter traffic light color (red/yellow/green): ").lower()
# # if light == "red":
# #     print("Stop!")
# # elif light == "yellow":
# #     print("Get ready to move.")
# # elif light == "green":
# #     print("Go!")
# # else:
# #     print("Invalid color!")
#
# #4ATM
#
# balance = 5000
# withdraw_amount = int(input("Enter withdrawal amount: ₹")) #200
# if withdraw_amount > balance:
#     print("Insufficient balance!")
# elif withdraw_amount % 100 != 0:
#     print("Please enter an amount in multiples of ₹100.")
# else:
#     # balance -= withdraw_amount
#     balance=balance-withdraw_amount
#     print("Transaction successful! Remaining balance:",balance)
# # #
# #
# ##nasted condition statment
#
#
#
#
#
#
#
#
#
# # age
#
# # p
# #2)it checks if the person is 18 or older. Then, depending on their membership status,
# # if age more then 18 and and memabership==premiun so it is full access to in office
# #     if standard membership=='sta  ndard so limit access' and no memeebr shio so pl chek memenership
# #     other wise age is less then 18 you are not elagiable to memership show
#
# # purchasamount)
#
# # membership_status = 'gold'
# # total_price = 150
# #
# # if membership_stat us == 'platinum':
# #     discount = 0.2  # 20% discount
# # elif membership_status == 'gold':
# #     discount = 0.1  # 10% discount
# # elif membership_status == 'silver':
# #     discount = 0.05  # 5% discount
# # else:
# #     discount = 0  # No discount
#
# # final_pri inal price after discount: ${final_price}")
#
# # final_ final_amount)
#
# # meal_type = 'vegetarian'
# #
# # if meal_type == 'vegetarian':
# #     price = 12.99
# # elif meal_type == 'vegan':
# #     price = 14.99
# # elif meal_type == 'non-vegetarian':
# #     price = 16.99
# # else:
# #     price = 0  # Unknown meal type
# #
# # print(f"The price for the {meal_type} meal is ${price}")
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
# #1) Nasted
# # age = 32
# # has_id = True
# # if age >= 18:
# #     if has_id:
# #         print("You can enter the vot room.")
# #     else:
# #         print("You need an ID to enter vot room.")
# # else:
# #     print("You a  re too young to enter.")
#
# # x=10
# # y=1
# # if x>y:  # condition 1
# #     print("x is grater")  ###1
# #     if x>15: ####cond2
# #         print("x is also gratrer")
# #     elif x==10:
# #         print("x is exactely 10")
# #     else:
# #         print(" x is betwen y and 15")
# # elif x==y:
# #     print("x is equal y")
# # else:
# #     print("x is less then y")
#
#
#
#
# # age=20
# # membership_status = 'premium'
# #
# # if age >= 18:
# #     if membership_status == 'premium':
# #         print("You have full access to all content.")
# #     elif membership_status == 'standard':
# #         print("You have limited access.")
# #     else:
# #         print("Please check your membership status.")
# # else:
# #     print("You must be at least 18 years old to access the content.")
# #
#
# # real time interview question condition statment
# # 1)calcuate discount based on purchase amount
# # 2)wright the program to detarmine if a  persion donate blood based on thier age(18-65)
# # and weiht (above50 kg)
# # 3)calcuate driving lisance based on conditon
#
#
# # age=5
# # wight=48
# # if 18<=age<=65:
# #     if wight>=50:
# #         print("u r elg")
# #     else:
# #         print("you are age is match but wight is not match")
# # else:
# #     print("you are not elg")
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
# # a=60
# # if a >= 70:
# #     print('Distinction')
# # elif 70 > a > 55:
# #     print('1st')
# # elif 55 > a > 35:
# #     print('2nd')
# # else:
# #     print('Fail')
#
#
#
# # units = int(input("Enter electricity units consumed: "))
# # bill = units * 5  # ₹5 per unit
# #
# # if units <= 100:
# #     discount = 0
# # elif units <= 300:
# #     discount = bill * 0.10
# # else:
# #     discount = bill * 0.20
# #
# # final_bill = bill - discount
# # print(f"💡 Final Bill after discount: ₹{final_bill}")
#
#
#
# # Apply discount based on total amount.
# #
# # Rules
# #
# # ≥ 5000 → 20% discount
# #
# # ≥ 3000 → 10% discount
# #
# # Else → No discount
#
#
# # amount = 5200
# #
# # if amount >= 5000:
# #     discount = amount * 0.20
# # elif amount >= 3000:
# #     discount = amount * 0.10
# # else:
# #     discount = 0
# #
# # print("Final Amount:", amount - discount)
#
#
#
# # Calculate bonus based on experience.
# #
# # experience = 6
# # salary = 40000
# #
# # if experience >= 5:
# #     bonus = salary * 0.15
# # else:
# #     bonus = salary * 0.05
# #
# # print("Bonus:", bonus)
#
# # Check eligibility based on age, income & credit score.
# # age = 28
# # income = 35000
# # credit_score = 720
# #
# # if age >= 21 and income >= 30000 and credit_score >= 700:
# #     print("Loan Approved")
# # else:
# #     print("Loan Rejected")
#
#
#
# # Find Total & Average of Marks
# # marks = [70, 80, 90, 60, 75]
# # total = 0
# #
# # for m in marks:
# #     total += m
# #
# # average = total / len(marks)
# # print("Total:", total)
# # print("Average:", average)
#
# # Count Even & Odd Numbers
# numbers = [10, 15, 20, 25, 30]
# even = 0
# odd = 0
#
# for n in numbers:
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print("Even:", even)
# print("Odd:", odd)
#
#
#
# # 2nd largest number
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the first number: "))
# num3 = int(input("Enter the first n umber: "))
# 
# if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
#     print("The second largest number is ", num1)
# 
# elif (num2 > num3 and num2 < num1) or (num2 < num3 and num2 > num1):
#     print("The second largest number is ", num2)
# 
# elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
#     print("The second largest number is ", num3)


#
