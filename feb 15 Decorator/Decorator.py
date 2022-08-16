''' wa decorator which takes a string and reversed it '''

# def reve(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#
#     return wrapper
# @reve
# def spam(string):
#     return string
#
# print(spam("debashis"))

''' wa decorator to executes a function for 3 times '''

# def reve(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#
#     return wrapper
#
# @reve
#
# def spam(a, b):
#     print (a + b)
#
# spam(1, 2)



'''             Decorator can not take more then 1 argument          '''


''' wa decorator which executes the function for 'n' times    '''

# def outer(n):
#     def repeat(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#
#         return wrapper
#     return repeat
#
# @outer(5)                               # repeat
# def add(a, b):
#     print(a + b)
#
# add(1, 2)
#
# @outer(2)
# def sub(a, b):
#     print(a - b)
#
# sub(10, 4)

'''  wa decorator which input a delay of n seconds  '''

# import time
# def outer(n):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#
#         return wrapper
#     return delay
#
#
# @outer(3)                               # repeat
# def add(a, b):
#     print(a + b)
#
# add(8, 2)
#
# @outer(2)
# def sub(a, b):
#     print(a - b)
#
# sub(10, 8)


''' wa decorator programs that calculate time of execution of a function '''

import time
def outer(n):
    def delay(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            time.sleep(n)
            func(*args, **kwargs)
            end = time.time()
            print(f"time of execution :{end - start}")
        return wrapper
    return delay


@outer(3)                               # repeat
def add(a, b):
    print(f" outer output {a + b}")

add(8, 2)


'''  1.  wa decorator function  to count the number of arguments passed to a function 
     2.  wadf to return only positive values after subtraction
     3.  wadf to print "hello world " message if the user has not given input 
     4.  wadf to return the length of the given interable  '''



'''   1.     '''

# def count(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#
#         if isinstance(res, (str, tuple, list,set,dict)):
#             print(len(res))
#         else:
#             out = str(res)
#             print(len(out))
#
#     return wrapper
#
# @count
#
# def spam(n):
#     return n
# spam(1234)

'''2.  wadf to return only positive values after subtraction '''

# def pos(func):
#         def wrapper(*args, **kwargs):
#
#             res = func(*args, **kwargs)
#             print(res)
#             print(abs(res))
#         return wrapper
# @pos
#
# def sub(a, b):
#     return a - b
#
# sub(6, 10)

''' 3.  wadf to print "hello world " message if the user has not given input  '''

# def msg(func):
#     def wrapper(*args, **kwargs):
#
#         res = func(*args, **kwargs)
#         if res:
#             return res
#         else:
#             return "hello world"
#
#     return wrapper
# @msg
#
# def pas(*args):
#     return args
#
# print(pas())



