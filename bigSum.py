#!/bin/python

import sys

def aVeryBigSum(n, ar):
    m = []
    count = 0
    m.extend(ar)
    #print m
    for i in m:
        i = int(i)
        count += i
    return count

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
