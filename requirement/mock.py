# s = "deb ashis howe are ypu so"
# d = s.split()
# f = []
# for item in d:
#     print(item[::-1], end = ' ')


# s = [1, 2, 3, 1, 2]
# d = {}
# for item in s:
#     d[item] = s.count(item)
#
# print(d)


# def fahrenhite(temp):
#     try:
#         assert (temp>0), temp
#         return ((temp-273)*1.8 + 32)
#     except AssertionError:
#         return "colder then absolute zero", temp
#
# print(fahrenhite(565627))





# a = [1, 2, 3, 4]
# from copy import deepcopy
# b = deepcopy(a)
# print(id(a), id(b))
# b = a
# print(b)
#
# print(id(a))
# print(id(b))


# s = dict.fromkeys("hello", "hai")
# print(s)
#
# k = s.pop("e")
# print(k)
# print(s)
# s.popitem()
# print(s)

# class Numbers:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             raise StopIteration
#
#         a = self.start
#         self.start += 1
#         return a
#
#
# n = Numbers(1, 5)
# for item in n:
#     print(item)

# import json
# a = {"hai": 3, "hello": 4}
#
# b = json.dumps(a)
# print(b)
# print(type(b))
# c = json.loads(b)
# print(c)
# print(type(c))










# def fibo(num, a = 0, b = 1, i=0):
#     if i<=num:
#         print(a, end = ' ')
#         c = a + b
#         a = b
#         b = c
#         fibo(num, a, b, i+1)
# fibo(10)

# def fibo(num, a = 0, b = 1):
#     if a <= num:
#         print(a, end = ' ')
#         c = a + b
#         a = b
#         b = c
#         fibo(num, a, b)
# fibo(10)


















""" prime numbers """
def prime(n):
    for item in range(2, n+1):
        for char in range(2, item):
            if item % char == 0:
                break
        else:
            print( item)
prime(100)
""" fibonacci series """
def fibo(num, a=0, b = 1):
    if a <= num:
        print(a)
        c = a + b
        a = b
        b = c
        fibo(num, a, b)
fibo(10)
""" factorials """
def facto(n):
    fact = 1
    for item in range(1,n+1):
        fact *= item
    print(fact)
facto(15)
""" armstrong number """
for num in range(10, 2000):
    n = len(str(num))
    c = 0
    # print(n)
    for item in str(num):
        c += (int(item) ** n)
        # print(c)
    if c == num :
        print(num)





