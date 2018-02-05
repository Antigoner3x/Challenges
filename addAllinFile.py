import sys

array = []
class myNum():

    def addMe(self, test):

        # print "test"
        # print test
        test = int(test)
        array.append(test)
        # print sum(array)

        # print array
    def readIn(self):
        testCases = open(sys.argv[1], 'r')
        for test in testCases:
            myNum().addMe(test)


def main():
    myNum().readIn()
    print sum(array)
    # print array


if __name__ == "__main__":
    main()