from functools import reduce
import cProfile

def manual_sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def standard_sum(n):
    return sum(range(1, n+1))

def reduce_sum(n):
    return reduce(lambda x, y: x + y, range(1, n+1))

cProfile.run("manual_sum(10000000)")
cProfile.run("standard_sum(10000000)")
cProfile.run("reduce_sum(10000000)")
