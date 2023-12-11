#!python3

def task(initial):
    value = initial
    while True:
        value = yield f"<{value * 2}>"

core = task(100500)

print(f"Start: {next(core)}")

for i in range(5):
    print(core.send(i + 1))
