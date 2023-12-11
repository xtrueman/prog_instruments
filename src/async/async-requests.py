import requests
import asyncio

async def ping_url(url):
    print(url, ':', requests.get(url).status_code)

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(ping_url('https://yandex.ru/')),
    loop.create_task(ping_url('https://mail.ru/'))
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
