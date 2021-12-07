from utils import getLines

def getCheapestFuelCost(filename, rule):
    datas = getLines(filename)[0].split(",")
    maximum = max(datas)
    cheapestFuelCost = -1
    for i in range(int(maximum)):
        fuel = 0
        for number in datas:
            if rule == 1:
                fuel += abs(i - int(number))
            else:
                fuel += sum(range(1, abs(i - int(number)) + 1))
        if cheapestFuelCost == -1:
            cheapestFuelCost = fuel
        elif fuel < cheapestFuelCost:
            cheapestFuelCost = fuel
    return cheapestFuelCost

testOne = getCheapestFuelCost('../inputs/07_input_exemple.txt', 1)
print("Réponse test 1 : " + str(testOne) + " --> " + str(testOne == 37))

testTwo = getCheapestFuelCost('../inputs/07_input_exemple.txt', 2)
print("Réponse test 2 : " + str(testTwo) + " --> " + str(testTwo == 168))

resultOne = getCheapestFuelCost('../inputs/07_input.txt', 1)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 347449))

resultTwo = getCheapestFuelCost('../inputs/07_input.txt', 2)
print("Réponse partie 2 : " + str(resultTwo) + " --> " + str(resultTwo == 98039527))
