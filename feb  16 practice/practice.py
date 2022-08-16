# number = 10
# def add(b, a = number):
#     return a + b
# print(add(5))
# number = 20
# print(add(5))     # due to default value , default value will take only defined values before function initialization

def add(a, b):
    add.count += 1
    return a+b
def sub(a, b):
    sub.count +=1
    return a-b
add.count = 0
sub.count = 0
# print(add(10,5))
# print(sub(10,5))

items = [1, 2, 3, add, sub]
# print(items)

# print(items[3](10,5))

func = {"a" : add, "b": sub}
# print(func['a'](10, 89))



def demo(something):
    return something

# print(demo("debashis"))
# print(demo(add))
# print(demo(add(10, 6)))
# print(demo(sub))
import time
def add(a, b):
    return a+b
# def delay(func, *args, **kwargs):
#
#     time.sleep(5)           # extra functionality # which is called decorators
#     return func(*args, **kwargs)         # original function


def delay(func):
    def wrapper(*args, **kwargs):

        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper

# result = delay(add)
# print(result(1, 2))


def greeting(name):
    return f"hello {name}"

# d = delay(greeting)
# print(d("debashis"))







