""" wap to print th\e sum of entire list and sum of only internal list  """

# l = [[1,2,3],[4,5,6],[7,8,9]]
# total_sum = 0
# for item in l:
#     internal_sum = 0
#     for i in item:
#         internal_sum += i
#         total_sum += i
#     print(internal_sum)
# print(total_sum)

"""list of prime  number """

# prime_ = []
# for n in range(1,100):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             prime_.append(n)
# print(prime_)


"""reverse the list """

# l = ["hii", "hello", "python"]
#
# res = []
#
# for item in l[::-1]:
#     res.append(item[::-1])
# print(res)


"""rotatting the list based on k value """

# langeages = ["python", "java", "perl", "php", "python"]
# k = 2
#
# for i in range(k):
#     item = langeages.pop()
#     langeages.insert(0,item)
# print(langeages)


# l = [1, 2, 3, 4, 5, 6]
# n = 3
# for i in range(n):
#     *n, n1 = l
#     l = n1, *n
# print(l)



# s = "AABBCCCDSSAACDD"
# i = 0
# c = 0
# res = ""
# while i < len(s):
#     if s[i] == s[i+1: i+2]:
#         c += 1
#         i += 1
#     else:
#         c += 1
#         res += str(c)+s[i]
#         i +=1
#         c = c-c
# print(res)




