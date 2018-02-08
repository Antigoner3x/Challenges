"""redo me :( """

N, M = map(int,raw_input().split())
for i in xrange(1,((N+1)/2),1):
    print((((N-i-2)))*"-"+".|."*(i%N)+"-"*(((N-i-2))))
print((N + 2)*"-"+"Welcome"+(N + 2)*"-")
for i in xrange(N-2, -1, -2):
    print((N-i)*"-"+".|."*(i%N)+"-"*(N-i))

