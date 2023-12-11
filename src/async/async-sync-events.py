#!python3

import asyncio

async def waiter(name, event):
    print(f'{name} waits for {event}…')
    await event.wait()
    print(f'…{name} got it!')

async def eventer(wait, event):
    print(f"Emitting {event} in {wait} seconds")
    await asyncio.sleep(wait)
    print(f"Emitting {event}…")
    event.set()
    print(f"Emitted {event}…")

async def main():
    event = asyncio.Event()
    await asyncio.gather(
        waiter("One", event),
        waiter("Two", event),
        eventer(1, event))

asyncio.run(main())
