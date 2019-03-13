import time
import numpy as np

def runProblem(n):
    arr = [0 for i in range(0, int(np.log10(n))+1000)] #TODO I dont know why just yet, need to investigate why 1000 works
    arr[0] = 1
    for i in range(1,n+1):
        arr = [j*2 for j in arr]
        for j in range(0,len(arr)-1):
            arr[j+1] += int(arr[j] / 10)
            arr[j] = arr[j] % 10
    return np.sum(arr)




if __name__ == "__main__":
    start = time.time()
    print(runProblem(1000))
    end = time.time()
    print(end-start)

