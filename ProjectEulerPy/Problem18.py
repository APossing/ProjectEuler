def readData(filename):
    arr = []
    f = open(filename)
    for line in f:
        line = line.replace("\n","")
        arr.append([int(i) for i in line.split(" ")])
    return arr


def runAlg(triange):
    for i in range(1, len(triange)):
        line = triange[len(triange) - i - 1]
        for j in range(0, len(line)):
            line[j] += max(triange[len(triange) - i][j], triange[len(triange) - i][j+1])

    return triange[0][0]


if __name__ == '__main__':
    data = readData("Resources/Problem18.txt")
    print(runAlg(data))
