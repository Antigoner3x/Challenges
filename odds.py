'''one num per line, print 1-99 odds'''


def odds():
    m = 100
    x = 1

    for i in range(1, m):
        if x <= 100:
            print x
            x+= 2

def main():
    odds()
if __name__ == "__main__":
    main()