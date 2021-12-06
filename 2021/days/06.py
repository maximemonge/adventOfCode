from utils import getLines

def getLanternfishCount(filename, days):
    datas = getLines(filename)[0].split(",")
    lanternfishCounter = init()
    for number in datas:
        lanternfishCounter[int(number)] += 1
    while days:
        nbZeros = lanternfishCounter[0]
        for i in range(len(lanternfishCounter)):
            if i == 8:
                lanternfishCounter[i] = nbZeros
            else:
                lanternfishCounter[i] = lanternfishCounter[i + 1]
                if i == 6:
                    lanternfishCounter[i] += nbZeros
        days -= 1
    return sum(lanternfishCounter.values())

def init():
    dictionnary = {}
    for i in range(9):
        dictionnary[i] = 0
    return dictionnary
    

testOne = getLanternfishCount('../inputs/06_input_exemple.txt', 18)
print("Réponse test 1 : " + str(testOne) + " --> " + str(testOne == 26))

testTwo = getLanternfishCount('../inputs/06_input_exemple.txt', 80)
print("Réponse test 2 : " + str(testTwo) + " --> " + str(testTwo == 5934))

testThree = getLanternfishCount('../inputs/06_input_exemple.txt', 256)
print("Réponse test 3 : " + str(testThree) + " --> " + str(testThree == 26984457539))

resultOne = getLanternfishCount('../inputs/06_input.txt', 80)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 373378))

resultTwo = getLanternfishCount('../inputs/06_input.txt', 256)
print("Réponse partie 2 : " + str(resultTwo) + " --> " + str(resultTwo == 1682576647495))
