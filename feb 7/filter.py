''' wap to return even values in the below list'''
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def even(num):
#     if num % 2 == 0:
#         return num
#
# evens = map(even, l)
# print(list(evens))
#
#
# # use filter
#
# evens = filter(even, l)
# print(list(evens))

''' wap that returns list of strings with odd length '''

# l = ['debashis', 'behera', 'gmail', 'flipcart','yahoo']
# def odd_(st):
#     if len(st) % 2 == 1:
#         return st
# print(list(filter(odd_, l)))
#
# # res = lambda st: len(st) % 2 != 0
# # print(list(filter(res, l)))


''' wap which returns all the words starting with vowels in the gievn sentence '''

# sentence = " hello hai how are you"
# l = sentence.split()
# def ext(word):
#     if word[0].lower() in "aeiou":
#         return word
# print(list(filter(ext, l)))
'''   '''
# st = ['debashis', 'behera']
# def fun(a):
#     print([a])
# res = map(fun, st)
# list(res)

# res = list(map(list, st))
# print(res)

# l = [1, 2, 3, 4]
# def count(a):
#     return (a*a)
# print(list(map(count, l)))

# res = lambda i: i*i
# print(list(map(res, l)))


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def c(a):
#     if a[0] % 2 == 0:
#         return a[1] ** 2

# res = list(filter(c, enumerate(l)))
# print(list( map(c, res)))


# print(list( map(c, list(filter(c, enumerate(l))))))















