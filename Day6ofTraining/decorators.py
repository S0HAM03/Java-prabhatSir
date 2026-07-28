# ==========================================
# CONCEPT: Python Decorators (Fixed Logic)
# ==========================================

# IMPORTANT REMARK: Decorators
# A decorator wraps a function, modifying its behavior before or after execution.

# Basic Decorator
def my_deco(func):
    def wrapper():
        print("--- before ---")
        func()
        print("--- after ---")
    return wrapper   

@my_deco
def hello():
    print("Hello World")

hello()          

# Decorator that modifies the return value
def to_upper(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper    

@to_upper
def greet():
    return "Hello"

print("Modified greeting:", greet())

# Decorator that adds values returned from a function
# IMPORTANT REMARK: Fixed the bug where the decorator was trying to access undefined variables a and b.
# It now unpacks the return values from the function correctly!
def to_add(func):
    def wrapper():
        a, b = func()
        result = a + b
        return result
    return wrapper    

@to_add
def get_numbers():
    a = 10
    b = 20
    return a, b 

print("Addition via decorator:", get_numbers())
