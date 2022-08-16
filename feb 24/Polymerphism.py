from functools import singledispatch

@singledispatch
def add(a, b):
    print("base function add")

@add.register(int)
def _(a, b):
    print("calling int")
    return a+b

@add.register(float)
def _(a, b):
    print("calling float")
    return a+b

@add.register(list)
def _(a, b):
    print("calling list")
    return sum(a) + b

# print(add(1, 2))
# print(add(5.6, 5))
# print(add([1, 2, 3], 4))




''' 
1. class 
2. constructor (__init__)                  # call by passing positional arguments and keyword arguments     
3. instance and class variable             # self.__class__.name 
4. instance and class dictionary           # self.__class__.__dict__ and self.__dict__
5. multi constructor in same class         #  
6. Overloaded constructor 
7. Inheritance ---> 5 different methods    # imp
8. mro --- >   __mro__ 
9. object
10.Decorating entire class 
11.property decorators (getters, setters) 
12.Single dispatch 
'''




# class employee:
#     def __init__(self, _id, name):
#         self._id = _id
#         self.name = name
#
# class weeklyEmployee(employee):
#     def __init__(self, _id, name , weekly_salary, weeks_worked):
#         self.weekly_Salary = weekly_salary
#         self.weeks_worked = weeks_worked
#         super().__init__(_id, name )
#
#     def calculate_pay(self):
#         return self.weekly_Salary * self.weeks_worked
#
#
# class HourEmployee(employee):
#     def __init__(self, _id, name, hourly_rate, hours_worked):
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked
#         super().__init__(_id, name)
#
#     def calculate_pay(self):
#         return self.hours_worked * self.hourly_rate
#
# class CommisionedEmployee(weeklyEmployee):
#     def __init__(self, _id, name , weekly_salary, weeks_worked, commission_amount):
#         self.commission_amount = commission_amount
#         super().__init__(_id, name , weekly_salary, weeks_worked)
#
#     def calculate_pay(self):
#         actual_pay = super().calculate_pay()
#         return actual_pay + self.commission_amount