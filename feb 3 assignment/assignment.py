""" 1 to 10 """
# def range_(end, start=0):
#     for i in range(start, end):
#         print(i)
# range_(10)
""" 10 to 1 """
# def range_(start, end):
#     for i in range(start, end, -1):
#         print(i)
# range_(10, 0)

""" even numbers  from 1 to 10 """
# def even(end, start= 0):
#     for i in range(start, end):
#         if i % 2 == 0:
#             print(i)
# even(100)

""" traversing through strings """
# def trav_(args):
#     for i in args:
#         print(i)
# trav_("debashis")

""" traversing through lists """
# def list_(args):
#     for i in args:
#         print(i)
# list_([10,20,30,3.6])

""" traversing through sets """
# def set_(args):
#     for i in args:
#         print(i)
# set_({10,20,6.6})

""" traversing through dictionaries """
# def dict_(n):
#     for i in n.items():
#         print(i)
# dict_({'a':2, 'b':3})

""" to print index and character in a string """
# def ind(n):
#     for i, j in enumerate(n):
#         print(i, j)
# ind("debashis")

""" traversing a string in reversed order """
# def rev(n):
#     for i in reversed(n):
#         print(i, end=' ')
# rev("debashis")

""" count the number of characters in a string """
# def count_(n):
#     count = 0
#     for i in n:
#         count += 1
#     print(count)
# count_("debashis")

""" print even indexed characters in the string """
# def even(n):
#     for i in range(len(n)):
#         if i % 2 == 0:
#             print(n[i])
# even("debashis")

""" print the digits in the string """
# def digit_(n):
#     for i in n:
#         if i.isdigit():
#             print(i)
# digit_("debashis123")

""" print the number of special charecter present inside the string """

# def sp(n):
#     count = 0
#     for char in n:
#         if not ("a" <= char <= "z" or "A" <= char <= "Z" or "0" <= char <= "9"):
#             count += 1
#
#     print(count)
# sp("hai#4(&*")

""" capital and small letters """
# def lt(n):
#     cap = 0
#     sm = 0
#     for i in n:
#         if i.islower():
#             sm += 1
#         elif i.isupper():
#             cap += 1
#     print(sm)
#     print(cap)
# lt("debASHis")

""" count of consonants """
# def count_(n):
#     count = 0
#     for i in n:
#         if not i.lower() in "aeiou":
#             count += 1
#     print(count)
# count_("debashis")

""" char and its index """

# def char(n):
#     item = "a"
#     for i, j in enumerate(n):
#         if j == item:
#             print(i, j)
#             break
#
# char("hai hello how are you")

