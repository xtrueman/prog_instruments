#!python3

import os
import multiprocessing

def worker(num):
    """process worker function"""
    print(f'Worker: {num}, PID:', os.getpid())

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
