def readData(filename):
    arr = []
    f = open(filename)
    for line in f:
        line = line.replace("\n","")
        line = line.replace("-", "0")
        arr.append([int(i) for i in line.split(",")])
    return arr


def runAlg(matrix):
    prevColumn = 0
    for row in range(0, len(matrix)):
        min = matrix[row][0]
        for column in range(0,row):
            if matrix[row][column] is not 0:
                if column < prevColumn:
                    matrix[row][column] = 0
                elif column < min:
                    column =


if __name__ == '__main__':
    data = readData("Resources/Problem107.txt")
    print(runAlg(data))