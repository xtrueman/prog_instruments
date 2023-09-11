from functools import reduce
import timeit

def manual_sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def standard_sum(n):
    return sum(range(1, n+1))

def reduce_sum(n):
    return reduce(lambda x, y: x + y, range(1, n+1))


timeit_time = timeit.timeit(
    "manual_sum(1000000)",
    "from __main__ import manual_sum", number=10
)
print('manual_sum:\t', round(timeit_time * 1000), 'millisec')

timeit_time = timeit.timeit(
    "standard_sum(1000000)",
    "from __main__ import standard_sum", number=10
)
print('standard_sum:\t', round(timeit_time * 1000), 'millisec')

timeit_time = timeit.timeit(
    "reduce_sum(1000000)",
    "from __main__ import reduce_sum", number=10
)
print('reduce_sum:\t', round(timeit_time * 1000), 'millisec')
