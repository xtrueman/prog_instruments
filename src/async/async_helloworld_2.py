#!python3

import asyncio

async def print_hello():
    await asyncio.sleep(1)
    print('Hello')

async def print_world():
    await asyncio.sleep(1)
    print('World')

async def main():
    await asyncio.gather(
        print_hello(), print_world()
    )

asyncio.run(main())
