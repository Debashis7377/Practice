'''traversing a string in reversed order'''

'''reversed order ----- in reversed'''
# string="hai"
# for item in range(len(string)-1,-1,-1):
#     print(string[item],end=' ')
#
# print()
#
#
# for char in string [::-1]:
#     print(char, end=' ')
#
#
# print()
#
# for char in reversed(string):
#     print(char,end=' ')
#


'''count the number of charecters present in the string'''
s="Hello world"
# count=0
# for i in s :
#     count+=1
# print(count)

'''print even index charecter ,given in the string'''
# for item in range(0,len(s),2):
#     print(s[item],end=' ')
#
# print()
#
# for ele in s[::2]:
#     print(ele,end=' ')

'''print the digits in the string'''
s="hello 123 hai43987"

# for char in s:
#     if char.isdigit() :
#         print(char,end=" ")


#or

# for char in s:
#     if '0' <= char <= '9':
#         print(char,end=" ")


'''wap to count the number of digits present in the string'''

# count=0
# for char in s:
#     if '0' <= char <= '9':
#         count+=1
# print(count)

# Assignment
'''wap to count the number of special charecter in a string'''
'''WAP to count the number of capital and small letters in the string'''

# '''file-- file settig -- version control --- u have git  ---


'''wap to count the number of special charecter in a string'''

# count=0
# string="DebashisDG@2!@#$%^&kjxbhvhj"
# for i in string:
#     if not(('A'<= i <= 'Z') or ('a' <= i <= 'z') or ('1' <= i <= '9')):
#         count+=1
# print(count)


'''WAP to count the number of capital and small letters in the string'''

# string="DebashisDG@2!@#$%^&kjxbhvhj"
# small=0
# capital=0
# for item in string:
#     if 'A'<= item <= 'Z':
#         capital+=1
#     elif 'a' <= item <= 'z':
#         small+=1
# print("capital letters count:",capital)
# print("small letters count is:",small)

# or

# for char in string :
#     if char.islower() :
#         small+=1
#     elif char.isupper() :
#         capital+=1
# print("capital letters count:",capital)
# print("small letters count is:",small)
