''' previous dictionary assesment question '''
'''1.  '''
s = "helloworld"
# d = {}
# for item in s:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item] += 1
# print(d)
p = {item:s.count(item) for item in s}
print(p)

'''  2.     '''
names = ["apple","google","apple","yahoo","yahoo","gmail","google","gmail","gmail","gmail"]
# d = {}
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
# print(d)

from collections import defaultdict
d = defaultdict(list)
for item in range(len(names)):
    d[nmaes[item]] += [item]
print(d)
'''  4.    '''
# s = "hello world"
# d = {}
# for item in s:
#     if s.count(item) > 1:
#         d[item] = s.count(item)
# print(d)

''' 5.    '''

# d = {'a': 'hello', 'b': 100, 'c': 10.21, 'd': 'world'}
# e = {}
# for item, value in d.items():
#     if isinstance(value,str):
#         e[item] = value[::-1]
#     else:
#         e[item] = value
# print(e)

''' 6.   '''
# names = ["apple","google","apple","yahoo","yahoo","gmail","hii","google","gmail","apple","gmail","gmail"]
# d= {}
# for item in names:
#     if names.count(item) > 1:
#         d[item] = names.count(item)
# print(d)

''' 8.    '''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# d = {}
# a = []
# b = []
#
# for item in numbers:
#     if item % 2 == 0:
#         b.append(item)
#     else:
#         a.append(item)
# d[0] = b
# d[1] = a
# print(d)






















