#!python3

import time
import asyncio
import asyncmy

dbparams = { 'host': 'localhost', 'user': 'trueman', 'password' : '12345', 'db' : 'test' }

queries = [
    'SELECT SLEEP(5) + 42',
    'SELECT SLEEP(5) + 43',
    'SELECT SLEEP(5) + 44',
]

async def execute_query(query):
    conn = await asyncmy.connect(**dbparams)
    async with conn.cursor() as cur:
        await cur.execute(query)
        print(query, ':', await cur.fetchone())
    await conn.ensure_closed()

async def main():
    await asyncio.gather(*(execute_query(query) for query in queries))

start_time = time.perf_counter()

asyncio.run(main())

elapsed = time.perf_counter() - start_time
print("Finished in", round(elapsed,2), "sec.")
