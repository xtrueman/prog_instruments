#!python3

import asyncio
import time

async_mode = False

def showjob(jobname, sync_time_seconds = 0):
    curtime = time.perf_counter() - start_time
    print( f"{curtime:.2f}:\t{jobname}" )
    if sync_time_seconds:
        time.sleep( sync_time_seconds / 60 )

async def PourCoffee():
    showjob("КОФЕ: Ставим чайник наполняться водой", 20)
    showjob("КОФЕ: ЖДЁМ наполнения чайника водой", 40)
    showjob("КОФЕ: Ставим чайник греться", 10)
    showjob("КОФЕ: ЖДЁМ пока нагреется чайник", 0)
    await asyncio.sleep(3) if async_mode else time.sleep(3)
    showjob("КОФЕ: Достаём стакан", 10)
    showjob("КОФЕ: Кладём кофе и сахар", 40)
    showjob("КОФЕ: Наливаем кипяток", 15)
    showjob("КОФЕ: Относим на стол", 20)

    return 'Кофе'

async def FryEggsAsync(eggs_count):
    showjob("ЯИЧНИЦА: Достаём сковородку и ставим на плиту", 20)
    showjob("ЯИЧНИЦА: Достаём масло, наливаем в сковородку", 30)
    showjob("ЯИЧНИЦА: Зажигаем огонь, ставим сковородку", 15)
    showjob("ЯИЧНИЦА: ЖДЁМ пока нагреется сковородка", 0)
    await asyncio.sleep(1) if async_mode else time.sleep(1)
    showjob("ЯИЧНИЦА: Разбиваем в сковородку %d яиц" % eggs_count, eggs_count * 20 )
    showjob("ЯИЧНИЦА: ЖДЁМ пока пожарится яичница", 0)
    await asyncio.sleep(3) if async_mode else time.sleep(3)
    showjob("ЯИЧНИЦА: Достаём тарелку и вилку", 15)
    showjob("ЯИЧНИЦА: Перекладываем в тарелку", 30)
    showjob("ЯИЧНИЦА: Относим на стол", 30)

    return 'Яичница'

async def ToastAsync():
    showjob("ТОСТЫ: Достаём хлеб, доску, нож", 30)
    showjob("ТОСТЫ: Нарезаем тосты", 40)
    showjob("ТОСТЫ: Ставим тосты в тостер жариться", 30)
    showjob("ТОСТЫ: ЖДЁМ обжарки в тостере", 0)
    await asyncio.sleep(3) if async_mode else time.sleep(3)
    showjob("ТОСТЫ: Вытаскиваем тосты", 30)
    showjob("ТОСТЫ: Достаём масло и джем", 30)
    showjob("ТОСТЫ: Намазываем масло и джем", 40)
    showjob("ТОСТЫ: Достаём тарелку и накладываем", 30)
    showjob("ТОСТЫ: Относим на стол", 30)

    return 'Тосты'

async def main():
    await asyncio.gather(PourCoffee(), FryEggsAsync(3), ToastAsync())
    
start_time = time.perf_counter()

asyncio.run(main())

elapsed = time.perf_counter() - start_time
print("Завтрак готов за", round(elapsed,2), " минут.")
