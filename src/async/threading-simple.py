#!python3

import threading

def worker(num):
    """thread worker function"""
    print( 'Worker: %d' % num,
           '; Thread ID: %d' % threading.get_ident() )

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()