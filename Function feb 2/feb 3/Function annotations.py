# def add_(a: int, b:int) -> None:
#     return (a+b)
#
# print(add_(1, 2))

''' activity '''

'''1.   WAF to count the number of positional and keyword arguments passed to it  ?
   2.   waf to print message "Hai Everyone" if the user input is not present and if the user input is present , 
print the user input
   3.   A function takes variable number of positional arguments as input . How to check if the arguments that are 
    4.   waf to check whether the number is prime or not '''
'''  1.       '''
# def num(*args, **kwargs):
#     return ('length of positional arguments:',len(args)), ("length of keyword arguments are:", (len(kwargs)))
#
#
# print(num(1,2,3,6,5,4,a=10, b=60, h=98))


'''   2.   '''

# def display(msg="hello everyone"):
#     print(msg)
#
# # display("hello")
# display()

'''     4.      '''

# def prime(*args):
#     for i in args:
#         if args[0] % i == 0:
#             return "it is not a prime number"
#     return "it is prime number"
# print(prime(15))

'''   or   '''

# def prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return f"{num}is not a prime number"
#     return f"{num} is prime number"
# print(prime(15))

'''waf to return last digit of a nuumber / an integer'''
# def last_digit(num):
#     return num % 10        # return str(num)[-1]
#
# print(last_digit())


'''waf named tail that taken sequence an input and a number n and return the last 'n' element from the sequence'''

# def tail(sequence, n):
#     return sequence[-n:]
# print(tail("debashis",5))

''' waf named isperfect_square that accepts a no. and returns true if it is a perfect sqare
 and returns false if it is not  '''

# def isperfect_square(n):                                       #   n // 2
#     for i in range(n):
#         if i * i == n:                                         #   i * i   or i ** 2
#             return "it is a perfect square"
#     return "it is not a perfect square number"
#
#
# print(isperfect_square(16))

'''   or   '''

# def isperfect_square(num):                  #  n // 2
#     sq = int(num ** 0.5)
#     if sq * sq == num:
#         return True
#     return False
# print(isperfect_square(4))

''' waf to get the below output
 func("TRACXN",0) should print RCN
func("TRACXN",1) should print TAX'''

# def func(a=0, b= "TRACXN"):
#     if a == 0 :
#         return b[1::2]
#     elif a == 1:
#         return b[::2]
#     else:
#         return "invalid input number "
# print(func(9))

''' waf that checks if the given  number is a fibonocci number or not '''

# def fibo(n):
#     a = 0
#     b = 1
#     i = 0
#     l = []
#     while a <= n:
#         l.append(a)
#         c = a + b
#         a = b
#         b = c
#
#     if n in l:
#         return "it is a fibonocci number "
#     return "it is not a fibonocci number"
# print(fibo(13))

'''  or  '''

# def fibo_(num):
#     a = 0
#     b = 1
#     while a<= num:
#         if a == num:
#             return f"{num} is a fibonacci number"
#         c = a + b
#         a = b
#         b = c
#     return f"{num} is not a fibonacci number"
#
# print(fibo_(21))

''' waf that takes variable number of inputs and returns length of all the iterables given'''

# def num(args):
#     if isinstance(args,(int,float,complex,bool)):
#         return " give collection as input "
#     return len(args)
# print(num('debashis'))

''' or    '''

# def num(*args):
#     for item in args:
#
#         if isinstance(item,(str,tuple,list,set)):
#             print(item, len(item))
#
# num('debashis')




