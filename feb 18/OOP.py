# class Employee:
#     def __init__(self, fname, lname, pay):            # magic method , constructor, initialization method
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@company.com"

# emp1 = Employee("steve", "jobs", 1000)
# emp2 = Employee("bill", "gates", 2000)
# emp1ee.__dict__


# add = Employee.email(emp1)
# print(add)
#
# odd = Employee.email(emp2)
# print(odd)

#or                             # emp1 and emp2 are the object instsnce of the class Employee
#   when we store the  data in __init__ constructor ,, it is called instance method cause it is storing the values in dictionary

# print(emp1.email())

''' salary hiked '''

# class Employee:
#     def __init__(self, fname, lname, pay):            # magic method , constructor, initialization method
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#     def pay_hike(self, percentage_hike):
#         hike_amout = self.salary * percentage_hike
#         self.salary = self.salary + hike_amout
#         return self.salary
#
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@company.com"
#
#
# emp1 = Employee("steve", "jobs", 1000)
# emp2 = Employee("bill", "gates", 2000)
#
# print(emp1.pay_hike(0.2))
# print(emp1.__dict__)
# print(emp2.pay_hike(0.2))
# print(emp2.__dict__)

class calculator:
    def __init__(self, a, b):             # default value also we can give    a=0, b=0
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

c1 = calculator(10, 20)
c2 = calculator(a=10, b=20)

print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())














