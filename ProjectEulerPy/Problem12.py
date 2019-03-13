import numpy as np

def countFactors(element):
    cur = {}
    for i in range(1, int(np.sqrt(element))+1):
        if element % i == 0:
            if element / i not in cur.keys():
                cur[i] = element / i
    return len(cur) * 2


if __name__ == "__main__":
    sum = 0
    for i in range(1,10000000):
        sum = sum + i
        if (countFactors(sum)) > 500:
            print(sum)
            break
