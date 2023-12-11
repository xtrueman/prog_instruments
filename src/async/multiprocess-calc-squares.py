#!python3

import os
from multiprocessing import Pool

def f(x):
    print('Worker PID:', os.getpid(), '; arg:', x)
    return x * x

if __name__ == '__main__':
    with Pool(5) as p:
        print('Squares:', p.map(f, [1, 2, 3]))
