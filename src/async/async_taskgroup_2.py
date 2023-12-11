#!python3

import asyncio

async def task1():
    await asyncio.sleep(1)
    print('Task 1 completed')
    return 'Result of Task 1'

async def task2():
    await asyncio.sleep(2)
    print('Task 2 completed')
    return 'Result of Task 2'

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())
        # TaskGroup будет ждать завершения всех задач, прежде чем выйти из блока

asyncio.run(main())
