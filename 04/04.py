def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()

def bingo(filename, strategy):
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
    return play(numbers, players, sizeOfGrid, strategy)

def play(numbers, players, sizeOfGrid, strategy):
    winner = 0
    winners = []
    for number in numbers:
        for player in players:
            if player not in winners:
                player[:] = [i if i != number else "X" for i in player]
                winner = verifyPlayer(player, sizeOfGrid)
                if winner != 0:
                    winners.append(player)
                    if strategy == 1:
                        return winner * int(number)
                    else:
                        if len(winners) == len(players):
                            return winner * int(number)

def verifyPlayer(player, sizeOfGrid):
    end = False
    score = 0
    line = []
    columns = [""]*5
    for i in range(len(player)):
        if not end:
            columns[i % sizeOfGrid] += player[i]
            if i % sizeOfGrid == 0:
                if i != 0:
                    if line.count("X") == sizeOfGrid:
                        end = True
                    line = []
            line.append(player[i])
        if player[i] != "X":
            score += int(player[i])
    if not end:
        end = columnWin(columns, sizeOfGrid)
    return score if end else 0

def columnWin(columns, sizeOfGrid):
    for i in range(sizeOfGrid):
        countX = 0
        for j in range(sizeOfGrid):
            if columns[i][j] == "X":
                countX += 1
        if countX == sizeOfGrid:
            return True
    return False


testOne = bingo('04_input_exemple.txt', 1)
print("Réponse test partie 1 : " + str(testOne) + " --> " + str(testOne == 4512))

resultOne = bingo('04_input.txt', 1)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 72770))

testTwo = bingo('04_input_exemple.txt', 2)
print("Réponse test partie 2 : " + str(testTwo) + " --> " + str(testTwo == 1924))

resultTwo = bingo('04_input.txt', 2)
print("Réponse partie 2 : " + str(resultTwo) + " --> " + str(resultTwo == 13912))
