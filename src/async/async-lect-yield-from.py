#!python3

def subr():
    yield "One"
    yield "Two"

def task():
    for i in range(3):
        yield from subr()
        yield f"{i} Passed"

for res in task():
    print(res)
