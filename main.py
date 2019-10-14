import routerGenerator


def main():
    customers = routerGenerator.readFile("./models/r101.txt")
    print(customers)


if __name__ == '__main__':
    main()
