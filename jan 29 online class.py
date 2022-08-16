'''<1>      Write a program to print a tuple of character and its ascii value in the given string'''
# s="hello world"
# for i in s :
#         print((i,ord(i)))

'''<2>   WAP to check if the given number is prime or not'''
# n= 23
# for num in range(2,n):
#     if n % num == 0:
#         print("it is not a prime number")
#     else:
#         print("it is a prime number")
'''<3>       WAP to print sum of all the digits present in the string'''

# s = "alpha2python34selenium1239"
# num = 0
# for i in s :
#     if i.isdigit():
#         num+=int(i)
# print(num)

'''or   '''

# s='Hello123hai78hai046'
# num=0
# for char in s:
#     if '0' <= char <= '9':
#         num+=int(char)
# print(num)

'''<4>      WAP to print all the consonants present in the sting'''

s= "debashis behera6980@gmail.com"
# count=0
# for i in s:
#     if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
#         if i.lower() not in "aeiou":
#
#             print(i,end=' ')
#             count+=1
# print(count)

'''wap to print a tuple of index and charecter in the string'''
for i,j in enumerate(s):
    print((i,j))
'''wap to extract all speciasl charecter'''
