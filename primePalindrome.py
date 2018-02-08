<<<<<<< HEAD
''' Write a program which determins the largest prime palindrome less than 1000'''

#prime is # can't be divided by anything but itself
primes = []
def myprime():
    count = 0
    x = 1
    m = 1
    while count != 1001:
        for i in range(2, count):
            if x%i == 0: # i is not a prime
                break
        else:
            #print x
            primes.append(x)
            count += 1
        x += 2 #if 15, x = 17, if 19, x = 21, if 21, x = 23

def palindrome():
    #print primes
    palin = []
    for items in primes:
        if str(items) == str(items)[::-1]:
            #print items
            palin.append(items)
    print max(palin)





def main():
    myprime()
    palindrome()
if __name__ == "__main__":
=======
''' Write a program which determins the largest prime palindrome less than 1000'''

#prime is # can't be divided by anything but itself
primes = []
def myprime():
    count = 0
    x = 1
    m = 1
    while count != 1001:
        for i in range(2, count):
            if x%i == 0: # i is not a prime
                break
        else:
            #print x
            primes.append(x)
            count += 1
        x += 2 #if 15, x = 17, if 19, x = 21, if 21, x = 23

def palindrome():
    #print primes
    palin = []
    for items in primes:
        if str(items) == str(items)[::-1]:
            #print items
            palin.append(items)
    print max(palin)





def main():
    myprime()
    palindrome()
if __name__ == "__main__":
>>>>>>> origin/master
    main()