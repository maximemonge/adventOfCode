def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()

def getColumn(table, index):
    return [row[i] for row in table]

def bingo(filename):
    datas = getLines(filename)
    numbers = datas[0].split(",")
    players = []
    player = []
    nbPlayers = -1
    sizeOfGrid = 0
    for i in range(1, len(datas)):
        if datas[i] == "":
            if nbPlayers >= 0:
                players.append(player)
            player = []
            nbPlayers += 1
        else:
            player += datas[i].split()
            if sizeOfGrid == 0:
                sizeOfGrid = len(player)
    players.append(player)
    return play(numbers, players, sizeOfGrid)

def play(numbers, players, sizeOfGrid):
    winner = 0
    for number in numbers:
        for player in players:
            player[:] = [i if i != number else "X" for i in player]
            winner = verifyPlayer(player, sizeOfGrid)
            if winner != 0:
                return winner * int(number)

def verifyPlayer(player, sizeOfGrid):
    end = False
    score = 0
    column = []
    line = []
    for i in range(len(player)):
        if not end:
            if i % 5 == 0:
                if len(column) == 5:
                    if column.count("X") == sizeOfGrid:
                        end = True
                    column = []
                column.append(player[i])
                if i != 0:
                    if line.count("X") == sizeOfGrid:
                        end = True
                    line = []
            line.append(player[i])
        if player[i] != "X":
            score += int(player[i])
    return score if end else 0

testOne = bingo('04_input_exemple.txt')
print("Réponse test partie 1 : " + str(testOne) + " --> " + str(testOne == 4512))

resultOne = bingo('04_input.txt')
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 72770))
