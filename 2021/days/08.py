from utils import getLines

def countOccurrences(filename):
    datas = getLines(filename)
    counter = 0
    for index in range(len(datas)):
        splitted = datas[index].split("|")
        for n in splitted[1].split():
            counter += 1 if len(n) == 2 or len(n) == 3 or len(n) == 4 or len(n) == 7 else 0
    return counter

testOne = countOccurrences('../inputs/08_input_exemple.txt')
print("Réponse test 1 : " + str(testOne) + " --> " + str(testOne == 26))

resultOne = countOccurrences('../inputs/08_input.txt')
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 383))
