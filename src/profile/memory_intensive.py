@profile
def memory_intensive():
    small_list = [None] * 1000000
    big_list = [None] * 10000000
    del big_list
    return small_list

a = memory_intensive()
print(len(a))
