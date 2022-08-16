'''traversing throuh a list'''

# l=["python",10,3.2,'selenium','java']
# for item in l :
#     print(item,end=' ')

# for i in range(len(l)):
#     print(l[i])


'''print index and its corresponding element from list '''

# for char in range(len(l)):
#     print('index is :',char,"element is: ",l[char])

# for index , char in enumerate(l):
#     print(index,char)

'''wap to print element in the list in reversed order'''
# l=["python",10,3.2,'selenium','java',3+6j]

# for char in range(len(l)-1,-1,-1) :
#     print(l[char])

# for char in reversed(l):
#     print(char,end=',')

# for char in l[::-1]:
#     print(char)


'''WAP to print alternate elements in list '''
# for char in range(0,len(l),2):
#     print(l[char],end=' ')
#
# print()
#
# for char in range(1,len(l),2):
#     print(l[char],end=' ')

# for i in l[::2]:                      #  sing slicing
#     print(i,end=' ')

# for i in range(0,len(l)):            # using condition
#     if i % 2 == 0 :
#         print(l[i],end=' '

'''odd index '''
# for char in range(0,len(l)):             # using condition
#     if char % 2 != 0 :
#         print(l[char],end=',')

# for char in l[1::2]:                     # using slicing
#     print(char,end=',')

'''wap to print integers present in a list'''

# for item in l :
#     if isinstance(item,int):
#         print(item)

'''to print numeric data type                   # numeric means it consider integer , float and cmplex data type'''
# for item in l :
#     if isinstance(item,(int,float,complex)):
#         print(item)

'''wap to print length of each string in the list'''


# l=['python','node js','selenium','java']
# for item in l :
#     print((item,len(item)))


'''wap to print the strings which are of even length'''

# for char in l:
#     if len(char) % 2 == 0:
#         print(char)


'''wap to create a list which have even length of string'''
# d=[]
# for char in l:
#     if len(char) % 2 == 0:
#         d.append(char)
# print(d)


'''wap to print the elements in the list if the element is of even length print as it is ,
 if the element is odd then reversed it  and print it  '''
# res=[]
# for i in l:
#     if len(i) % 2 == 0:
#         res.append(i)
#     else:
#         res.append(i[::-1])
# print(res)

'''wap to reversed the elements in the list , if the element is of type string or else keep it as it is '''

l=["java",'python',10,True,1.4,"c++","rubby"]
res=[]

for item in l:
    if isinstance(item,str):
        res.append(item[::-1])

    else :
        res.append(item)
print(res)

'''wap to print the elements which are starting with vowel'''

# files=["amazone","flipcart","walmart","gmail","yahoo"]
#
# for char in files :
#     if char[0] in "aeiouAEIOU":                 # char[0].lower() in "aeiou"
#         print(char)

'''wap to all the extensions in the following list'''

files = ["youtube.txt","amazone.pdf","apple.xls","flipcart.in"]
# res = []
# for char in files:
#     res.append(char.split('.')[1])
# print(res)

'''wap to print the file name if the file name is of odd length'''

# for item in files:
#     filename, extension = item.split(".")
#     if len(filename) % 2 != 0:
#         print(filename)
#
# or

# for item in files:
#     a=item.split('.')
#     if len(a[0]) % 2 == 0:
#         pass                            # using pass
#     else :
#         print(a[0])

'''wap to return 1st occurance of the index of given element '''
# numbers=[10,40,20,80,20,40,30]
# num=40

# #using index()
# print(numbers.index(40))

# for index, item in enumerate(numbers):
#     if item == num:
#         print(f"{num} is present at the index of {index}")
#         break
# else:
#     print("element is not persent")


'''check if the number is a prime number '''
# n=5
# for i in range(2,n):
#     if n % 2 == 0:
#         print("it is not a prime numbers")
#         break
# else:
#     print("it is a prime number")

'''series of prime number'''

# for n in range(10):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#
#                 break
#         else:
#             print(n)

'''wap to print all thr elements other then the given element '''

# numbers=[10,40,20,80,20,40,30]
# n=20
#
# for num in numbers:
#     if n == num:
#         continue
#     print(num)

'''<16>   wap to print all the palindrom in the given list'''

# l=["python", "dad", "hai", "malayalam", "madam", "mom"]
# for i in l:
#     if i == i[::-1]:
#         print(i)
