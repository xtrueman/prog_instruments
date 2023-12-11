#!python3

def subr(n):
    yield f"One: {n}"
    yield f"Two: {n}"
    return f"Done: {n}"

def task():
    for i in range(3):
        result = yield from subr(i)
        yield result
    return "*END*"

core = task()
try:
    while (res := next(core)):
        print(res)
except StopIteration as E:
    print(E.value)
