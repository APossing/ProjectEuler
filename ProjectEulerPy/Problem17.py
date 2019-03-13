def getLettersInNumber(n):
    ones = n % 10
    wordString = ""
    tens = n % 100
    hundreds = n % 1000
    thousands = n % 10000
    if thousands >= 1000:
        #todo the rest.... but only need 1000 for now just simple
        return 11
    if hundreds >= 100:
        hundreds = int(hundreds/100)
        if hundreds is 1:
            wordString = "one"
        if hundreds is 2:
            wordString = "two"
        if hundreds is 3:
            wordString = "three"
        if hundreds is 4:
            wordString = "four"
        if hundreds is 5:
            wordString = "five"
        if hundreds is 6:
            wordString = "six"
        if hundreds is 7:
            wordString = "seven"
        if hundreds is 8:
            wordString = "eight"
        if hundreds is 9:
            wordString = "nine"
        wordString+="hundred"
        if tens > 0:
            wordString+="and"


    if tens > 9 and tens < 20:
        if tens is 10:
            wordString += "ten"
        elif tens is 11:
            wordString += "eleven"
        elif tens is 12:
            wordString += "twelve"
        elif tens is 13:
            wordString += "thirteen"
        elif tens is 14:
            wordString += "fourteen"
        elif tens is 15:
            wordString += "fifteen"
        elif tens is 16:
            wordString += "sixteen"
        elif tens is 17:
            wordString += "seventeen"
        elif tens is 18:
            wordString += "eighteen"
        elif tens is 19:
            wordString += "nineteen"

    else:
        tens = int(tens / 10)
        if tens is 2:
            wordString += "twenty"
        elif tens is 3:
            wordString += "thirty"
        elif tens is 4:
            wordString += "forty"
        elif tens is 5:
            wordString += "fifty"
        elif tens is 6:
            wordString += "sixty"
        elif tens is 7:
            wordString += "seventy"
        elif tens is 8:
            wordString += "eighty"
        elif tens is 9:
            wordString += "ninety"

        if ones is 1:
            wordString += "one"
        elif ones is 2:
            wordString += "two"
        elif ones is 3:
            wordString += "three"
        elif ones is 4:
            wordString += "four"
        elif ones is 5:
            wordString += "five"
        elif ones is 6:
            wordString += "six"
        elif ones is 7:
            wordString += "seven"
        elif ones is 8:
            wordString += "eight"
        elif ones is 9:
            wordString += "nine"
    return len(wordString)




if __name__ == "__main__":
    sum = 0
    for i in range(1,1001):
        sum += getLettersInNumber(i)
    print(sum)
