<<<<<<< HEAD
import sys

class mywords():
    def getString(self):
        testcases = open(sys.argv[1], 'r')
        for test in testcases:
            mywords().lowercase(test)
    def lowercase(self, test):
        test = str(test)
        test = test.lower()
        print test
def main():
    mywords().getString()
if __name__ == "__main__":
=======
import sys

class mywords():
    def getString(self):
        testcases = open(sys.argv[1], 'r')
        for test in testcases:
            mywords().lowercase(test)
    def lowercase(self, test):
        test = str(test)
        test = test.lower()
        print test
def main():
    mywords().getString()
if __name__ == "__main__":
>>>>>>> origin/master
    main()