from math import sqrt, pow
import datetime

# Helper function
def max(a, b):
    'retorna maior valor'
    return a if a > b else b


def distance(coordsA, coordsB):
    'Calcula distancia entre duas coordenadas'
    return sqrt(
        pow(coordsA[0] - coordsB[0], 2) +
        pow(coordsA[1] - coordsB[1], 2))



def readFile(path):
    'Le conteudo de arquivo'
    file = open(path)
    return file.read()



def measure(callback):
    start = datetime.datetime.utcnow()
    callback()
    end = datetime.datetime.utcnow()
    duration = end - start
    print "Execution time: ", duration.total_seconds(), " seconds"



