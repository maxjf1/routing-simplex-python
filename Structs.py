from math import sqrt, pow

# Helper function


def max(a, b):
    return a if a > b else b


def distance(coordsA, coordsB):
    return sqrt(
        pow(coordsA[0] - coordsB[0]) +
        pow(coordsA[1] - coordsB[1]))


class Instance:
    customers = []
    routes = []

    def __init__(self, file):
        lines = file.split("\n")
        self.name = lines[0]
        data = lines[4].split(" ")
        while("" in data):
            data.remove("")
        self.vehicles = int(data[0])
        self.capacity = int(data[1])
        lines = lines[9::]

        for line in lines:
            fields = line.replace("\r", "").replace("\n", "").split(" ")
            while("" in fields):
                fields.remove("")
            if(len(fields) < 6):
                continue
            self.customers.append(Customer(fields))

    def generateRoutes(self, ammount=2000):
        route = Route(self.customers[0])

        sortedCustomers = self.customers
        sortedCustomers.sort(
            key=lambda c: c.timeWindow[1] - c.timeWindow[0])

        for customer in sortedCustomers:
            print(customer.id)

        self.routes.append(route)


class Customer:
    def __init__(self, fields):
        id, x, y, weigth, begin, end, serviceTime = fields
        self.id = int(id)
        self.coords = (float(x), float(y))
        self.weigth = float(weigth)
        self.timeWindow = (float(begin), float(end))
        self.serviceTime = int(serviceTime)

    def distanceOf(self, customer):
        return distance(self.coords, customer.coords)


class Route:
    customers = []
    demand = 0
    distance = 0
    endTime = 0

    def __init__(self, base):
        self.customers.append(base)
    # Gera ID unico para a rota

    def getRouteID(self):
        return " ".join(map(lambda customer: customer.id, self.customers))

    def isInRoute(self, customerId):
        for c in self.customers:
            if c.id == customerId: 
                return True
        return False
        
    def addCustomer(self, customer):
        self.demand += customer.weigth
        dist = customer.distanceOf(self.customers[-1])
        self.endTime = max(
            customer.timeWindow[0], self.customers[-1].timeWindow[0]) + dist + customer.serviceTime
        self.distance += dist
        self.customers.append(customer)
