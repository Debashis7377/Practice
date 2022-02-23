path = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\csv_files\employees.csv"
# # employee.csv
# import csv
# def read_csv():
#     with open(path) as file:
#         records = []
#         # rows = csv.reader(file)
#         rows = csv.DictReader(file)
#         for row in rows:
#             # print(row)
#             # print(row["name"], row["gender"])
#             records.append(row)
#     return records
#
# # print(read_csv())
#
#
# ''' i want to calculate the total pay that i am paying for all the employee'''
#
# data = read_csv()
# def total_salary(data):
#     total = 0.00
#     for item in data:
#         total = total + float(item["pay"])
#     return total
#
# # print(total_salary(data))
#
#
#
# ''' i want to know how many male and female employees are working in the company '''
# def get_emp_by_gender(data):
#     from collections import defaultdict
#     by_gender = defaultdict(int)
#     for item in data:
#         g = item["gender"]
#         by_gender[g] += 1
#     return by_gender
#
#
# # print(get_emp_by_gender(data))
#
#
# ''' i want to sort based on their names '''
#
# by_name = sorted(data, key = lambda item:item["name"])
# by_pay = sorted(data, key = lambda item:item["pay"])
#
# # for item in by_name:
# #     print(item)
#
#
# # for item in by_pay:
# #     print(item)
#
# # for item in reversed(by_pay):
# #     print(item)
#
#
# ''' how many unique teams are present in the company '''
#
# # using list
# # teams = [item["team"] for item in data]
# # print(teams)
#
# # using set
# # teams = {item["team"] for item in data}
# # print(teams)
#
#
# '''how many employee details who are drawing more then 80000'''
#
#
# # more_80k = [item for item in data if float(item["pay"]) > 80000]
#
# # for item in more_80k:
# #     print(item)
#
#
'''        most important

a = [1, 2, 3]
b = (1, 2, 3)
from sys import getsizeof
# print(getsizeof(a))
print(getsizeof(b))
a.append(5)
a.append(9)
print(getsizeof(a)) '''



# ''' using log files  '''



path1 = r"C:\Debashis\pythonProject\pythonProject\Practice\files_directory\txt_log_files\sample.log"

'''
1.  list of tuples
2.  list of lists
3.  list of dictionary
4.  list of employee instance 
5.  Data class
6.  Namedtuple
'''
import csv
# def read_csv():
#     records = []
#     with open(path) as file:
#         rows = csv.reader(file)
#         next(rows)          # skip the first row
#         for row in rows:
#             # print(row)
#             # print(row[0], row[1], row[2])
#             # records.append([row[0], row[1], row[2]])
#             # records.append((row[0], row[1], row[2]))
#             records.append({"fname": row[0], "gender": row[1], "team":row[2]})
#         return records
# data = read_csv()
# # print(data)
# for item in data:
#     print(item)
#

# class employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
# def read_csv():
#     records = []
#     with open(path) as file:
#         rows = csv.reader(file)
#         next(rows)          # skip the first row
#         for row in rows:
#             e= employee(row[0], row[1], row[2])
#             records.append(e)
#         return records
#
# data = read_csv()
#
# for item in data:
#     print(item)






