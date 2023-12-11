#!python3

import httpx
import asyncio

async def fetch(url):
    async with httpx.AsyncClient(follow_redirects=False) as client:
        response = await client.get(url)
        print(url, '—', response.status_code)

async def main():
    tasks = [fetch(url) for url in urls]
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

asyncio.run(main())
