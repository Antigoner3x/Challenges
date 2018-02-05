
import sys
''' Add digits of the numbers'''

# 12
# 5
#496
#19
def addingNum(num):
    array = []
    num = num.strip("\n")
    for digits in num:
        digits = int(digits)
        # print digits
        array.append(digits)
    # print array
    print sum(array)

def main():
    testCase = open(sys.argv[1], 'r')
    for test in testCase:
        addingNum(test)

if __name__ == '__main__':
    main()
