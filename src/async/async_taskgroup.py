#!python3

import asyncio

async def do_work(item):
    await asyncio.sleep(1) # Представим, что здесь выполняется какая-то работа.
    print(f'Работа {item} выполнена')

async def main():
    async with asyncio.TaskGroup() as tg:
        for item in range(3):  # Создаем несколько задач.
            tg.create_task(do_work(item))
        # TaskGroup будет ждать завершения всех задач, прежде чем выйти из блока

# Запуск основной корутины.
asyncio.run(main())