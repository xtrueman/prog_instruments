from pympler.asizeof import asizeof

cnt = 1000000
list_int = list(range(cnt))
list_str = [str(i) for i in range(cnt)]
dict_i_s = {i : str(i) for i in range(cnt)}
print('sizeof list_int:', asizeof(list_int))
print('sizeof list_str:', asizeof(list_str))
print('sizeof dict_i_s:', asizeof(dict_i_s))
print('elem size list_int:', asizeof(list_int)//cnt)
print('elem size list_str:', asizeof(list_str)//cnt)
print('elem size dict_i_s:', asizeof(dict_i_s)//cnt)
