""" positional arguments """
# def greet(name , age):
#     print(f"{name} is {age} years old")
# greet("ram", 25)
# greet(25, "age")             #it is wrong due to position

"""keyword arguments"""
# def greet(name , age):
#     print(f"{name} is {age} years old")
# greet(name="ram",age= 25)
# greet(age=25,name= "ram")

""" combination of positional and Keyword"""
# def add_(a,b,c,d):
#     print(a,b,c,d)
#
# add_(1,2,3,4)
# add_(a=1,b=2,c=3,d=4)
# add_(1,2,c=3, d=4)
# add_(a=1, b=2, 3, 4)                        # keyword arguments should be placed after positional arguments

""" positional only arguments"""
# def add_(a, b, c, d, /):
#     print(a, b, c, d)
#
# add_(1, 2, 3, 4)
# add_(a=1, b=2, c=3, d=4)                           # type error

# def add_(a, b, /, c, d):
#     print(a, b, c, d)
# add_(1,2,3,4)
# add_(1,2, c=3, d=4)
# # add_(a=1,b=2,c=3,d=4)

"""keyword only arguments"""

# def add_(*, a, b, c, d):
#     print(a,b,c,d)
#
# add_(a=1,b=2, c=3, d=4)
# add_(1, 2, 3, 4)          #type error
# add_(1,2, c=3, d=4)       # type error


# def add_(a, b, *, c, d):
#     print(a,b,c,d)

# add_(a=1,b=2, c=3, d=4)
# add_(1, 2, 3, 4)
# add_(1,2, c=3, d=4)


''' slash represents positional only arguments , if a function defination has slash in the parameter list then the parameters 
define before slash must accept only positional arguments, but parameters after slash can accept either positional or keyword 
arguments'''


"""  *  star represents keyword only arguments , it specifies the parameters define after star ( * ) mandatorily accepts 
keyword argumetns where as the parameters before star can accept both possitional or keyword arguments"""


'''combination of  * and / '''

# def add_(a, b, /, *, c, d):
#     print(a, b, c, d)
#
# add_(1, 2, c=3, d=4)
# add_(1, 2, 3, 4)                               #type error

"""write a  function to add 2 numbers and return the result """
# use positional as well as keyword arguments
# use positional only arguments
# use keyword only arguments

"""write a function which returns list even numbers in the range 1 to 50"""

# def even_(start, end):
#     l= []
#     for i in range(start, end):
#         if i % 2 == 0 :
#             l.append(i)
#     return l
#
#
# print(even_(1, 21))

# def evens(start=0, end ):
#     l= []
#     for i in range(start, end):
#         if i % 2 == 0 :
#             l.append(i)
#     return l
#
#
# print(even_(1, 21))
# print(even_(21))


                                          #""" Default parameters"""

'''1.     default values indicate that the function argument will take that value if no argument value is passed during function call
 2.     the default value is assigned by using assignment ( = ) operator'''

# def add_(a, b):
#     return a + b
# print(add_(10, 20))
#
# def add_(a, b, c=0):
#     return a + b + c
#
# print(add_(10, 20))
# print(add_(10, 20, 30))



''' any global varibale can be assigned as value to the default parameter , if there is any modification done on that globar variable 
after function defination , then it will have no affect on the defalt value that has already been assign'''

# x = 10
# def add_(a, b= x):                     # x = 10
#     print(a + b)
#
# x = 20
# add_(60)
# print(x)

""" write a function to create a list that returns all the prime numbers in user define range, if the user does not provide start index ,
 take it as 2"""

# def prime(end, start= 2):
#     l= []
#     for n in range(start, end):
#         if n > 1 :
#             for i in range(2, n):
#                 if n % i == 0:
#                     break
#             else:
#                 l.append(n)
#     return l


# print(prime(50))

"""waf to print fibonacci series in the user define range """

# a = 0
# b = 1
# i = 0
# while i < 10 :
#     print(a)
#     c = a+ b
#     a = b
#     b = c
#     i += 1

'''waf that returns fibonacci series up to the number specify'''
'''waf that return nth fibonacci number'''


# def fib(k):
#     a = 0
#     b = 1
#     i = 0
#     for n in range(k):
#         while i < n :
#             print(a)
#             c = a+ b
#             a = b
#             b = c
#             i += 1
#
# fib(15)
