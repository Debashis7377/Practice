# for row in range(5):
#     for col in range(row+1):
#         print("*", end = ' ')
#     print()
'''
*
* *
* * *
* * * *
* * * * *'''

# for row in range(1,5):
#     print('* ' * row)

'''
* 
* * 
* * * 
* * * *'''





# for row in range(1, 5):
#     print(f'{"* " * row:>8}')       # print(f'{"* " * row:>4}')    this is should be double of the number
'''
      * 
    * * 
  * * * 
* * * * 
'''
# for row in range(1, 5):
#     print(f'{"* " * row: ^8}')
'''
   *    
  * *   
 * * *  
* * * *
'''

'''
* * * * 
* * * 
* * 
*
'''
# for row in  range(4, 0, -1):
#     print("* " * row)

'''
* * * * 
  * * * 
    * * 
      * 
      '''
# for row in range(4, 0, -1):
#     print(f'{"* " * row:>8}')

'''
* * * * 
 * * *  
  * *   
   *   
   '''


# for row in range(4, 0, -1):
#     print(f'{"* " * row:^8}')




'''
1 
1 2 
1 2 3 
1 2 3 4 
'''

# for row in range(1, 5):
#     for col in range(1, row+1):
#         print(col, end = ' ')
#     print()

# x = ''
# for row in range(1, 5):
#     x += str(row) + ' '           # row = 1 ===> '1' , '12', '123', '1234'
#     print(x)




'''
1 2 3 4 
1 2 3 
1 2 
1 
'''

# for row in range(4, 0, -1):
#     for col in range(1, row+1):
#
#         print(col, end = ' ')
#     print()



'''
a 
a b 
a b c 
a b c d 
'''

# for row in range(ord('a'), ord('d')+1):
#     for col in range(ord('a'), row+1):
#         print(chr(col), end = ' ')
#     print()
#
# x = ' '
# for row in range(ord("a"), ord("d")+1):
#     x += chr(row) + ' '
#     print(x)
#
# for row in range(1, 5):
#     for col in range(ord('a'), ord("a")+row):
#         print(chr(col), end = ' ')
#     print()





for row in range(1, 7):
    print(f'{"* "*row: ^12}')
