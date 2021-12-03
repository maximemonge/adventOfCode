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
