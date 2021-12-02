def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()

def getNumberOfIncreases(filename, slidings):
    increases = 0
    lines = getLines(filename)
    for index in range(len(lines) - slidings):
        previous = 0
        current = 0
        for sliding in range(slidings):
            previous += int(lines[index + sliding])
            current += int(lines[index + sliding + 1])
        increases += int(current) > int(previous)
    return increases

testOne = getNumberOfIncreases('01_input_exemple.txt', 1)
print("Réponse test partie 1 : " + str(testOne) + " --> " + str(testOne == 7))

resultOne = getNumberOfIncreases('01_input.txt', 1)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 1316))

testTwo = getNumberOfIncreases('01_input_exemple.txt', 3)
print("Réponse test partie 2 : " + str(testTwo) + " --> " + str(testTwo == 5))

resultTwo = getNumberOfIncreases('01_input.txt', 3)
print("Réponse partie 2 : " + str(resultTwo) + " --> " + str(resultTwo == 1344))
