""" 1) Write a program to separate out the numbers and alphabets from the string "ASD1GD4J5L37K9" """
import re
string = "ASD1GD4J5L37K9"
# num = []
# alpha = []

# for item in string:
#     if "A" <= item <= "Z" or "a" <= item <= "z":
#         alpha.append(item)
#     elif "0" <= item <= "9":
#         num.append(item)
#
# print(num)
# print(alpha)

# res = []
# for item in string:
#     res += re.findall(r"\d", item)
#
# print("".join(res))
""" 2) Write a program to arrange alphabets in descending order from the string "AlgoShackPrivateLimited" """


# s = "AlgoShackPrivateLimited"
#
#
# res = sorted(s, reverse = True)
# print(res)
# out = "".join(res)
# print(out)










# s = input("enter the string")
# if s == s[::-1]:
#     print("yes")
# else:






""" 279.	Wap to reverse the list without using inbuilt function & slicing  """

''' 1st method '''

# s = "i am a good boy"
# d = []
# for i in s:
#     d.append(i)
# print(d)
# p = []
# for item in range(len(d)):
#     *rest, last = d
#     d.pop()
#     p.append(last)
#
# print("".join(p))


''' 2nd method '''
# s = "i am a good boy"
# d = []
# for i in s:
#     d.append(i)
# print(d)
# k = []
# for item in range(len(d)):
#     old = d.pop()
#     k.append(old)
#
# print("".join(k))




# """	d = {'a': {'b': 1, 'c': 2, 'd':4}}. Print the value of 'd' """
# d = {'a': {'b': 1, 'c': 2, 'd':4}}
# print(d['a']['d'])



""" 
L1 = [1, 2, 3]
L2 = [4, 5, 6]
Merging of two list and sort it in ascending order 
"""
# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
#
# l3 = L2 + L1
# print(l3)
# print(sorted(l3))


""" wap to extract email id from the string """
# st = "debashis behera debashisbehera7377@gmail.com debashis@ "

# import re
# s = re.findall(r"\w+\@\w+\.\w+", st)
# print(s)



""" Extract only password which is having min length of 8, with lower case , special characters [using re] """

# s = "debashis behera 123@!fgp 123jdsdsk@@2"
# import re

# d = re.findall(r"\s[\w+\W+]{8}\s", s)
# print(d)


""" Write a decorator program to find the even number """

# d = []
# t = []
# def deco(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         # print(args)
#         if (args):
#             if isinstance(args[0], (list, tuple)):
#                 for i in args[0]:
#                     d.append(i)
#                 for item in d:
#                     if item % 2 != 0:
#                         t.append("odd")
#                     else:
#                         t.append("even")
#                 return t
#             else:
#                 if args[0] % 2 == 0:
#                     return "even"
#                 return 'odd'
#     return wrapper
# @deco
# def add(a):
#     return a
# print(add(5))
# print(add(10))
# print(add([11, 21, 30]))



""" 
1. Wap to swap variables by using class 
2. Write a decorator program to find the even number
3. How to find web element if there is no locators to find
"""




# class swap_:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         print(self.a)
#         print(self.b)
#     def _swap(self):
#         self.a, self.b = self.b, self.a
#         print(self.a)
#         print(self.b)
#
# k = swap_(("debashis", "Behera"), ("nandu", "gupta"))
# k._swap()




# a = [10, 20, 30]
# s = "10, 20, 30"
# for i in a:
#     print(i)




