from Structs import Customer, Instance, Route
import datetime

def readFile(path):
    file = open(path)
    return file.read()


def main():
    instance = Instance(readFile("./models/c101.txt"))
    instance.generateRoutes()
    print(len(instance.routes))
    

def measure(callback):
    start = datetime.datetime.now()
    callback()
    end = datetime.datetime.now()
    duration = end - start
    print("Execution time: ", duration)

if __name__ == '__main__':
    measure(main)
