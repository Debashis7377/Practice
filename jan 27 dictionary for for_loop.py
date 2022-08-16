'''zip class'''

# s1 = 'hai'
# s2 = "hey"
# s3 = "are"

# for item in zip(s1,s2,s3):
#     print(item)

# for item1, item2, item3 in zip(s1,s2,s3):
#     print(item1,item2,item3,sep='-')

'''different length to zip'''

# s = "hai"
# s1 = "hello"

# for i1,i2 in zip(s,s1):
#     print(i1, i2)                           # from this method we will loss some data so use longest method

# from itertools import zip_longest
# from itertools import zip_longest
# for i1,i2 in zip_longest(s, s1, fillvalue="Not present"):
#     print(i1, i2)
#
# s=[1,2,3]
# a=enumerate(s)
# print(list(a))
s=["mumbai", "chennai","delhi"]
d= ["1212",'56565','8989']
v={}
for i , j in zip(s,d):
    v[i] = j
print(v)

