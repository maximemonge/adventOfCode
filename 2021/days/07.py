from utils import getLines

def getCheapestFuelCost(filename):
    datas = getLines(filename)[0].split(",")
    maximum = max(datas)
    cheapestFuelCost = -1
    for i in range(int(maximum)):
        fuel = 0
        for number in datas:
            fuel += abs(i - int(number))
        if cheapestFuelCost == -1:
            cheapestFuelCost = fuel
        elif fuel < cheapestFuelCost:
            cheapestFuelCost = fuel
    return cheapestFuelCost
    

testOne = getCheapestFuelCost('../inputs/07_input_exemple.txt')
print("Réponse test 1 : " + str(testOne) + " --> " + str(testOne == 37))

resultOne = getCheapestFuelCost('../inputs/07_input.txt')
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 347449))
