from Structs import Customer, Instance, Route




def readFile(path):
    file = open(path)
    instance = Instance(file.read())
    return instance



def main():
    instance = readFile("./models/r101.txt")
    


if __name__ == '__main__':
    main()
