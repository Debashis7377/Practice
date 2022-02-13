''' wap to convert all the strings in the list to upper case using map'''
#
# s= "hello world"
# d = lambda word: word.upper()
# print(list(map(d,s.split())))
# res = map(str.lower, s.split())
# print(list(res))


''' wap to convert all the negative numbers in the list to positive '''

# l = [1, 3, -6, 8, -7, -2]
# def convert(num):
#     return abs(num)
#
# con = lambda num: abs(num)


# res = map(con,l)
# print(list(res))

# res = map(abs, l)
# print(list(res))

''' wap that returns the list of numbers raised to the power of their indices using map'''
l = [10, 20, 30, 40]
# def  func(item):
#     return item[1] ** item[0]
# func = lambda item:item[1] ** item[0]
#
# res = map(func, enumerate(l))
# print(list(res))
''' wap that returns all the words in lower case in the given sentence '''


# l = list(range(10))
# evens = [i for i in l if i % 2 == 0]
# odd = [i for i in l if i % 2 != 0]
# print(evens, odd)

# l = [1, 2, 3, 4, 5, 6]
# n = 3
# for i in range(n):
#     *n, n1 = l
#     l = n1, *n
# print(l)

''' wap to get list of length of each word'''

# s = "hii hello everyone"

# res_ = map(len, s.split())
# print(list(res_))

''' wap to get a list of tuples charecter and its value pair'''
# word = "hai"
# def asci(char):
#     return char, ord(char)
#
# res = map(asci, word)
# print(list(res))

''' wap to add the following list elements simultanously '''
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
#
#
# def add_(item1,item2):
#     return item1 + item2
#
# print(list(map(add_,a,b)))

