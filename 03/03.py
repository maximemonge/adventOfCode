def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()

def getPowerConsumption(filename, bits):
    gammaRate = 0
    epsilonRate = 0
    sumOfBits = [0 for i in range(bits)]
    lines = getLines(filename)
    for line in lines:
        for bit in range(bits):
            sumOfBits[bit] += int(line[bit])
    for index in range(len(sumOfBits)):
        value = sumOfBits[index] > len(lines) / 2
        gammaRate += int(value) * (2 ** (bits - index - 1))
        epsilonRate += int(not value) * (2 ** (bits - index - 1))
    return gammaRate * epsilonRate

testOne = getPowerConsumption('03_input_exemple.txt', 5)
print("Réponse test : " + str(testOne) + " --> " + str(testOne == 198))

resultOne = getPowerConsumption('03_input.txt', 12)
print("Réponse : " + str(resultOne) + " --> " + str(resultOne == 1071734))


def getLifeSupportRating(filename, bits):
    oxygenGeneratorRating = 0
    cooScrubber = 0
    firstStepZero = []
    firstStepOne = []
    lines = getLines(filename)
    for line in lines:
        if line[0] == "1":
            firstStepOne.append(line)
        else:
            firstStepZero.append(line)
    if len(firstStepOne) > len(firstStepZero):
        oxygenGeneratorRating = traitment(firstStepOne, True, 1)
        cooScrubber = traitment(firstStepZero, False, 1)
    else:
        oxygenGeneratorRating = traitment(firstStepZero, True, 1)
        cooScrubber = traitment(firstStepOne, False, 1)
    return oxygenGeneratorRating * cooScrubber

def traitment(liste, useMax, index):
    ones = []
    zeros = []
    for element in liste:
        if element[index] == "1":
            ones.append(element)
        else:
            zeros.append(element)
    moreOnesThanZeros = len(ones) >= len(zeros)
    if useMax:
        liste = ones if moreOnesThanZeros else zeros
    else:
        liste = zeros if moreOnesThanZeros else ones
    if len(liste) > 1:
        return traitment(liste, useMax, index + 1)
    else:
        return getDecimalValue(liste[0])

def getDecimalValue(binary):
    decimal = 0
    for index in range(len(binary)):
        decimal += int(binary[index]) * (2 ** (len(binary) - index - 1))
    return decimal

testTwo = getLifeSupportRating('03_input_exemple.txt', 5)
print("Réponse test : " + str(testTwo) + " --> " + str(testTwo == 230))

resultTwo = getLifeSupportRating('03_input.txt', 12)
print("Réponse : " + str(resultTwo) + " --> " + str(resultTwo == 6124992))

