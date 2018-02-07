import math

def arith(a, b):
    c = a + b
    d = a - b
    e = a*b
    print c
    print d
    print e

def div(a, b):
    c = a//b
    e = (a/float(b))
    print c
    print e

def rangeMe(a):
    for i in range(0, a):
        p = i ** 2
        print p
def main():
    a = int(raw_input())
    # b = int(raw_input())
    rangeMe(a)
if __name__ == "__main__":
    main()