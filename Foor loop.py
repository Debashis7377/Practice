# from 1 to 10
#
# for i in range(1,11):
#     print(i)


# 10 ------ 1
# for i in range(10,0,-1):
#     print(i)


# -1 ------ -10
# for i in range(-1,-11,-1):
#     print(i)



 # '''-10 -------------- -1'''
# for i in range(-10,0):
#     print(i)


'''even  numbers   '''
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)


'''traversing through strings'''

# string= "python"
# for item in range(len(string)):
#     print(item,string[item])

# list=[10,23,56,58,9]
#
#
# for char in list :
#     print(char,end=' ')


# tup=(10,23,56,58,9)
# for char in tup:
#     print(char,end=' ')


# list= [1,213,89,45,5263,2,54,56]
# for index in range(len(list)):
#     print(list[index])




# '''traversing through set'''
#
# set_= {}




'''traversing through dictionary'''

# d={"one": 1, "two": 2,"three": 3}
#
# for key in d:
#     print(key,d[key],sep="-->")


'''to print index and charecter in a string'''

string= 'Debashis'
# for index in range(len(string)):
#      print(index,string[index])

'''Enumerator ---> packing anf unpacking with two variables '''
for index,item in enumerate(string):
    print(index,'--->',item)



