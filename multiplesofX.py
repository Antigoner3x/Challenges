
import sys


def multiples(x, n):
    p = []
    #print "x: " + str(x) + " n: " + str(n)
    for i in range(n):
        y = (i*n)
        #print y
        if y >= x:
            # print "p " + str(p)
            p.append(y)
    # print p
    # print "array: " + str(p)
    minimum = min(p or [x])
    print minimum
    # del p[:]



def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        #]print(test.lower())
        # print "test:"+ test
        test = test.split(",")
        x = int(test[0])
        n = int(test[1])
        multiples(x, n)
if __name__ == '__main__':
    main()