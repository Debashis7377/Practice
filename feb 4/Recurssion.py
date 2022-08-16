# st = "hi hello how are hi you"
# d = {}
# l= st.split()
# for i in l:
#     d[i] = l.count(i)
#
# print(d)
# #
# e = {}
# for i in st:
#     e[i] = st.count(i)

# print(e)

# for i in st:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)




# def count_(start, end):
#     if start < end:
#         return
#     print(start)
#     count_(start-1,end)
# count_(10,1)

'''wa r.programe to add the digits of a number'''
# def sum_(num, count=0):
#     if num > 0:
#         last = num % 10
#         count += last
#         num = num // 10
#         return sum_(num, count)
#     return count
# print(sum_(1234))


# # normal method
# count = 0
# n = 123
# while n > 0:
#
#     num = n % 10
#     n = n // 10           # n //= 10
#     count += num
# print(count)


'''sum of nth number '''

# def sum_(num, count=0):
#     if num > 0:
#         count += num
#         return sum_(num-1, count)
#     return count
# print(sum_(10))

''' wa r.program to find the factorial of a number'''
# def fact_(n, fact=1):
#     if n > 0:
#         fact *= n
#         return fact_(n-1, fact)
#     return fact
# print(fact_(5))

''' wa r.p to count the number of digits in a number'''
# def count_(num, count=0):
#     if num > 0:
#         num = num // 10
#         count += 1
#         return count_(num, count)
#     return count
# print(count_(123))

''' reversed the string '''


# def rev(st, i=0,res=''):
#     if i < len(st):
#         res = st[i] + res
#         return rev(st, i+1, res)
#     return res
# print(rev("debashis"))

''' wa r.p to print fibinacci series up to n '''

# def fibo(num, a=0, b=1, i=1):
#     if i <= num:
#         print(a, end=' ')
#         c = a + b
#         a = b
#         b = c
#         fibo(num, a, b,i+1)
# fibo(15)
# def fibo(num, a= 0, b=1):
#     if a < num:
#         print(a, end = ' ')
#         c = a + b
#         a = b
#         b = c
#         return fibo(num, a, b)
# fibo(15)
# def fibo(num, a=0, b=1, i=o):
#     if i < num :


# my = 'kasi'

# def sr(si = 0):
#     if  my[si:si+1]:
#         print(my[si])
#         sr(si+1)
#
# sr()



# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo( n -2)
# print(fibo(15))



