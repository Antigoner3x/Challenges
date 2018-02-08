#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    A = []
    B = []
    AA = 0
    BB = 0
    A.extend([a0, a1, a2])
    B.extend([b0, b1, b2])
    #print A
    #print B[1]
    for i in range(0, 3):
        #print(A[i])
        #print(B[i])
        if A[i] > B[i]:
            AA +=1
        elif A[i] < B[i]:
            BB +=1
    return AA, BB

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))

