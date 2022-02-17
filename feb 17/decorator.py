# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"you are calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def greet():
#     return "hello world"
#
# @log
# def greeting(name):
#     return f"hello {name}"
#
# @log
# def add(a, b):
#     return a+b

# print(greet())
# print()
# print(greeting("debashis"))
# print()
# print(add(5, 6))

''' reverse decorator '''

# def rev(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, str):
#             return res[::-1]
#         return res
#     return wrapper
#
#
# @rev
# def greet():
#     return "hello world"
#
# @rev
# def greeting(name):
#     return f"hello {name}"

# print(greet())
# print()
# print(greeting("debashis"))
import time

''' convert in to positive if it isnot float and int then return it as it is '''

# def positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, (float, int)):
#             return abs(res)
#         return res
#     return wrapper

# @positive
# def add_(a, b):
#     return a + b
#
# print(add_(-9, 3))
# @positive
# def greet():
#     return "hello world"
# print(greet())

'''  time decorator '''

from time import time, sleep

# def _time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         res = func(*args, **kwargs)
#         end = time()
#         print(f"execution time of function is {func.__name__} is {end - start}")
#
#         return res
#     return wrapper
#
# @_time
# def add(a, b):
#     sleep(5)
#     return a+b
#
# print(add(5,5))


''' func count decorator '''
from collections import defaultdict
count = defaultdict(int)


# def count_(func):
#     def wrapper(*args, **kwargs):
#         count[func.__name__] += 1
#         return func(*args, **kwargs)
#     return wrapper
#
#
#
#
# @count_
# def greet():
#     return "hello world"
#
# @count_
# def add(a, b):
#     return a+b
#
# @count_
# def sub(a, b):
#     return a-b
# def greeting(name):
#     return f"hello {name}"
#
#
# print(add(1,2))
# print(add(1,2))
# print(add(1,2))
# print(add(1,2))
# print(add(1,2))
# print(count)




# def count_(func):
#     func.c = 0            # greet.c = 0
#     def wrapper(*args, **kwargs):
#         func.c += 1
#         res = func(*args, **kwargs)
#         print(f"Function {func.__name__} was invoked {func.c} times")
#         return res
#     return wrapper
#
#
# @count_
# def greet():
#     return "hello world"
#
# @count_
# def add(a, b):
#     return a+b
#
# @count_
# def sub(a, b):
#     return a-b
# def greeting(name):
#     return f"hello {name}"
#
# print(add(1,2))
# print(add(1,2))
# print(add(1,2))
# print(add(1,2))
# print(add(1,2))


''' max call decorator '''


# def max_calls(func):
#     func.c = 0            # greet.c = 0
#     def wrapper(*args, **kwargs):
#         func.c += 1
#         if func.c > 5:
#             raise ValueError(f"maximum calls to function {func.__name__} exceeded")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @max_calls
# def greet():
#     return "hello world"
#
# @max_calls
# def add(a, b):
#     return a+b
#
# @max_calls
# def sub(a, b):
#     return a-b

# @max_calls
# def greeting(name):
#     return f"hello {name}"
#
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(greet())
# print(greet())


''' waf to repeat decorator '''

# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(2):
#             func(*args, **kwargs)
#             sleep(3)
#     return wrapper
#
# @repeat
# def greet():
#     print("hello world")
#
# greet()


# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(2):
#             res = func(*args, **kwargs)
#             sleep(3)
#         return res
#     return wrapper
#
# @repeat
# def add(a, b):
#     print("its adding")
#     return a + b
#
#
# @repeat
# def greet():
#     print("its greet function")
#     return "hello world"
#
# print(add(12, 56))
# # print(add(1, 56))
# # print(add(2, 56))
# # print(greet())


# def repeat(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(2):
#             res = func(*args, **kwargs)
#             print(res)
#             sleep(3)
#
#     return wrapper
#
#
# @repeat
# def add(a, b):
#     print("its adding")
#     return a + b
#
#
# print(add(12, 56))
# # print(add(1, 56))
# # print(add(2, 56))





'''    cache decorator   '''

# def cache(func):
#     func._cache = {}                    # attaching a empty dictionary
#     def wrapper(*args, **kwargs):
#         if args in func._cache:
#             print("getting result from the cache ")
#             return func._cache[args]
#         print("getting result for the first time ")
#         result = func(*args, **kwargs)
#         func._cache[args] = result
#         return result
#     return wrapper
#
# @cache
# def sub(a, b):
#     sleep(5)
#     return a - b
#
# @cache
# def add(a, b):
#     sleep(5)
#     return  a+b
#
#
# print(add(2, 5))
# print(add(2, 5))

'''  phone decorator '''
# numbers = [1234567890, 7978423230, 8093763907, 7978423235, 8989457810]
#
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) ==10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith("91"):
#         str_number = "+" + str_number[:2] + "-" + str_number[2:]
#         return str_number
#     else:
#         return str_number
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         temp = args[0]
#         processed_numbers = [add_prefix(number) for number in temp ]
#         return func(processed_numbers)
#     return wrapper
#
# @prefix_country_code
# def print_numbers(phone_numbers):
#     for item in phone_numbers:
#         print(item)


''' parameterised decorator '''

def delay(seconds = 5):
    def _delay(func):
        def wrapper():
            sleep(seconds)
            return func
        return wrapper
    return _delay
























