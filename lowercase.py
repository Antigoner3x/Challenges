'''given a string, write a program to convert it into lowercase'''

import sys

class mywords():
    def getString(self):
        testcases = open(sys.argv[1], 'w')
        for test in testcases:
            lowercase(test)
    def lowercase(self, test):
        test = str(test)
        test = test.lower()
        print test
def main():
    mywords().getString()
if __name__ == "__main__":
    main()