# # # ####. What is DSA?
# # #
# # # # Data Structure → A way to store and organize data.
# # # # Example: List, Stack, Queue.
# # # #
# # # # Algorithm → A step-by-step procedure to solve a problem.
# # # # Example: Searching for a number in a list, sorting numbers.
# # # #
# # # # 👉 DSA = Data Structures + Algorithms
# # #
# # # ####2. Arrays / Lists
# # #
# # # # Array = collection of elements in continuous memory.
# # # #
# # # # In Python, we use lists instead of arrays.
# # # #
# # # # Example:
# # arr = [10, 20, 30, 40, 50,60,70]
# # #
# # # # print("First element:", arr[0])
# # # # arr.append(60)         # add
# # # # arr.remove(30)         # delete
# # # # print("Updated list:", arr)
# # #   #1 D array:
# # #
# # # # a=[1,2,3,4,5]
# # # #find length of array
# # # #size(a)=u-l+1
# # #
# # # # 2. 1D Array
# # # #
# # # # A 1D array is like a single row of elements.
# # # #
# # # # Example: Marks of 5 students [85, 90, 78, 92, 88]
# # #
# # # # 2D Array → table/matrix (list of lists).
# # # # #
# # matrix=[
# #     [1,2,3,4],
# #     [5,6,7,9],
# #     [10,11,12]
# # ]
# # #accessing element of 2 d array
# # # print(matrix[0][1])
# #
# # matrix[1][2]=44
# # print(matrix)
# # # # Access elements → [row][col]
# # #
# # # # 1D Array (using list)
# # # # marks = [85, 90, 78, 92, 88]
# # # #
# # # # print("First element:", marks[0])
# # # # print("Last element:", marks[-1])
# # # #
# # # # # Traversing
# # # # for m in marks:
# # # #     print(m, end=" ")
# # # #
# # # # # Updating
# # # # marks[2] = 80
# # # # print("\nUpdated marks:", marks)
# # #
# # # ###2D Array
# # # # 2D Array
# # # #
# # # # A 2D array is like a matrix with rows and columns.
# # # #
# # # # Example: Marks of 3 students in 3 subjects.
# # # #
# # # #
# # # # 2D Array (list of lists)
# # # # marks = [
# # # #     [85, 90, 78],   # student 1
# # # #     [88, 92, 80],   # student 2
# # # #     [75, 85, 89]    # student 3
# # # # ]
# # # #
# # # # print("Marks of Student 1 in Subject 2:", marks[1][1])
# # # #
# # # # # Traversing 2D array
# # # # for row in marks:
# # # #     for val in row:
# # # #         print(val, end=" ")
# # # #     print()  # new line for each row
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # sum of all elemnt in 2 d array
matrix=[
    [1,2,3,4],
    [5,6,7,9],
    [10,11,12]
]
total=0
for row in matrix:
    for num in row:
        total+=num
