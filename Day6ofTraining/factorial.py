# ==========================================
# CONCEPT: Factorial Calculation (Fixed Logic)
# ==========================================

# IMPORTANT REMARK: The previous code had a logic bug (num = i * i-1).
# We fixed it by using a proper multiplier accumulator variable 'result'.

def fact(num):
    result = 1
    i = num
    while i > 1:
       result = result * i
       i = i - 1
    print(f"Factorial of {num} is: {result}")

fact(6)
