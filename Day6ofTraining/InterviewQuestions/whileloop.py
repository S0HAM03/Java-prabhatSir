#While Loop in Python

# The while loop keeps repatating an action until an associated condition return False

#syntex
# while(condition):
#     statment

#eg1)


# for i in range(10):
#     print(i)
#

# a=1    #2   #3    #4  #5      #10  #11
# while a<=10:    #11   True     #False
#     print(a)  #1 #2   #3  #4    #10
#     a=a+1    #2     #5    #11
# print("Rest of code ")


#2While loop with else

# a=1
# while a<=4:   #True   False
#     print(a)   #1
#     a=a+1
#     print("hi")
# else:
#     print("While condition FALSE so Else Part Exacusated")
# print('Rest of the Code')

#
# Infinate conditin
# while True:
#     print("Aanugrah Education")
# print("Rest of code ")


#to avoied Infinate condition code
# i=0    #5
# while True:
#     i=i+1      #
#     print(i)    #1
#     if i==5:
#         break
# print("Rest of the code")

# nasted for loop

# i=1
# while i<=3:    #1
#     print("outer loop",i)
#     i=i+1       #2#
#     j=1
#     while j<=5:      #1
#         print("Inner loop ",j)     #1
#         j=j+1    #2
# print("Rest of the code")