print(total)
#
#
# # #
# # #
# # # # 3. Strings
# # # #
#
# # # # A string is a sequence of characters.
# # # #
# # # # Strings are immutable (cannot be changed directly).
# # # #
# # # # Example:
# # #
# # # # s = "hello"
# # # # print("Length:", len(s))
# # # # print("Reverse:", s[::-1])  # slicing
# # # # print("Is palindrome?", s == s[::-1])
# # # #
# # # # 4. Stack (LIFO – Last In First Out)
# # # #
# # # # Last item added → first one removed.
# # # #
# # # # Used in Undo/Redo, Back button in browser.
# # #
# # #
# # # #stack operaton
# # # #list implemenation of stack
# # # #
# st=[]
# st.append(8)
# st.append("nikhil")
# st.append(20.5)
# st.append(6)
# st.append(True)
# print(st)
# st.pop()#remove last element (last in first out)
# print(st)
# # #
# # #
# # # #PEEK / TOP OPERATION
# # #
# # # # Returns the top element without removing it
# # # #
# # # # Access last element using index -1
# # # # if len(st) == 0:
# # # #     print("Stack is empty")
# # # # else:
# # # #     print("Top element:", st[-1])
# # #
# # # #5isEmpty OPERATION
# # #
# # # # Checks whether stack is empty
# # # #
# # # # If length is zero → empty
# # #
# # # # if len(st) == 0:
# # # #     print("Stack is Empty")
# # # # else:
# # # #     print("Stack is Not Empty")
# # #
# # #
# # # # Example:
# # # #
# #________________________
# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print("Stack:", stack)
# # # # #
# print("Pop:", stack.pop())   # removes last
# print("Stack after pop:", stack)
# #_________________________________________
#
# # # #2)# stack=[]
# # # # stack.append(10)
# # # # stack.append(20)
# # # # stack.append(30)
# # # # print(stack)
# # # # print(stack.pop())
# # # # print(stack)
# # # # print(stack.pop())
# # #
# # # # class stack:
# # # #     def __init__(self):
# # # #         self.value=[]
# # # #     def push(self,x):
# # # #         self.value=[x]+self.value
# # # #     def pop(self):
# # # #         return self.value.pop(0)
# # # # s=stack()
# # # # s.push(10)
# # # # s.push(20)
# # # # s.push(30)
# # # # print(s.value)
# # # # s.pop()
# # # # print(s.value)
# # #
# # #
# # # # Output:
# # # #
# # # # Stack: [1, 2, 3]
# # # # Pop: 3
# # # # # Stack after pop: [1, 2]
# # #
# # #
# # #
# # # # stack = []##add element in list using input int
# # # # n = int(input("Enter number of elements: "))
# # # #
# # # # for i in range(n):
# # # #     num = int(input("Enter number: "))
# # # #     stack.append(num)
# # # #
# # # # print("Stack:", stack)
# # #
# # #
# # # # 5. Queue (FIFO – First In First Out)
# # # #
# # # # First item added → first one removed.
# # # #
# # # # Used in Ticket booking system, Print queue.
# # # #
# # # # Example:
# # #
# # # ##using list of queue
# # # # class queue:
# # # #     def __init__(self):
# # # #         self.value=[]
# # # #     def en(self,x):
# # # #         self.value.append(x)
# # # #     def deque(self):
# # # #         front=self.value[0]
# # # #         self.value=self.value[1:]
# # # #         return front
# # # # q1=queue()
# # # # q1.en(10)
# # # # q1.en(20)
# # # # q1.en(30)
# # # # q1.en(40)
# # # # print(q1.value)
# # # # print(q1.deque())
# # # # print(q1.value)
# # # # from collections import deque
# # #
# # # # queue = deque()
# # # #
# # # # queue.append(1)
# # # # queue.append(2)
# # # # queue.append(3)
# # # # print("Queue:", queue)
# # # #
# # # # print("Pop left:", queue.popleft())   # removes first
# # # # print("Queue after pop:", queue)
# # #
# # #
# # # # Output:
# # # #
# # # # Queue: deque([1, 2, 3])
# # # # Pop left: 1
# # # # Queue after pop: deque([2, 3])
# # #
#
#
#
# from collections import deque
# queue=deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# queue.popleft()
# print(queue)
# # # # 6. Searching
# # #
# # #
# # # # Linear Search → check one by one.
# # #
# # # # Binary Search → check middle (works on sorted list).
# # # #
# # # # Example (Linear Search):
# # # #
# # # # arrak
# # #
# # #
# # #
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index
    return -1

