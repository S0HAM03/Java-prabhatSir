# # # # # Threading is a way to run multiple operations concurrently in
# # # # # the same program.
# # # # # single tread(main thread by default_exacute to program )
# # # # #
from time import sleep
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(3):
            print("nikhil")
            sleep(3)
#
class B(Thread):
    def run(self):
        for i in range(3):
            print("avanti")
            sleep(3)

# Create thread objects
t1 = A()
t2 = B()

# Start threads
t1.start()
t2.start()
# #
# # # Wait for both threads to complete
# t1.join()
# t2.join()
# # # # # # #
# # # #
# # def nik():
# #     for i in range(3):
# #         print("nikhil")
# # def ava():
# #     for i in range(3):
# #         print("avanti")
# # nik()
# # ava()
# #
# # # import threading
# # # def task1():
# # #     for i in range(5):
# # #         print("Task1",i)
# # # def task2():
# # #     for i in range(5):
# # #         print('Task2',i)
# # # t1=threading.Thread(target=task1)
# # # t2=threading.Thread(target=task2)
# # # t1.start()
# # # t2.start()
# # # t1.join()
# # # t2.join()
# #
# # # import threading
# # # import time
# # #
# # # def print_numbers():
# # #     for i in range(1, 6):
# # #         print("Number:", i)
# # #         time.sleep(1)
# # #
# # # def print_letters():
# # #     for ch in ['A', 'B', 'C', 'D', 'E']:
# # #         print("Letter:", ch)
# # #         time.sleep(1)
# # # #
# # # # Create threads
# # # t1 = threading.Thread(target=print_numbers)
# #
# # # t2 = threading.Thread(target=print_letters)
# #
# # # # Start threads
# # # t1.start()
# # # t2.start()
# # #
# # # # # Wait for both threads to complete
# # # t1.join()
# # # t2.join()
# # # # # #
# # # print("Done with both threads!")
# #
# # # import threading
# # # import time
# # #
# # # def task1():
# # #     for i in range(3):
# # #         print("Task 1 running")
# # #         time.sleep(4)
# # #
# # # def task2():
# # #     for i in range(3):
# # #         print("Task 2 running")
# # #         time.sleep(4)
# # #
# # # # Create threads
# # # t1 = threading.Thread(target=task1)
# # # t2 = threading.Thread(target=task2)
# # #
# # # # Start threads
# # # t1.start()
# # # t2.start()
# # #
# # # # Wait for both threads to finish
# # # t1.join()
# # # t2.join()
# # #
# # # print("Both tasks completed")
# #
# # # import threading
# # # #
# # # def display(name):
# # #     print("Hello", name)
# # #
# # # t1 = threading.Thread(target=disaplay, args=("Nikhil",))
# # # t2 = threading.Thread(target=display, args=("Python",))
# # #
# # # t1.start()
# # # t2.start()
# # # ob=display()
# #
