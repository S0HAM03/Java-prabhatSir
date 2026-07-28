# ==========================================
# CONCEPT: Variable Swapping (Pythonic Way)
# ==========================================

# IMPORTANT REMARK: Tuple Unpacking
# In Python, you do not need a temporary variable to swap values!
# You can swap them directly on a single line using tuple unpacking.

a = 10
b = 20
print(f"Before: a={a}, b={b}")

a, b = b, a

print(f"After:  a={a}, b={b}")