# Example usage
nums = [10, 25, 30, 45, 50]
print(linear_search(nums, 30))  # Output: 2
# # # # print(linear_search(nums, 100)) # Ou
# # #
# # #
# # count occurrence using liner search
#
# def count_occ(arr,target):
#     count=0
#     for num in arr:
#         if num==target:
#             count+=1
#     return count
# number=[10,20,20,30,30,40]
# print(count_occ(number,20))
#
# def count_occ(arr,target):
#     count=0
#     for num in arr:
#         if num.startwith(target):
#             count+=1
#     return count
# target=[hi,hello,hi,hello,ok,ok]
# print(count_occ(target,h))
#
# # # ##binary serach
# # # def binary_search(arr, target):
# # #     low, high = 0, len(arr) - 1  # Start with first index (0) and last index (n-1)
# # #
# # #     while low <= high:  # Continue until search space is valid
# # #         mid = (low + high) // 2  # Find the middle index (integer division)
# # #
# # #         # Case 1: Target is found
# # #         if arr[mid] == target:
# # #             return mid  # Return index of target
# # #
# # #         # Case 2: Target is greater than middle element
# # #         elif arr[mid] < target:
# # #             low = mid + 1  # Ignore left half, search in right half
# # # #
# # #         # Case 3: Target is smaller than middle element
# # #         else:
# # #             high = mid - 1  # Ignore right half, search in left half
# # #
# # #     return -1  # Target not found
# #
# #
# def bin(arr,target):   #[10,20,30,40,50]
#   left,wright=0,len(arr)-1
#   while left<wright:
#       mid=(left+wright)//2
#       if arr[mid]==target:
#           return mid
#       elif arr[mid]<target:
#           left=mid+1
#       else:
#           wright=mid-1
#   return -1
# arr=[10,20,30,40,50]
# target=40
# print(bin(arr,target))
#
# # # 7. Sorting
# #
# # # Bubble Sort → repeatedly swap adjacent elements.
# #
# # # Example:
# #
# # # arr = [5, 2, 8, 1]
# # #
# # # for i in range(len(arr)):
# # #     for j in range(len(arr)-i-1):
# # #         if arr[j] > arr[j+1]:
# # #             arr[j], arr[j+1] = arr[j+1], arr[j]
# # #
# # # print("Sorted:", arr)
# #
# #
# # # ✅ Summary for Students
# #
# # # Lists/Arrays → store elements
# # #
# # # Strings → sequence of characters
# # #
# # # Stack → LIFO (last in, first out)
# # #
# # # Queue → FIFO (first in, first out)
# # #
# # # Searching → find elements
# # #
# # # Sorting → arrange in order
# #
# #
# #
# # ###DAY 2
# # # Recursion
# # #
# # # Definition: A function that calls itself to solve a problem.
# #
# # # Useful for: factorial, Fibonacci, tree traversal.
# # #
# # # Example – Factorial (Recursion):
# # #
# # # def factorial(n):
# # #     if n == 0 or n == 1:   # base case
# # #         return 1
# # #     return n * factorial(n - 1)  # recursive call
# # #
# # # print("Factorial of 5:", factorial(5))
# #
# #
# # # Hashing (Python Dictionary)
# # #
# # # Hashing = technique to map keys to values for fast lookup.
# # #
# # # In Python, dict is implemented as a Hash Table.
# # #
# # # Example:
# # #
# # # # Dictionary (Hash Map)
# # # student = {
# # #     "id": 101,
# # #     "name": "Nikhil",
# # #     "marks": 85
# # # }
# # #
# # # print("Student Name:", student["name"])
# # # student["marks"] = 90  # update
# # # print("Updated dict:", student)
# # #
# # # # Searching
# # # if "id" in student:
# # #     print("ID exists:", student["id"])
# # #
# # #
# # # Output:
# # #
# # # Student Name: Nikhil
# # # Updated dict: {'id': 101, 'name': 'Nikhil', 'marks': 90}
# # # ID exists: 101
# # #
# # #
# # # 👉 Compare dictionary search (O(1)) vs linear search (O(n) in list).
# # #
# # # 4. Real-Life Examples for Students
# # #
# # # Recursion → folder explorer in Windows (each folder contains subfolders).
# # #
# # # Linked List → train coaches connected one by one.
# # #
# # # Hashing → contact list in phone (name → phone number).
# #
# #
# # ##bubble sorting
# # # def bubble_sort(arr):
# # #     n = len(arr)
# # #     for i in range(n):   # repeat n times
# # #         for j in range(0, n - i - 1):  # last i elements are already sorted
# # #
# # #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
# # #     return arr
# # #
# # # nums = [64, 34,  25, 12, 22, 11, 90]
# # # print(bubble_sort(nums))
# # # Output: [11, 12, 22, 25, 34, 64, 90]
# #
# # # def bubble_sort_dict(prices_dict):
# # #     # Extract prices into a list
# # #     prices = list(prices_dict.values())
# # #     n = len(prices)
# # #
# # #     # Bubble Sort
# # #     for i in range(n):
# # #         for j in range(0, n - i - 1):
# # #             if prices[j] > prices[j + 1]:
# # #                 prices[j], prices[j + 1] = prices[j + 1], prices[j]
# # #
# # #     return prices
# #
# #
# # # Dictionary of product prices
# # # shop_prices = {
# # #     "Shoes": 250,
# # #     "Shirt": 100,
# # #     "Cap": 75,
# # #     "Watch": 300,
# # #     "Jeans": 150
# # # }
# # #
# # # print("Sorted Prices:", bubble_sort_dict(shop_prices))
# #
# # #   Tree
# #
# class Node:  #(first create Node)   #node under total 3 part 1) left,data,right
#     def __init__(self,data):
#         self.left=None
#         self.right=None
#         self.data=data
#     def show(self):
#         if self.left:
#             self.left.show()  ##left side data show
#         print(self.data)# print node
#         if self.right:
#             self.right.show()   #data is empty so thats reasion 100 show only
# root=Node(100)
# root.show()
# #
# r_left=Node(102)
# r_right=Node(104)
# # #
# root.left=r_left
# root.right=r_right
# root.show()
# #
# # #add the 50 value in
# # #
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
# #
#     def inorder(self):
#         if self.left:
#             self.left.inorder()
#         print(self.data, end=" ")
#         if self.right:
#             self.right.inorder()
# # # # #
# # # # #
# root = Node(100)
# # root.inorder()
# r_left = Node(102)
# r_right = Node(104)
#
# root.left = r_left
# root.right = r_right
# root.inorder()
# # #
# # # # Add 50
# # # r_left.left = Node(50)
# # # r_right.right=Node(105)
# #
# root.inorder()
#
# #
# #
# # #Binary tree path
# #
# #
# #
# # #Graph-
# # # A Graph is a non-linear data structure used to represent connections between different elements.
# # #
# # # A graph consists of:
# # #
# # # Vertices (Nodes) → Points (A, B, C)
# # #
# # # Edges → Connections between nodes
# #
# #
# # class vertex:
# #     def __init__(self,name):#inatialse vertex and pass vertex name
# #         self.name=name # applay vertex name
# #         self.connection=[]  #store the connection of vertex(1to 2,2to3...etc) coonetion means edge
# #
# #         #create edge function
# #         def add_edge(self,obje):   #appaly age object
# #             self.connection.append(obje)
# #
# # class Edge:
# #     def __init__(self): #no name of edge
# #         self.connection=[]
# #
# #     def add_edge(self,from_ver,to_ver):  #edge are conntied fron 1 to 2,2 to 3..etc
# #         self.connection.append(from_ver.name)  #inforamtion are two stoed of two vertix
# #         self .connection.append(to_ver.name)
# # # #
# # # ##creta a graph
# # #
# # # class Graph: #add vertices in graph (1,2,3,4)
# # #     def __init__(self):
# # #         self.graph={}
# # #
# # #     def add_vertices(self,obj):#pass the obj of vertex and add in graph
# # #         self.graph.update({obj.name:obj.connection})
# # #
# # # v1=vertex("1")
# # # v2=vertex("2")
# # # v3=vertex("3")
# # # v4=vertex("4")
# # #
# # # e1=Edge
# # # e1.add_edge(v1,v2)
# # #
# # # e2=Edge
# # # e1.add_edge(v1,v3)
# # #
# # # e3=Edge
# # # e1.add_edge(v1,v3)
# # #
# # # e4=Edge
# # # e1.add_edge(v2,v3)
# # #
# # # e5=Edge
# # # e1.add_edge(v4,v1)
# # #
# # # ##connection(connect) from vertec to edges
# # # v1.add_edge(e1.connection)
# # # v2.add_edge(e2.connection)
# # #
# # # v2.add_edge(e3.connection)
# # # v3.add_edge(e4.connection)
# # # v4.add_edge(e5.coonction)
# # #
# # # # all structure add in empty graph
# # #
# # # g1=Graph()
# # #
# # # g1.add_vertices(v1)#addall vertices
# # # g1.add_vertices(v2)
# # # g1.add_vertices(v3)
# # # g1.add_vertices(v4)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # Create Vertex class
# class Vertex:
#     def __init__(self, name):
#         self.name = name
#         self.connections = []   # store connected vertices
#
#     def add_edge(self, vertex_obj):
#         self.connections.append(vertex_obj.name)
#
#
# # Create Edge class
# class Edge:
#     def __init__(self, from_vertex, to_vertex):
#         self.from_vertex = from_vertex
#         self.to_vertex = to_vertex
#
#     def connect(self):
#         # Connect from -> to
#         self.from_vertex.add_edge(self.to_vertex)
#
#
# # Create Graph class
# class Graph:
#     def __init__(self):
#         self.graph = {}
#
#     def add_vertex(self, vertex_obj):
#         self.graph[vertex_obj.name] = vertex_obj.connections
#
#     def display(self):
#         for vertex in self.graph:
#             print(vertex, "->", self.graph[vertex])
#
#
# # Create Vertices
# v1 = Vertex("1")
# v2 = Vertex("2")
# v3 = Vertex("3")
# v4 = Vertex("4")
#
# # Create Edges
# e1 = Edge(v1, v2)
# e2 = Edge(v1, v3)
# e3 = Edge(v2, v3)
# e4 = Edge(v4, v1)
#
# # Connect Edges
# e1.connect()
# e2.connect()
# e3.connect()
# e4.connect()
#
# # Create Graph
# g1 = Graph()
#
# g1.add_vertex(v1)
# g1.add_vertex(v2)
# g1.add_vertex(v3)
# g1.add_vertex(v4)
#
# # Display Graph
# g1.display()
#
