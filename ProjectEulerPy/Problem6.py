import numpy as np

if __name__ == "__main__":
    arr = [i for i in range(1,101)]
    left = np.sum(arr)
    squaredSum = left**2
    sumOfSquared = np.sum([pow(i) for i in arr])
    print(squaredSum-sumOfSquared)


