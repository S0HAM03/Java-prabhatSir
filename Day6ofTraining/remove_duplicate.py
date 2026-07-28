# ==========================================
# CONCEPT: Removing Duplicates from a List
# ==========================================

# IMPORTANT REMARK: Manual Duplicate Removal
# Here we remove duplicates without using Python's built-in set() function.
# We iterate through the list and only append items that are not already in our 'unique' list.

def remove_duplicate(input_list):
    unique = []
    for item in input_list:
        if item not in unique:
            unique.append(item)
    return unique   

a = [2, 2, 4, 6, 6, 8, 8, 'hi']
print("Original:", a)
print("Unique:", remove_duplicate(a))
