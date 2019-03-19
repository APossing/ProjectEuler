def countingSundays(beginYear, endYear):
    curYear = 1900
    beginDay = 0
    curDay = 0
    while curYear <= endYear:
        if curYear == beginYear:
            beginDay = curDay
        if beginDay != 0:
            if curDay % 7 == 6:

        curDay += 30

        curDay += 30
        curDay += 30
        curDay += 30
        curDay += 31
        curDay += 31
        curDay += 31
        curDay += 31
        curDay += 31
        curDay += 31
        curDay += 31
        curDay += 28
        if curYear % 4 == 0:
            if curYear % 100 == 0:
                if curYear % 400 == 0:
                    curDay+= 1
            else:
                curDay+= 1
        curYear+= 1
    sTotal = int(curDay/7)
    sBegin = int((beginDay)/7)
    return sTotal-sBegin


if __name__ == '__main__':
    print(countingSundays(1901,2000))
