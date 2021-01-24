#!/usr/bin/env python3
# coding=utf-8

from numpy import random as rd
import numpy as np

import rich as r


def verficate(level=10, times=100):
    cnt = [0] * level
    #p = [0] * level

    n = 0
    while n < times:
        num = rd.randint(level)
        cnt[num] += 1
        n += 1

    for i in range(level):
        cnt[i] = np.divide(cnt[i], times)
    
    return cnt

# TODO: add argv to control arguments
def main():
    p = verficate(100, 1000)
    for i in range(len(p)):
        r.print(p[i])

main()
