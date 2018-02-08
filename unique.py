<<<<<<< HEAD
import sys


def duplicates(test):
    m = []
    n = set()
    test = str(test)
    test = test.split(",")
    for items in test:
        # print items
        if items not in n:
            m.append(items)
            n.add(items)
    m = ",".join(m)
    print m


def main():
    testcases = open(sys.argv[1], 'r')
    for test in testcases:
        test = test.replace("\n", "")
        duplicates(test)


if __name__ == "__main__":
=======
import sys


def duplicates(test):
    m = []
    n = set()
    test = str(test)
    test = test.split(",")
    for items in test:
        # print items
        if items not in n:
            m.append(items)
            n.add(items)
    m = ",".join(m)
    print m


def main():
    testcases = open(sys.argv[1], 'r')
    for test in testcases:
        test = test.replace("\n", "")
        duplicates(test)


if __name__ == "__main__":
>>>>>>> origin/master
    main()