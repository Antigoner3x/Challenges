
import pprint
def multiply(n):
    partial = []
    array = []*n
    # print n
    for i in range(1, n, 1):
        for m in range(1, n, 1):
            # print i
            # print m
            partial.append(i * m)
            # print partial

        array.append(partial)
        partial = []
    # print array

    for line in array:
        line = str(line)
        myarray = "".join(line)
        myarray = myarray.replace(",", "")
        myarray = myarray.replace("[", "")
        myarray = myarray.replace("]", "")
        myarray = myarray.replace(" ", "    ")
        print myarray



def main():
    # print "Class"
    n = 12
    n += 1
    multiply(n)

if __name__ == "__main__":
    main()




def main():
    testcases = open(sys.argv[1], 'r')
    for test in testcases:
        fib(test)

if __name__ == "__main__":
    main()