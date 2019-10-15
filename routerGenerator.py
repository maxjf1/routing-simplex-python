from math import sqrt, pow


def max(a, b):
    return a if a > b else b


def readFile(path):
    file = open(path)
    customers = []
    for line in file:
        fields = line.replace("\n", "").split(" ")
        if(len(fields) < 6):
            continue
        while("" in fields):
            fields.remove("")
        customers.append(Customer(fields))

    return customers


class Customer:
    def __init__(self, fields):
        id, x, y, weigth, begin, end, _ = fields
        self.id = int(id)
        self.coords = (float(x), float(y))
        self.weigth = float(weigth)
        self.timeWindow = (float(begin), float(end))


class Route:
    customers = []
    demand = 0
    distance = 0
    endTime = 0

    # Gera ID unico para a rota
    def getRouteID(self):
        return ",".join(map(lambda customer: customer.id, self.customers))

    def addCustomer(self, customer):
        self.demand += customer.weigth
        self.endTime = max(customer.timeWindow[0], self.customers[-1].timeWindow[0])
        self.distance += sqrt(
            pow(customer.x - self.customers[-1].x) +
            pow(customer.y - self.customers[-1].y))
        self.customers.append(customer)
