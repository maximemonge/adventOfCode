print("Exercice 1")

def exerciceUn(filename):
    file = open(filename,'r')
    increases = 0
    lines = file.read().splitlines()
    for index in range(len(lines) - 1):
        increases += int(lines[index + 1]) > int(lines[index])
    return increases

test = exerciceUn('01_input_exemple.txt')
print("Réponse test : " + str(test) + " --> " + str(test == 7))

result = exerciceUn('01_input.txt')
print("Réponse : " + str(result) + " --> " + str(result == 1316))



print("\nExercice 2")

def exerciceDeux(filename):
    file = open(filename,'r')
    increases = 0
    lines = file.read().splitlines()
    for index in range(len(lines) - 3):
        old = int(lines[index]) + int(lines[index + 1]) + int(lines[index + 2])
        new = int(lines[index + 1]) + int(lines[index + 2]) + int(lines[index + 3])
        increases += int(new) > int(old)
    return increases

test = exerciceDeux('01_input_exemple.txt')
print("Réponse test : " + str(test) + " --> " + str(test == 5))

result = exerciceDeux('01_input.txt')
print("Réponse : " + str(result) + " --> " + str(result == 1344))
