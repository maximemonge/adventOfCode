def getLines(filename):
    file = open(filename,'r')
    return file.read().splitlines()