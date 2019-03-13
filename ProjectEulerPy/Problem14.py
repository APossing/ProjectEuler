masterDict = {}

def problem(n):
    if n in masterDict.keys():
        return masterDict[n]
    if n <= 1:
        return 1
    if n % 2 is 0:
        cur = 1 + problem(int(n/2))
        masterDict[n] = cur
        return cur
    cur = 1 + problem(3*n+1)
    masterDict[n] = cur
    return cur



if __name__ == "__main__":
    max = 0
    maxIndex = 0
    for i in range(0,1000000):
        cur = problem(i)
        masterDict[i] = cur
        if cur > max:
            max = cur
            maxIndex = i
    print(max)
    print(maxIndex)