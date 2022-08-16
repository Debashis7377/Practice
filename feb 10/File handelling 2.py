from collections import Counter
from collections import defaultdict
import csv

# import sys
#
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())
""" Assignment
     3, 6, 7, 8, 9"""

''' 3.   finding the length of each line in the text file '''

path = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\sample.txt"

# with open(path) as file:
#     for line in file:
#         print(line, len(line))

'''   6.   extracting message of from sample.log'''

path_ = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\sample.log"

# with open(path_) as file:
#     l = []
#     for lines in file:
#         if lines.strip():
#             word = lines.split()
#             l.append(word[2])
#     print(l)

'''  7.  counting the number of info , warn, trace message '''

# with open(path_) as file:
#     l = []
#     for lines in file:
#         if lines.strip():
#             word = lines.split()
#             l.append(word[2])
#
# msg = Counter(l)
# for i in msg:
#     if i in ('INFO', 'TRACE', 'WARNING'):
#         print(i, msg[i], end=',')

''' 8.    Reading countries from footbal.txt '''

path3 = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\football.txt"
# with open(path3, encoding="UTF-8") as file:
#
#     for line in file:
#         if line.strip():
#             country = line.split("\t")
#             print(country[1])

'''   9.   least and most common words '''

# with open(path) as file:
#     d = defaultdict(int)
#     for line in file:
#         if line.strip():
#             words = line.split()
#             for word in words:
#                 d[word] += 1
# print(d)
# c = Counter(d)
# print(c)
# most, *rest, least = c.most_common()
# print(most, least)

''' 1.  wap to read all the names of the employees in the employee.csv file'''

path2 = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\csv_files\employees.csv"

# with open(path2) as csv_file:
#     obj = csv.reader(csv_file)
#     next(obj)
#     for i in obj:
#         print(i[0])

''' 2.   wap to print only the names salaries that are >70000 '''

# with open(path2) as csv_file:
#     obj = csv.reader(csv_file)
#     next(obj)                             # to skip 1 line we have to use next
#     for i in obj:
#         if int(i[-1]) > 70000:
#             print(i[0])

'''3.     wap to group male and female employees in the file '''

# with open(path2) as csv_file:
#     obj = csv.reader(csv_file)
#     next(obj)
#     d=defaultdict(list)
#     for i in obj:
#        if i[1] == 'male':
#            d[i[1]] += [i[0]]
#        #     d['male'] += [i[0]]
#        # else:
#        #     d['female'] += [i[0]]
#     print(d)
#
# or
# with open(path2) as csv_file:
#     obj = csv.reader(csv_file)
#     next(obj)
#     d={"male":[], "female":[]}                   # new method
#     for i in obj:
#        if i[1] == 'male':
#            d['male'] += [i[0]]
#        else:
#            d['female'] += [i[0]]
#     print(d)

''' 4.  wap to group employees based on their team '''
# with open(path2) as csv_file:
#     obj = csv.reader(csv_file)
#     next(obj)
#     d=defaultdict(list)
#     for i in obj:
#        d[i[2]] += [i[0]]
#     print(d)

''' 5.   wap to sort the shares in test.csv file based on the share prices '''

_path = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\csv_files\test.csv"
# with open(_path) as file:
#     obj = csv.DictReader(file)
#     l = list(obj)
#     print(l)
#     res = sorted(l, key=lambda d: float(d["price"]))
#     print(list(res))


''' 6.   wap to add  all the shares in test.csv file '''

# with open(_path) as file:
#     obj = csv.reader(file)
#     count = 0
#     next(obj)
#     for i in obj:
#         count += int(i[1])
#     print(count)

path4 = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\csv_files\vaccination_data.csv"
'''  7.          '''
''' a.   '''
# with open(path4) as file:
#     obj = csv.reader(file)
#     for line in file:
#         print(line[5])

# with open(_path) as file:
#     obj = csv.
#
''' b.      '''
# d = {}
# with open(path4) as file:
#     obj =  csv.reader(file)
#     next(obj)
#
#     for row in obj:
#         d[row[0]] = row[5]
#     print(d)

'''c.  '''
# d = {}
# with open(path4) as file:
#     obj =  csv.reader(file)
#     next(obj)
#
#     for row in obj:
#         d[row[0]] = row[2]
#     print(d)

'''d..   '''
# d= {}
# with open(path4) as file:
#     obj = csv.reader(file)
#     next(obj)
#     for row in obj:
#         if row[7]:
#             d[row[0]] = row[7]
#
#     # print(d)
# res = sorted(d.items(), key = lambda item:item[-1])
# print(res[-3:])

'''  e.   '''
# with open(path4) as file:
#     obj = csv.DictReader(file)
#     next(obj)
#     for row in obj:
#         total_vaccination = row["TOTAL_VACCINATIONS"]
#         if total_vaccination:
#             if int(total_vaccination) < 10000:
#                 print(row["COUNTRY"])

''' f .   '''

# with open(path4) as file:
#     obj = csv.DictReader(file)
#     d = defaultdict(list)
#     next(obj)
#     for row in obj:
#         d[row['DATE_UPDATED']] += [(row["COUNTRY"]) + (row["TOTAL_VACCINATIONS"])]
# res = sorted(d.items())
# print(res[-1])
# # for item in d.items():
# #     print(item)









