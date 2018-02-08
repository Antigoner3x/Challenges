#!/bin/python

import sys


def simpleArraySum(n, ar):
    # print(ar)
    # print(n)
    n = 0
    for i in ar:
        n = n + i
    return n


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)