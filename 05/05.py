def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()

def calculatePoints(filename):
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
                if str(x1) + "," + str(i) in dictionnary:
                    dictionnary[str(x1) + "," + str(i)] += 1
                else:
                    dictionnary[str(x1) + "," + str(i)] = 1
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                if str(i) + "," + str(y1) in dictionnary:
                    dictionnary[str(i) + "," + str(y1)] += 1
                else:
                    dictionnary[str(i) + "," + str(y1)] = 1
    print(dictionnary)
    for coord in dictionnary:
        if dictionnary[coord] >= 2:
            result += 1
    return result


testOne = calculatePoints('05_input_exemple.txt')
print("Réponse test partie 1 : " + str(testOne) + " --> " + str(testOne == 5))

resultOne = calculatePoints('05_input.txt')
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 72770))
