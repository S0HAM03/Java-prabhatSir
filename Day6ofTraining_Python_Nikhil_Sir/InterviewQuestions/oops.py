# # # # # Inheritance is one of the core concepts of Object-Oriented Programming. It allows a class (child class) to inherit properties and
# # # # # methods from another class (parent class).
# # # #
# # # # # Why use Inheritance?
# # # # # Code reusability
# # # # #
# # # # # Structure and hierarchy
# # # # #
# # # # # Extending functionality without modifying the base class
# # # #
# # # #
# # # # # Basic
# # # # # Syntax in Python
# # # # #
# # class Parent:
# #     # parent class
# #     pass
#
# # # class Child(Parent):
# # #     # child class inherits from Parent
# # #     pass
# # #
# # #
# # # #
# # # # # 🔸 Example 1: Single Inheritance
# # # # # A single child class inherits from one parent class.
# # # #
# # # # # class Animal:
# # # # #     def speak(self):
# # # # #         print("Animal speaks")
# # # # #
# # # # # class Dog(Animal):
# # # # #     def bark(self):
# # # # #         print("Dog barks")
# # # # #
# # # # # d = Dog()
# # # # # d.speak()   # Inherited from Animal
# # # # # d.bark()    # Dog's own method
# # # # #
# class father():
#     def king(self):
#         print("iam king of my family")
#
#     # def dy(self):
#     #     print("DY PATIL COLLAGE ")
# class Sun(father):
#     def ni(self):
#         print("hi iam  sun ")
# d=Sun()
# d.ni()
# # # d.king()
# # class Student:
# #     def __init__(self,name):
# #         self.name=name
# #     def display(self):
# #         print(self.name)
# # class Dog:
# #     def sound(self):
# #         print("Bark")
# # class Cat:
# #     def sound(self):
# #         print("Meow")
# # dog1=Dog()
# # cat1=cat()
#
# # dog1.sound()
# # cat1.sound()
#
# # # #
# # # #
# # # # # Example
# # # # # 2: Multilevel
# # # # # Inheritance
# # # #
# # # # # A class is derived from another derived class.
# # # # #
# # # # class Animal:
# # # #     def speak(self):
# # # #         print("Animal speaks")
# # # #
# # # # class Dog(Animal):
# # # #     def bark(self):
# # # #         print("Dog barks")
# # # #
# # # # class Puppy(Dog):
# # # #     def weep(self):
# # # #         print("Puppy weeps")
# # # # # #
# # # # p = Puppy()
# # # # p.speak()
# # # # p.bark()
# # # # p.weep()
# # # # #
# # class Grandfather():
# #     def abc(self):
# #         print("i am god father")
# # class Father(Grandfather):
# #     def xyz(self):
# #         print("iam father")
# # class sun(Father):
# #     def qwe(self):
# #         print("iam sun")
# # f=sun()
# # f.abc()
# # f.xyz()
#
# # #
# # # # # Example
# # # # # 3: Multiple
# # # # # Inheritance
# # # # # # A child class inherits from more than one parent class.
# # # class Father:
# # #     def skills1(self):
# # #         print("Father paisa")
# # #
# # # class Mother:
# # #     def skills(self):
# # #         print("Mother ka paisa")
# # # class bro():
# # #     def bhai(self):
# # #         print("")
# # # class Child(Father):
# # #     def abc(self):
# # #         print("  v i am child paisa nhe hai ")
# # # ob=Child()
# # # ob.abc()
# # # ob.skills1()
# # # #
# # # # c = Ch 1()
# # # # #
# # # # # # 🔹 4. Hierarchical Inheritance
# #1
# # # # #
# # # # # 🔸 Theory:
# # # # # Multiple child classes inherit from the same parent class.
# # # #
# # # # # class Animal:
# # # # #     def speak(self):
# # # # #         print("Animal speaks")
# # # # #
# # # # # class Dog(Animal):
# # # # #     def bark(self):
# # # # #         print("Dog barks")
# # # # #
# # # # # class Cat(Animal):
# # # # #     def meow(self):
# # # # #         print("Cat meows")
# # # #
# # # # # d = Dog()
# # # # # d.speak()
# # # # # d.bark()
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # #
# # class Father():  #parent class
# #     def abc(self):
# #         print("i iam father ")
# # class Son1(Father):  # chils class
# #     def rahul(self):
# #         print("i am rahul")
# # class Son2(Father):  # child class
# #     def pratmesh(self):
# #         print("i am pratmesh ")
# # # class Son3(Father):  #  child class
# # #          def sonal(self):
# # #            print("i iam sonal")
# # # a=Son3()
# # # a .pramesh()
# # # a.abc()
# # # a.sonal()
# # # # a.pratmesh()
# # # # # b=Son2()
# # # # # b.abc()
# # # # #
# # # # # c = Cat()
# # # # # c.speak()
# # # # ## c.meow()
# # #
# # # # class father():
# # # #     def abc(self):
# # # #         print("hi iam father")
# # # # class mother():
# # # #     def xyz(self):
# # # #         print("hi iam mother")
# # # # class sun(father,mother):
# # # #     def pq(self):
# # # #         print("hi iam sun")
# # # # g=sun()
# # # # g.abc()
# # # # g.xyz()
# # # # g.pq()
# # # # #Hybrid inheritance is a combination of two or more types of inheritance
# # # # # (like single, multiple, multilevel, hierarchical).
# # # # # It represents a complex inheritance structure.
# # # #
# # # #
# # # #
# # # #
# # # # # class A:
# # # # #     def display(self):
# # # # #         print("Class A")
# # # # #
# # # # # class B(A):
# # # # #     def display_b(self):
# # # # #         print("Class B")
# # # # #
# # # # # class C(A):
# # # # #     def display_c(self):
# # # # #         print("Class C")
# # # # #
# # # # # class D(B, C):  # Hybrid inheritance
# # # # #
# # # # # # obj = D()
# # # # # obj.display()     # From Class A (inherited via B and C)
# # # # # obj.display_b()   # From Class B
# # # # # obj.display_c()   # From Class C
# # # # # obj.display_d()   # From Class D
# # # # #
# # # #
# # # #
# # # # #Polymorphism
# # # # # 🔷 What is Polymorphism?
# # # # # Polymorphism means "many forms."
# # # # # In object-oriented programming, polymorphism allows methods with
# # # # # the same name to behave differently depending on the object calling them
# # # #
# # # #
# # # # #method overloading
class Test:
    def show(self, a,b):
        print(a)

    def show(self, a):
        print(a)

