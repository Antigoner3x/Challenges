import sys


def reverseMe(sentence):
    rev = []
    for words in sentence:
        words = words.strip("\n")
        words = words.split(" ")

        # print words
        rev.append(words)
    rev = rev[0]
    rev = (rev[::-1])
    # print "wut"
    # print rev
    return rev


def main():
    sentence = []

    testCases = open(sys.argv[1], 'r')
    # print testCases
    for test in testCases:
        #print test
        sentence.append(test)
        rev = reverseMe(sentence)
        rev = " ".join(rev)
        print rev
        sentence = []

if __name__ == "__main__":
    main()