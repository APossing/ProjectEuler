def readData(filename):
    arr = []
    f = open(filename)
    for line in f:
        line = line.replace("\n","")
        line = line.replace("-", "0")
        arr.append([int(i) for i in line.split(",")])
    return arr


def isConnected(matrix, point1, point2, visited):
    if point1 in visited:
        return False
    if point1 == point2:
        return True
    visited.append(point1)
    left = point2 - 1
    right = point2
    cur = 0
    while left >= 0 or right < len(matrix[point1]):
        temp = left
        if cur % 2 == 0:
            if right < len(matrix[point1]):
                temp = right
                right += 1
            else:
                left -= 1
        else:
            if left < 0:
                temp = right
                right += 1
            else:
                left -= 1
        cur += 1
        if matrix[point1][temp] is not 0:
            if isConnected(matrix, temp, point2, visited) is True:
                return True
    return False


def runAlg(matrix):
    count = 0
    capacity = 0
    usedMatrix = []


    for rowIndex in range(0, len(matrix)):
        usedMatrix.append([0 for i in range(0, len(matrix[rowIndex]))])
        for columnIndex in range(0, rowIndex+1):
            if matrix[rowIndex][columnIndex] != 0:
                count += 1
                capacity += matrix[rowIndex][columnIndex]
    for i in range(0, count):
        max = 0
        maxColIndex = -1
        maxRowIndex = -1
        for rowIndex in range(0, len(matrix)):
            for columnIndex in range(0, rowIndex):
                if matrix[rowIndex][columnIndex] > max and usedMatrix[rowIndex][columnIndex] is 0:
                    max = matrix[rowIndex][columnIndex]
                    maxColIndex = columnIndex
                    maxRowIndex = rowIndex
        matrix[maxRowIndex][maxColIndex] = matrix[maxColIndex][maxRowIndex] = 0
        usedMatrix[maxRowIndex][maxColIndex] = usedMatrix[maxColIndex][maxRowIndex] = 1

        tempList = []
        if isConnected(matrix, maxRowIndex, maxColIndex, tempList) is False:
            matrix[maxRowIndex][maxColIndex] = matrix[maxColIndex][maxRowIndex] = max

    cap2 = 0
    for rowIndex in range(0, len(matrix)):
        for columnIndex in range(0, rowIndex):
            if matrix[rowIndex][columnIndex] != 0:
                cap2 += matrix[rowIndex][columnIndex]
    return capacity - cap2


if __name__ == '__main__':
    data = readData("Resources/Problem107.txt")
    print(runAlg(data))
