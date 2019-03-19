import numpy as np


def getSumOfFactors(n):
    sum = 1
    for j in range(2, int(np.sqrt(n)) + 1):
        if n % j == 0:
            if j != int(n / j):
                sum += j + n / j
            else:
                sum += j
    return sum


def computeAbundants(n):
    abundants = {}
    for i in range(1,n):
        if getSumOfFactors(i) > i:
            abundants[i] = True
    return abundants


def sumOfNon2SumAbundants(n, abundants):
    totalSum = 0
    for i in range(n):
        flag = False
        for j in abundants.keys():
            if j > i:
                break
            if i-j in abundants.keys():
                flag = True
        if flag is False:
            totalSum += i
    return totalSum


if __name__ == '__main__':
    abundants = computeAbundants(28123)
    print(sumOfNon2SumAbundants(28123, abundants))


