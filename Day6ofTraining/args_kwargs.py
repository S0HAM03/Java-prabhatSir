# ==========================================
# CONCEPT: *args and **kwargs
# ==========================================

# IMPORTANT REMARK: *args (Variable Length Positional Arguments)
# Allows you to pass an arbitrary number of arguments, which are packed into a tuple.
def sum_all(*numbers):
    return sum(numbers)

print("Sum of 2,3,5:", sum_all(2, 3, 5))

# IMPORTANT REMARK: **kwargs (Variable Length Keyword Arguments)
# Allows you to pass arbitrary keyword arguments, which are packed into a dictionary.
def fu(**kwargs):
    print("Keyword arguments received:", kwargs)

fu(greet="hello", name="chirag", subject="cse")