t = Test()
t.show(10,20)
# # # # #
# # # #
# # # #
# # # # #Method overding
# # # # # 2. Runtime Polymorphism (Method Overriding)
# # # # # Supported in Python
# # # # #
# # # # # Achieved through inheritance
# # # # #
# # # # # A child class can override the method of the parent class
# # # #
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# # # # Using Polymorphism
# # # def make_sound(animal):
# # #     animal.speak()
# # #
# # # a = Animal()
# # # d = Dog()
# # # c = Cat()
# # # #
# # # make_sound(a)  # Animal speaks
# # # make_sound(d)  # Dog barks
# # # make_sound(c)  # Cat meows
# # #
# # # # overiding in python
# # #
# # #
# # #
# # #
# # # class A:
# # #     def nikhil(self):
# # #         print("hi   iam parent class nikhil")
# # # class B(A):
# # #     def nikhil(self):
# # # #         print("hi i am chi ld class nikhil")
# # # # ob=B()
# # # # ob.nikhil()
# # #
# # # ###super()
# # class Parent:
# #     def display(self):
# #         print("Parent display method")
# #
# # class Child(Parent):
# #     def display(self):
# #         super().display()
# #         print("Child display method")
# #
# # c = Child()
# # c.display()
# # #
# # #Bank Interest Example
# #
# # #
# class Bank:
#     def interest(self):
#         print("Bank interest is 4%")
#
# class SBI(Bank):
#     def interest(self):
#         print("SBI interest is 6%")
#
# class HDFC(Bank):
#     def interest(self):
#         print("HDFC interest is 7%")
# # #
# b1 = SBI()
# b2 = HDFC()
# # #
# # # b1.interest()
# # # b2.interest()
# #
# # # Constructor Overriding
# #
# # # class Parent:
# # #     def __init__(self):
# # #         print("Parent constructor")
# # #     def display(self):
# # #         print("Parent display method")
# # # class Child(Parent):
# # #     def __init__(self):
# # #         super().__init__()
# # #         print("Child constructor")
# # #
# # # c = Child()
# #
# #
# #
# #
# # #
# # # ################################
# # #
# # # # ✅ What is
# # # # ✅ What is Abstraction in Python?
# # # # 🔷 Definition:
# # # # Abstraction means hiding the internal implementation and
# # # # showing only essential features to the user.atures to the user.
# # #
# # #
# # # # It helps in:
# # # #
# # # # Reducing complexity
# # # #
# # # # Increasing security
# # # #
# # # # Improving modularity
# # #
# # #  # How to implement Abstraction in Python?
# # # # You must:
# # # #
# # # # Import ABC and abstractmethod from abc module
# # # #
# # # # Create a class that inherits from ABC
# # # #
# # # # Use @abstractmethod decorator to declare abstract methods
# # #
# # #
# # # # from abc import ABC, abstractmethod
# # #
# # #
# # # # Abstract class
# # # # class Vehicle(ABC):
# # #     #
# # #     # @abstractmethod
# # #     # def start(self):
# # #     #     pass
# # #
# # #
# # # # Child class 1
# # # # class Car(Vehicle):
# # # #     def start(self):
# # # #         print("Car engine started")
# # # #
# # # #
# # # # # Child class 2
# # # # class Bike(Vehicle):
# # # #     def start(self):
# # # #         print("Bike engine started")
# # # #
# # # #
# # # # # obj = Vehicle() ❌ Error: Can't instantiate abstract class
# # # # v1 = Car()
# # # # v2 = Bike()
# # # #
# # # # v1.start()
# # # # v2.start()
# # #
# # #
# # #
# # # ####Abstraction in python
# # #
# import first
#
# first.Add()
#
# # first.Sub()
# #
# # #
# # #
# # #
# # #
# # #
# # #
# # # ########Enculaption in python
# # #
# class Super():
#     def __init__(self):
#         self._value=100    #procated member
#         self.__value1=200   #private member
#         print(self.__value1)
#     def display(self):
#         print(self._value)
#         # print(self.__value1)
# class Sub(Super):
#     def show(self):
#         print(self._value)
#         # print(self.__value1)
# ob=Sub()
# ob.show()

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
# # #
# # #
# # #
# # #
# # #
# # # #palendrom example
# # # # def is_palinderom(text):
# # # #     cleared=text.replace(" ","").lower()
# # # #     return cleared==cleared[::-1]
# # # # print(is_palinderom("nikhil"))
# # # # print(is_palinderom("nayan"))
# # # # print[1,2,3.......10]
# # #
# # # # for i i t("reaming odd number")
# # #
# # #
# # #
# # # # Factorial of code using python
# # #
# # # # def factoral(n):
# # # #     result=1
# # # #     for i in range(1,n+1):
# # # #         result *=i
# # # #     return result
# # # # print(factoral(10))
# # #
# # # #mearage two dictionary into single dictionary
# # #
# # # # dict1={"nikhil":1,"avanti":2}
# # # # dect2={"pune":3,"hyd":4}
# # # #
# # # # # mearge two dict
# # # # mearged={**dict1,**dect2}
# # #
# # # # print(mearged)
# # #
# # # ##using update
# # #
# # # # dict1.update(dect2)
# # # # print(dict1)
# # #
# # #
# # #
# # # #remove the duplicate value in the list
# # #
# # # # def remove_duplicate(lst):
# # # #     unique=[]
# # # #     for item in lst:
# # # #         if item not in unique:
# # # #             unique.append(item)
# # # #     return unique
# # # # print(remove_duplicate([1, 2, 2, 3, 4, 4]))
# # #
