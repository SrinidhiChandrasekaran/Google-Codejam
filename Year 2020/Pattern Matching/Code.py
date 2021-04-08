def matchSim(l):
    #Find the max_prefix
    m = 0; maxPrefix = "";
    for p in l:
        if len(p[0]) > m:
            m = len(p[0])
            maxPrefix = p[0]
    #print(maxPrefix)
    #Find the max_suffix
    m = 0; maxSuffix = "";
    for p in l:
        if len(p[-1]) > m:
            m = len(p[-1])
            maxSuffix = p[-1]
    #print(maxSuffix)
    #Check if every prefix is itself a prefix of max_prefix. If not, return '*'
    for p in l:
        for i in range(len(p[0])):
            if p[0][i]==maxPrefix[i]:
                continue
            return "*"
    #Check if every suffix is itself a suffix of max_suffix. If not, return '*'
    maxSuffix = maxSuffix[::-1]
    for p in l:
        p[-1] = p[-1][::-1]
        for i in range(len(p[-1])):
            if p[-1][i]==maxSuffix[i]:
                continue
            return "*"
    maxSuffix = maxSuffix[::-1]
    #Joining the middlepart of all strings and replacing '*' with ''
    maxMiddle = ''.join(''.join(p[i] for i in range(1, len(p)-1)) for p in l)
    #Return the string
    return maxPrefix + maxMiddle + maxSuffix
    

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for i in range(n):
        #Input all the strings and tokenize them with '*'
        l.append((input().split('*')))
    print("Case #{:d}: {:s}".format(_+1, matchSim(l)))
