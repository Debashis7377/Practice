
def timer(func):
    def wrapper():
        import time
        st = time.time()
        # print(st)
        func()
        end = time.time()
        # print(end)
        print("total time taken:" , end-st)
    return wrapper

@timer
def sqr():
    for item in range(1, 50):
        item = item ** 2
        print(item)

@timer
def cube():
    for item in range(1, 30):
        item = item ** 3
        print(item)

import threading
t1 = threading.Thread(target=sqr, args= ())
t2 = threading.Thread(target=cube, args=())
t1.start()
t2.start()
t1.join()
t2.join()