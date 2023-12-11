#!python3


def subr():
    x = yield "Wait for x"
    y = yield f"Wait for y ({x=})"
    return x * y

def task():
    print("Init Task")
    while True:
        value = yield from subr()
        print(f'RCVD: {value}')
        _ = yield value


core = task()
print("Core Created: "+str(core))
print(next(core))
for i in range(8):
    print(core.send(i))