#!python3

import asyncio
import aiohttp
from aiohttp import ClientTimeout

# Асинхронная функция для получения текста из URL
async def fetch(session, url):
    try:
        # Установка таймаута для запроса
        async with session.get(
            url, allow_redirects=False,
            timeout=ClientTimeout(total=1)
        ) as response:
            print(url, '—', response.status)
    except asyncio.TimeoutError:
        print(url, '— Request timed out')
    except Exception as e:
        print(url, '— Error:', str(e))

# Асинхронная функция для запуска задач параллельной загрузки
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # Создаем асинхронную задачу для каждого URL
            tasks.append(fetch(session, url))
        # Используем asyncio.gather для параллельного исполнения
        return await asyncio.gather(*tasks)

urls = [
    'http://yandex.ru/',
    'http://mail.ru/',
    'http://vk.com/',
    'http://ok.ru/',
    'http://www.google.com/',
    'http://www.example.com',
    'http://www.github.com',
]

# Запуск асинхронной загрузки
asyncio.run(fetch_all(urls))
