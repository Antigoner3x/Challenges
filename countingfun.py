from __future__ import print_function

def counting(n):
    n += 1
    p = []
    for x in range(1,n):
        p.append(x)
    print(p)
    p = "".join(map(str, p))
    print(p)


def main():
    n = int(raw_input())
    counting(n)
if __name__ =="__main__":
    main()