print("Exercice 1")

def exerciceUn(filename):
    file = open(filename,'r')
    horizontal = 0
    depth = 0
    lines = file.read().splitlines()
    for line in lines:
        datas = line.split()
        if datas[0] == "forward":
            horizontal += int(datas[1])
        elif datas[0] == "up":
            depth -= int(datas[1])
        else:
            depth += int(datas[1])
    return depth * horizontal

test = exerciceUn('02_input_exemple.txt')
print("Réponse test : " + str(test) + " --> " + str(test == 150))

result = exerciceUn('02_input.txt')
print("Réponse : " + str(result) + " --> " + str(result == 1648020))



print("\nExercice 2")


def exerciceDeux(filename):
    file = open(filename,'r')
    horizontal = 0
    depth = 0
    aim = 0
    lines = file.read().splitlines()
    for line in lines:
        datas = line.split()
        if datas[0] == "forward":
            horizontal += int(datas[1])
            depth += aim * int(datas[1])
        elif datas[0] == "up":
            aim -= int(datas[1])
        else:
            aim += int(datas[1])
    return depth * horizontal

test = exerciceDeux('02_input_exemple.txt')
print("Réponse test : " + str(test) + " --> " + str(test == 900))

result = exerciceDeux('02_input.txt')
print("Réponse : " + str(result) + " --> " + str(result == 1759818555))
