

def readFromFile(fileName):
    f = open(fileName)
    arr = []
    for line in f:
        current = line.replace("\n","")
        arrLine = []
        for letter in current:
            arrLine.append(int(letter))
        arr.append(arrLine)
    return arr



if __name__ == "__main__":
    arr = readFromFile("Resources/Problem13.txt")
    final = [0 for i in range(0,1000)]
    for column in range(49,-1,-1):
        sum = 0
        for row in arr:
            sum += row[column]
        final[49-column] = sum

    for i in range(0,300):
        final[i+1] += int (final[i] / 10)
        final[i] = final[i] % 10

    for i in range(300,0,-1):
        if final[i] != 0:
            for j in range(0,10):
                print(final[i-j])
            break

