from Structs import Customer, Instance, Route


def readFile(path):
    file = open(path)
    return file.read()


def main():
    instance = Instance(readFile("./models/r101.txt"))
    instance.generateRoutes()
    


if __name__ == '__main__':
    main()
