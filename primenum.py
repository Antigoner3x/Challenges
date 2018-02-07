

#std out: 3682913

def myPrime():
    primes = []
    count = 1
    i = 1
    while count != 1001:
        for k in range(2, i):
            if i%k == 0: # i is not a prime
                break
        else:
            #print i
            primes.append(i)
            count += 1
        i += 2
    #add sums of array
    #print primes
    mysum = sum(primes) + 1
    print mysum

def main():
    myPrime()


if __name__ == '__main__':
    main()