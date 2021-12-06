from utils import getLines

def traitement(datas, nbDays):
    while nbDays > 0:
        nbAppend = 0
        for i in range(len(datas)):
            datas[i] = int(datas[i]) - 1
            if int(datas[i]) < 0:
                datas[i] = 6
                nbAppend += 1
        while nbAppend > 0:
            datas.append(8)
            nbAppend -= 1
        nbDays -= 1
    return len(datas)

def getLanternfishCount(filename, nbDays):
    datas = getLines(filename)[0].split(",")
    dictionnaire = {}
    count = 0
    for i in range(len(datas)):

        if(datas[i] in dictionnaire):
            count += dictionnaire[datas[i]]
        else:
            copyNbJour = nbDays
            res = traitement([datas[i]], nbDays)
            count += res
            dictionnaire[datas[i]] = res
    return count
    

testOne = getLanternfishCount('../inputs/06_input_exemple.txt', 18)
print("Réponse test 1 partie 1 : " + str(testOne) + " --> " + str(testOne == 26))

testTwo = getLanternfishCount('../inputs/06_input_exemple.txt', 80)
print("Réponse test 2 partie 1 : " + str(testTwo) + " --> " + str(testTwo == 5934))

resultOne = getLanternfishCount('../inputs/06_input.txt', 80)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 373378))
