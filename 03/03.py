def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()

def getDecimalValue(binary):
    decimal = 0
    for index in range(len(binary)):
        decimal += int(binary[index]) * (2 ** (len(binary) - index - 1))
    return decimal

def getPowerConsumption(filename, bits):
    gammaRate = 0
    epsilonRate = 0
    sumOfBits = [0 for i in range(bits)]
    binaries = getLines(filename)
    for binary in binaries:
        for bit in range(bits):
            sumOfBits[bit] += int(binary[bit])
    for index in range(len(sumOfBits)):
        value = sumOfBits[index] > len(binaries) / 2
        gammaRate += int(value) * (2 ** (bits - index - 1))
        epsilonRate += int(not value) * (2 ** (bits - index - 1))
    return gammaRate * epsilonRate

def getLifeSupportRating(filename):
    oxygenGeneratorRating = 0
    cooScrubber = 0
    zeros = []
    ones = []
    binaries = getLines(filename)
    for binary in binaries:
        if binary[0] == "1":
            ones.append(binary)
        else:
            zeros.append(binary)
    if len(ones) > len(zeros):
        oxygenGeneratorRating = traitment(ones, True, 1)
        cooScrubber = traitment(zeros, False, 1)
    else:
        oxygenGeneratorRating = traitment(zeros, True, 1)
        cooScrubber = traitment(ones, False, 1)
    return oxygenGeneratorRating * cooScrubber

def traitment(binaries, useMax, index):
    ones = []
    zeros = []
    for binary in binaries:
        if binary[index] == "1":
            ones.append(binary)
        else:
            zeros.append(binary)
    moreOnesThanZeros = len(ones) >= len(zeros)
    if useMax:
        binaries = ones if moreOnesThanZeros else zeros
    else:
        binaries = zeros if moreOnesThanZeros else ones
    if len(binaries) > 1:
        return traitment(binaries, useMax, index + 1)
    else:
        return getDecimalValue(binaries[0])

testOne = getPowerConsumption('03_input_exemple.txt', 5)
print("Réponse test partie 1 : " + str(testOne) + " --> " + str(testOne == 198))

resultOne = getPowerConsumption('03_input.txt', 12)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 1071734))

testTwo = getLifeSupportRating('03_input_exemple.txt')
print("Réponse test partie 2 : " + str(testTwo) + " --> " + str(testTwo == 230))

resultTwo = getLifeSupportRating('03_input.txt')
print("Réponse partie 2 : " + str(resultTwo) + " --> " + str(resultTwo == 6124992))

