from memory_profiler import profile

@profile
def manual_sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

@profile
def standard_sum(n):
    tmplist = list(range(1, n+1))
    return sum(tmplist)

manual_sum(1000000)
standard_sum(1000000)
