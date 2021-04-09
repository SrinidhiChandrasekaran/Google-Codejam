def pascalWalk(n):
    if n < 30:
        for i in range(n):
            print("{:d} 1".format(i+1))
        return
    n = n - 30
    left = True #left side
    ones = 0 #count the number of ones
    for i in range(30):
        if left:
            print("{:d} 1".format(i+1))
        else:
            print("{:d} {:d}".format(i+1, i+1))
        if (n >> i) & 1: #odd number -> bit set
            if left: #left side
                for j in range(1, i+1):
                    print("{:d} {:d}".format(i+1, j+1))
            else: #right side
                for j in range(i-1, -1, -1):
                    print("{:d} {:d}".format(i+1, j+1))
            left = not(left) #change the side
            ones = ones + 1
    i = 30
    while ones:
        if left:
            print("{:d} 1".format(i+1))
        else:
            print("{:d} {:d}".format(i+1, i+1))
        ones = ones - 1
        i = i + 1

t = int(input())
for _ in range(t):
    n = int(input())
    print("Case #{:d}: ".format(_+1))
    pascalWalk(n)
