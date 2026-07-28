# # #🔹 What is a Generator in Python?
# #
# # A generator is a special type of function that allows you to generate values one at a time instead of returning them all at once.
# #
# # Instead of return, we use the yield keyword.
# #
# # They are memory efficient (don’t store everything in memory, generate values on demand).
# #
# # 🔹 Why use Generators?
# #
# # ✅ Saves memory → useful for large datasets.
# # ✅ Faster execution for streaming data.
# # ✅ Easy to implement iterators.
#
#
#
# #1
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

# print(list(even_numbers(10)))
g=even_numbers(10)
print(next(g))
print(next(g))
print(next(g))

# # print(n)
# # # print(next())
# # [0, 2, 4, 6, 8, 10]
#
# #####iterview Q’s Around Generators
# #
# # Difference between iterator and generator?
# #
# # Why use yield instead of ret urn?
# #
# # How do generators improve performance & memory?
# #
# # Can you write a generator for prime numbers?
# #
# # Explain generator expressions vs list comprehensions.
# # normal square function
# def square():
#     a=4
#     return a*a
# n = square()
# print(n)
# def squares(n):
#     for i in range(1, n+1):
#         yield i * i
#
# gen = squares(5)
# print(next(gen))  # 1
# print(next(gen))  # 4
# print(next(gen))
# # print(next(gen))
# # print(next(gen))
#
# # def square(n):
# #     for i in range(1,n+1):
# #         return n*n
# # print(square(5))
#
# # for i in range(10):
# #     print(i,end="")