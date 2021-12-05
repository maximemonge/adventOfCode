from utils import getLines

def bingo(filename, strategy):
    datas = getLines(filename)
    numbers, players, sizeOfGrid = parseDatas(datas)
    return play(numbers, players, sizeOfGrid, strategy)

def parseDatas(datas):
    numbers = datas[0].split(",")
    players = []
    player = []
    sizeOfGrid = 0
    for i in range(1, len(datas)):
        if datas[i] == "" and player != []:
            players.append(player)
            player = []
        else:
            player += datas[i].split()
            if sizeOfGrid == 0:
                sizeOfGrid = len(player)
    players.append(player)
    return numbers, players, sizeOfGrid

def play(numbers, players, sizeOfGrid, strategy):
    playerScore = 0
    winners = []
    for number in numbers:
        for player in players:
            if player not in winners:
                player[:] = addCrossInPlayerGrid(number, player)
                playerScore = getPlayerScore(player, sizeOfGrid)
                if playerScore > 0:
                    winners.append(player)
                    if strategy == 1 or len(winners) == len(players):
                        return playerScore * int(number)

def addCrossInPlayerGrid(number, player):
    return [i if i != number else "X" for i in player]
    
def getPlayerScore(player, sizeOfGrid):
    victory = False
    score = 0
    line = []
    columns = [""] * sizeOfGrid
    for i in range(len(player)):
        if not victory:
            columns[i % sizeOfGrid] += player[i]
            victory, line = isWinningLine(i, sizeOfGrid, line, player)
        if player[i] != "X":
            score += int(player[i])
    if not victory:
        victory = isWinningColumn(columns, sizeOfGrid)
    return score if victory else 0

def isWinningLine(i, sizeOfGrid, line, player):
    if i % sizeOfGrid == 0 and i != 0:
        if line.count("X") == sizeOfGrid:
            return True, line
        line = []
    line.append(player[i])
    return False, line

def isWinningColumn(columns, sizeOfGrid):
    for i in range(sizeOfGrid):
        countX = 0
        for j in range(sizeOfGrid):
            if columns[i][j] == "X":
                countX += 1
        if countX == sizeOfGrid:
            return True
    return False


testOne = bingo('../inputs/04_input_exemple.txt', 1)
print("Réponse test partie 1 : " + str(testOne) + " --> " + str(testOne == 4512))

resultOne = bingo('../inputs/04_input.txt', 1)
print("Réponse partie 1 : " + str(resultOne) + " --> " + str(resultOne == 72770))

testTwo = bingo('../inputs/04_input_exemple.txt', 2)
print("Réponse test partie 2 : " + str(testTwo) + " --> " + str(testTwo == 1924))

resultTwo = bingo('../inputs/04_input.txt', 2)
print("Réponse partie 2 : " + str(resultTwo) + " --> " + str(resultTwo == 13912))
