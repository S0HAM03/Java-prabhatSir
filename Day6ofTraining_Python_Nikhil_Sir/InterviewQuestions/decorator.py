# # # def my_decorator(hello):   ##new function
# # #     def wrapper():
# # #         print("Before function")
# # #         hello()
# # #         print("After function")
# # #     return wrapper
# # # @my_decorator
# # # def hello(): ##original function
# # #     print("Hello World")
# # # hello()
# # # # #
# # # # #
# # # # # # # #
# #
# def my_deco(say_hello):
#     def wrapper():
#         print("befor cal ling hello")
#         say_hello()
#         print("after calling hello")
#     return wrapper
# @my_deco
# # # # # # # # #
# # # # # # # # #
# def say_hello():  #original code or function
# 
#     print("Hello Team")
# say_hello()
# # # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
def to_upper(greet):
         def wrapper():
            result = greet()
            print(result.upper())
         return wrapper
@to_upper
def greet():
  return "hello world"
print(greet())
# # # # #
# # # #
# # # # # # #
# # # # # def second_deco(say_hello):
# # # # #     def wrapper():
# # # # #         print("=== Extra functionality added ===")
# # # # #         say_hello()
# # # # #         print("=== End of extra functionality ===")
# # # # #     return wrapper
# # # # #
# # # # # @second_deco       # This will run first
# # # # # @my_deco           # Then this one will wrap
# # # # # def say_hello():   # original function
# # # # #     print("Hello Team")
# # # # # #
# # # # # say_hello()
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # # def xyz(nikhil):
# # # # # # # #     def zxc(*args,**kwargs):
# # # # # # # #         print("")
# # # # # # # #
# # # # # # # # def nikhil(abc):
# # # # # # # #     print(abc)
# # # # # # # # nikhil("rmd collage")
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # lower case to upper case  ###
# # def upper_case_decorator(greet):
# #     def wrapper():
# #         result = greet()              # call original function
# #         modified = result.upper()    # convert to uppercase
# #         return modified
# #     return wrapper
# # @upper_case_decorator
# # def greet():
# #     return "hello team, welcome to django class"
# # print(greet())
# # # #
# # # #
# # # # # ###addition of two number using deco
def add_decorator(func):
    def wrapper(a, b):
        print("Before performing addition")
        result = func(a, b)        # call original function
        print("After performing addition")
        return result
    return wrapper
# #
@add_decorator
def add_numbers(x, y):
    return x + y
# # # #
# # # # # Test
print("Result:", add_numbers(5, 7))
# # # # #
# # # # # #
# # # # #
# # # # # ####Imagine a dashboard in a website. Only logged-in users should access it.
# # # # We can use a decorator to check authe ntication before showing the dashboard
# # # def login_required(func):
# # #     def wrapper(user):
# # #         if not user.get("is_logged_in"):   # check login
# # #             print("Access Denied! Please log in.")
# # #             return None
# # #         return func(user)   # call original function
# # #     return wrapper
# # # @login_required
# # # def dashboard(user):
# # #     print("Welcome " + user["name"] + " to your dashboard!")
# # # # Test Cases
# # # user1 = {"name": "Nikhil", "is_logged_in": True}
# # # user2 = {"name": "Guest", "is_logged_in": False}
# # # dashboard(user1)   # logged in
# # # dashboard(user2)   # not logged in
# # # #
