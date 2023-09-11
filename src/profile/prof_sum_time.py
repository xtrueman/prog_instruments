from functools import reduce
import time

def manual_sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def standard_sum(n):
    return sum(list(range(1, n+1)))

def reduce_sum(n):
    return reduce(lambda x, y: x + y, list(range(1, n+1)))


start = time.time()
manual_sum(10000000)
end = time.time()
print('manual_sum:\t', round((end - start) * 1000), 'millisec')

start = time.time()
standard_sum(10000000)
end = time.time()
print('standard_sum:\t', round((end - start) * 1000), 'millisec')

start = time.time()
reduce_sum(10000000)
end = time.time()
print('reduce_sum:', round((end - start) * 1000), 'millisec')
