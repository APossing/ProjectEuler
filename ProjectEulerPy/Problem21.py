import numpy as np


def getSumOfAmicableToN(n, sums):
    totalSum = 0
    for i in range(n):
        k = i
        v = sums[i]
        if v not in sums.keys():
            sums[v] = int(getSumOfFactors(v))
        if sums[v] == k and k != v:
            totalSum += v
    return totalSum


def getSumOfFactors(n):
    sum = 1
    for j in range(2, int(np.sqrt(n)) + 1):
        if n % j == 0:
            sum += j + n / j
    return sum


def getDictOfSums(n):
    sumOfFactor = {}
    for i in range(n):
        sumOfFactor[i] = int(getSumOfFactors(i))
    return sumOfFactor


if __name__ == '__main__':
    sums = getDictOfSums(10000)
    print(getSumOfAmicableToN(10000, sums))
