import timeit
import random

def copyf (i):
    lst = list(range(i))
    time = timeit.timeit(lambda: lst.copy())
    return time

for i in range(50,1050,50):
    print(i, copyf(i))

def rand_append():
    for i in range(1000, 1001000, 1000):
        print(i, append_avg())
    print("end")

def append_avg():
    lst = []
    total = 0
    for j in range(1000):
        r = random.randint(0, 10)
        start = timeit.default_timer()
        lst.append(r)
        end = timeit.default_timer()
        total += end - start

    return total/1000

def lookup():
    lst = []
    for i in range(1000000):
        lst.append(random.randint)
    return lst

def lookup_time():
    lsst = lookup()
    count = 0
    for i in range(1000, 1001000, 1000):
        total = 0
        for j in range(1000):
            start = timeit.default_timer()
            lsst[count]
            end = timeit.default_timer()
            total += end - start
            count += 1
        print(i, total/1000)