def matchSim(l):
    m = 0; maxPrefix = "";
    for p in l:
        if len(p[0]) > m:
            m = len(p[0])
            maxPrefix = p[0]
    #print(maxPrefix)
    m = 0; maxSuffix = "";
    for p in l:
        if len(p[-1]) > m:
            m = len(p[-1])
            maxSuffix = p[-1]
    #print(maxSuffix)
    for p in l:
        for i in range(len(p[0])):
            if p[0][i]==maxPrefix[i]:
                continue
            return "*"
    maxSuffix = maxSuffix[::-1]
    for p in l:
        p[-1] = p[-1][::-1]
        for i in range(len(p[-1])):
            if p[-1][i]==maxSuffix[i]:
                continue
            return "*"
    maxSuffix = maxSuffix[::-1]
    maxMiddle = ''.join(''.join(p[i] for i in range(1, len(p)-1)) for p in l)
    return maxPrefix + maxMiddle + maxSuffix
    

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for i in range(n):
        l.append((input().split('*')))
    print("Case #{:d}: {:s}".format(_+1, matchSim(l)))
