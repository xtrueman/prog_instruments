#!python3

import time
import asyncio
import aiomysql

dbparams = { 'host': 'localhost', 'user': 'trueman', 'password' : '12345', 'db' : 'test' }
queries = [
    'SELECT SLEEP(5) + 42 as result;',
    'SELECT SLEEP(5) + 43 as result;',
    'SELECT SLEEP(5) + 44 as result;',
]

async def fetch(pool, query):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(query)
            result = await cur.fetchone()
            print(f"Result of '{query}':", result)

async def main():
    async with aiomysql.create_pool(**dbparams) as pool:
        await asyncio.gather(*(fetch(pool, query) for query in queries))

start_time = time.perf_counter()

asyncio.run(main())

elapsed = time.perf_counter() - start_time
print("Finished in", round(elapsed,2), "sec.")
