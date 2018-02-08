<<<<<<< HEAD
"""given x, perform conditions:
if n is odd, print weird
if n is even and range 2 - 5, print not weird
if n is even and in range 6 - 20, print weird
if n is even and greater than 20, print not weird
n <=100"""

def ifElse(n):
    if n%2 == 0:
        if n < 5:
            print "Not Weird"
        if 6 <= n <= 20:
            print "Weird"
        if n > 20:
            print "Not Weird"

    else:
        print "Weird"


def main():
    n = int(raw_input())
    ifElse(n)
if __name__ == "__main__":
=======
"""given x, perform conditions:
if n is odd, print weird
if n is even and range 2 - 5, print not weird
if n is even and in range 6 - 20, print weird
if n is even and greater than 20, print not weird
n <=100"""

def ifElse(n):
    if n%2 == 0:
        if n < 5:
            print "Not Weird"
        if 6 <= n <= 20:
            print "Weird"
        if n > 20:
            print "Not Weird"

    else:
        print "Weird"


def main():
    n = int(raw_input())
    ifElse(n)
if __name__ == "__main__":
>>>>>>> origin/master
    main()