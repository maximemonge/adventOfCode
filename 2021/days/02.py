from utils import getLines

def calculate(filename, useAim):
    horizontal = 0
    depth = 0
    aim = 0
    steps = getLines(filename)
    for step in steps:
        direction, value = step.split()
        if direction == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        elif direction == "up":
            aim -= int(value)
        else:
            aim += int(value)
    if not useAim:
        depth = aim
    return depth * horizontal

testOne = calculate('../inputs/02_input_exemple.txt', False)
print("Réponse test : " + str(testOne) + " --> " + str(testOne == 150))

resultOne = calculate('../inputs/02_input.txt', False)
print("Réponse : " + str(resultOne) + " --> " + str(resultOne == 1648020))

testTwo = calculate('../inputs/02_input_exemple.txt', True)
print("Réponse test : " + str(testTwo) + " --> " + str(testTwo == 900))

resultTwo = calculate('../inputs/02_input.txt', True)
print("Réponse : " + str(resultTwo) + " --> " + str(resultTwo == 1759818555))
