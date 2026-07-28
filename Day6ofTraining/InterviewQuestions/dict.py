# # # A dictionary in Python is a collection of key-value pairs,
# # # where each key is unique, and the values can be of any data type.
# # # It is an ordered collection,
# # # meaning the order of the items is not guaranteed to be preserved.
# # #
# # # Creating a Dictionary
# # # A dictionary is created using curly b1races {},
# # # with key-value pairs sepa rated by colons
# #
# # my={1:"sham",2:'ravi',3:"aanugrah",4:"ravi"}
# # # print(my)
# #
# # # # Example of a dictionary
# # # my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# # # print(my_dict)
# #
# # #
# # # #mthods of dict
# # #
# # # # 1. Accessing Values
# # #
# # my_dict = {'name': 'John ', 'age': 30, 'city': 'New York'}
# # print(my_dict['name'])
# # print(my_dict['age'])
# #
# # # #2. Adding or Updating Items
# # # # To add a new        key-value p air or update an existing value,
# # # # simply assign the value to the key.
# # #
# # # #3 Adding a new item
# # #
# # my_dict = {'name': 'John ', 'age': 30, 'city': 'New York'}
# # my_dict['abc'] = "DYPATIL123"
# # print(my_dict)
# # #
# # #
# # # # a={1,}
# # # # print(type(a))
# # #
# # # # a=set()
# # # # print(type(a))
# # #
# # # #4Updating an existing item
# my_dict = {'name': 'John ', 'age': 30, 'city': 'New York'}
# my_dict['age'] = 31
# print(my_dict)
# # #
# # # # 5 Removing Items
# # # You can remove items using the del keyword or the pop() method.
# # # Using del to remove a key-value pair
# # my_dict = {'name': 'John ', 'age': 30, 'city': 'New York'}
# # del my_dict['ci']
# # print(my_dict)
# # #
# # # # Using pop() to remove an item and get its value
# # # age = my_dict.pop('age')  # Removes 'age' and returns its value
# # # print(age)
# # # #6 Checking if a Key Exists
# # # # You can check if a key exists in the dictionary using the in keyword.
# # #
# # # # Check if key 'name' exists
# # # # if 'name' in my_dict:
# # # #     print("Name exists")
# # #
# # #
# # # #5. Getting Keys, Values, and Items
# # # # Keys: Get a list of all keys.
# # # # Values: Get a list of all values.
# # # # Items: Get a list of all key-value pairs.
# # #
# # #
# # # # # store multipal value in dict
# # my_dict = {'name': 'John ', 'age': 30, 'city': 'New York'}
# # my_dict={1:["nikhil","solapur"] ,2:"it"}
# # items1 = my_dict.items()
# # # ii                                                                                           print(items1)
# # # print(my_dict)
# # #
# # # # my_dict = {'name': 'Aanugrah', 'age': 30, 'city': 'pune'}
# # # # Get all keys
# # # #
# # #
# # # # Get all values
# # # # value valu   es1)
# # #
# # # # Get all key-value pairs
# # # # items1 = my_dict.items()
# # # # print(items1)
# # #
# # # # print(k)   # Output: dict_keys(['name', 'age', 'email'])
# # # # print(values) # Output: dict_values(['John', 31, 'john@example.com'])
# # # # print(items)  # Output: dict_items([('name', 'John'), ('age', 31), ('email', 'john@example.com')])
# # #
# # #
# # #
# # #
# # #
# # # # 6. Clearing All Items
# # # # To remove all items from the dictionary, use the clear() method.
# # # #
# # # # my_dict.clear()
# # # # print(my_dict)  # Output: {}
# # #
# # #
# # #
# # # # 8. Merging Dictionaries
# # # # To merge two dictionaries, you can use the update() method.
# # #
# # # dict1 = {'name': 'John'}
# # # dict2 = {'age': 31}
# # # #
# # # dict1.update(dict2)  # dict1 now contains both name and
# # # print(dict1)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # 9. Nested Dictionaries
# # # # You can have dictionaries inside other dictionaries (nested dictionaries).
# # #
# nested_dict = {
#     'person': {'name': 'John', 'age': 31},
#     'address': {'city': 'New York', 'zip': '1001'}
# }
# print(nested_dict)
# # #
# # # c=nested_dict['person']['age']
# # # d=nested_dict['address']['zip']
# # # print(c)
# # # # print(d)
# # #
# # # # Getting Default Values
# # # # Use get() to access a value and avoid KeyError. If the key doesn’t exist, it returns None (or a default value if provided).
# # # # a={'ni':"nikhil","av":"avanti"}
# # # # my_dict = {'name': 'Aanugrah', 'age': 30, 'city': 'pune'}
# # # # name = my_dict.get('name', 'Unknown')
# # # # If 'name' doesn't exist, returns 'Unknown'
# # # # na=my_dict.get("na")
# # # # print(na)
# # # # print(name)
# # #
# # #
# # # # print(my_dict['na']) # get the error if name key is not present that time show error
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # Create a dictionary
# # # # my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# # # #
# # # # # Access a value
# # # # print(my_dict['name'])  # Output: John
# # # #
# # # # # Add or update items
# # # # my_dict['email'] = 'john@example.com'
# # # # my_dict['age'] = 31
# # # #
# # # # # Remove an item
# # # # del my_dict['city']
# # # #
# # # # # Pop an item
# # # # email = my_dict.pop('email')
# # # #
# # # # # Check if key exists
# # # # print('age' in my_dict)  # Output: True
# # # #
# # # # # Get keys, values, and items
# # # # print(my_dict.keys())    # Output: dict_keys(['name', 'age'])
# # # # print(my_dict.values())  # Output: dict_values(['John', 31])
# # # # print(my_dict.items())   # Output: dict_items([('name', 'John'), ('age', 31)])
# # #
# # # # Clear all items
# # # # my_dict.clear()
# # # # print(my_dict)  # Output: {}
# # # #
# # # # # Copy a dictionary
# # # # original_dict = {'name': 'John'}
# # # # copied_dict = original_dict.copy()
# # # # print(copied_dict)  # Output: {'name': 'John'}
# # #
# # # # Merge dictionaries
# # # # dict1 dict1)  # Output: {'a': 1, 'b': 2}
# # # #
# # # # # Nested dictionary
# # # # nested_dict = {'person': {'name': 'John', 'age': 31}, 'address': {'city': 'New York'}}
# # # # print(nested_dict['person']['name'])  # Output: John
# # # #
# # # # # Dictionary comprehension
# # squared_dict = {x: x**2 for x in range(1,5)}
# dict = {"a":2, "b":3, "c":4}
# #
# for key in dict:
#     dict[key] **= 2
#
# print(dict)

dict_comp = {k:k for k in range(0,10) if k<=4}
print(dict_comp)


# #
# # print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# # #
# # #########probleams################
# # # Login Authentication System
# # #
# # # Scenario: Verify username & password.
# #
# # # users  ogin fail")
# #
# # # Employee Salary Increment
# # #
# # # Scenario: Increase salary by 10%.
# #
# #
# salary = {"A": 30000, "B": 40000}
#
# for emp in salary:
#     salary[emp] += salary[emp] * 0.10
#
# print(salary)
# #
# #
# # # Shopping Cart
# # # culate total bill.
# #
# cart = {"Laptop": 50000, "Mouse": 500}
# #
# #
# #
# #
# # # print(sum(cart.values()))
# #
# # # students = [("Amit", "CS"), ("Sneha", "IT")]
# # # dept = {}
# # #
# # # for name, d in students:
# # #     dept.setdefault(d, []).append(name)
# # #
# # # print(dept)
# #
# # # Inventory Management
# # #
# # # Scenario: Update stock after sale.
# #
# # # stock = {"Pen": 20}
# # # sold = {"Pen": 5}
# #
# # #
# # # for k in sold:
# # #     stock[k] -= sold[k]
# #
# # # print(stock)
# #
