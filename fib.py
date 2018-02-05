
import sys

def fib(test):
    #1,1,2,3,5
    count = 0
    previous = 0
    current = 1
    test = int(test)
    for i in range(0,test,1):
        i += 1
        if i == 0:
            current = 1
            count +=1
        else:
            next = current + previous
            # print next
            previous = current
            count += 1
            # print current
            current = next
    print previous






def main():
    testcases = open(sys.argv[1], 'r')
    for test in testcases:
        fib(test)

if __name__ == "__main__":
    main()