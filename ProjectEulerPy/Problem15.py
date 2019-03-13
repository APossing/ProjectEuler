#Lattice paths
import time

mainDict = {}
def runProblem(n, curx, cury):
    if (curx,cury) in mainDict.keys():
        return mainDict[(curx,cury)]
    if n < curx or n < cury:
        return 0
    if n is curx and n is cury:
        return 1
    num = runProblem(n,curx+1,cury) + runProblem(n,curx,cury+1)
    mainDict[(curx,cury)] = num
    return num


if __name__ == "__main__":
    start = time.time()
    print(runProblem(20,0,0))
    end = time.time()
    print(end-start)