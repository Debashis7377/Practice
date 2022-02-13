""" variable positional arguments"""

# def spam(*args):                       # packing
#     print(args)
#
# spam(1,2,3,4)

''' waf that takes integers and float data type as input or arguments and returns its sum  '''
# def sum_(*args):
#     print(sum(args))
#
# sum_(1,2,3,4,5,6)

'''or '''
# def sum_(*args):
#     total = 0
#     for i in args:
#         if isinstance(i,(int, float)):
#             total += i
#     return total
# print(sum_(1,2,3,4))


''' waf that returns the number of positional arguments given to that function '''
# def pos(*args):
#     print(args)                       # len(args)
#     count = 0
#     for _ in args:
#         count += 1
#     return count
#
#
# print(pos(1,2,3))

''' waf that takes variable number of positional arguments and return all the integer values '''

# def num(*args):
#     print(args)
#
#     for item in args:
#         if isinstance(item,int):
#             print(item)
#
#
# num(1,2.3,56+6j,2,6,8,2.5)

''' waf that takes multiple arguments and returns only the string it reversed order'''
# def rev(*args):
#     print(args)
#     string = []
#
#     for i in args:
#         if isinstance(i, str):
#             string.append(i[::-1])
#
#     return string
#
# print(rev('debashis', 12, 3.65, 3+5j, 'behera'))

''' variable keyword arguments '''
# def aa(**kwargs):
#     return kwargs
#
# print(aa(a =1,b=2,c=3))

''' waf that returns number of positional arguments and no. of keyword arguments '''
# def count_(*args, **kwargs):
#     return len(args),len(kwargs)
#
# print(count_(1,2,3,a=1,b=3,c=3))

''' packing args'''

# def packing_args(*args,**kwargs):

#     return args, kwargs
# print(packing_args(1,2,3,a=10,b=20))
# ''' unpacking args '''
# l = [1, 2, 3]
# print(*l)

# d = dict(a=10, b=20)
# print(*d)
# print(**d)            # type error

''' waf that checks if the given number of arguments is greater then 5 or not '''

# def greater(*args):
#     if len(args) > 5:
#         return 'its length is greater then 5'
#     return 'length is less '

# print(greater(12,23,56))




