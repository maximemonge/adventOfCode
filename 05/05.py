def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()

def calculatePoints(filename, diagonals):
    lines = getLines(filename)
    dictionnary = {}
    result = 0
    for line in lines:
        coord1, coord2 = line.split(" -> ")
        x1, y1 = coord1.split(",")
        x2, y2 = coord2.split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                dictionnary = addInDict(dictionnary, x1, i)
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                dictionnary = addInDict(dictionnary, i, y1)
        elif diagonals:
            if abs(x1 - x2) == abs(y1 - y2):
                for i in range(abs(x1 - x2) + 1):
                    if min(x1, x2) == min(y1, y2) and max(x1, x2) == min(y1, y2):
                        dictionnary = addInDict(dictionnary, min(x1, y1) + i, max(x2, y2) - i)
                    else:
                        dirX = 1
                        dirY = 1
                        if x1 > x2:
                            dirX = -1
                        if y2 > y1:
                            dirY = -1
                        dictionnary = addInDict(dictionnary, x1 + i * dirX, y1 - i * dirY)
    for coord in dictionnary:
        if dictionnary[coord] >= 2:
            result += 1
    return result

def addInDict(dictionnary, x, y):
    if str(x) + "," + str(y) in dictionnary:
        dictionnary[str(x) + "," + str(y)] += 1
    else:
        dictionnary[str(x) + "," + str(y)] = 1
    return dictionnary


testOne = calculatePoints('05_input_exemple.txt', False)
print("Réponse test partie 1 : " + str(testOne) + " --> " + str(testOne == 5))

resultOne = calculatePoints('05_input.txt', False)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 6687))

testTwo = calculatePoints('05_input_exemple.txt', True)
print("Réponse test partie 1 : " + str(testTwo) + " --> " + str(testTwo == 12))

resultTwo = calculatePoints('05_input.txt', True)
print("Réponse partie 1 : " + str(resultTwo) + " --> " + str(resultTwo == 19851))
