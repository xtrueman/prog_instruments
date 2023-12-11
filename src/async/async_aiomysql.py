#!python3

import time
import asyncio
import aiomysql

dbparams = { 'host': 'localhost', 'user': 'trueman', 'password' : '12345', 'db' : 'test' }
queries = [
    'SELECT SLEEP(5) + 42',
    'SELECT SLEEP(5) + 43',
    'SELECT SLEEP(5) + 44',
]

async def fetch(query):
    conn = await aiomysql.connect(**dbparams)
    async with conn.cursor() as cur:
        await cur.execute(query)
        result = await cur.fetchone()
        print(f"Result of '{query}':", result)
    conn.close()

async def main():
    await asyncio.gather(*(fetch(query) for query in queries))

start_time = time.perf_counter()

asyncio.run(main())

elapsed = time.perf_counter() - start_time
print("Finished in", round(elapsed,2), " seconds.")

