from math import sqrt, pow
import random

# Helper function


def max(a, b):
    return a if a > b else b


def distance(coordsA, coordsB):
    return sqrt(
        pow(coordsA[0] - coordsB[0], 2) +
        pow(coordsA[1] - coordsB[1], 2))


class Instance:
    'Instancia do problema'
    customers = []
    routes = []
    vehicles = 0
    capacity = 0

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

    def addRoute(self, route):
        # print("ADD route", route.getId())
        for r in self.routes:
            if not route.getId() or r.getId() == route.getId():
                return
        self.routes.append(route)
        #print("Route: ", len(self.routes),
        #      "\tD:", round(route.distance, 2),
        #      "\tP:", route.demand,
        #      "\tT:", round(route.beginTime, 2), ":", round(route.endTime, 2),
        #      "\t", route.getId())

    def generateRoutes(self, ammount=20000):
        random.seed(42)
        self.routes = []
        customers = self.customers[1::]
        random.shuffle(customers)
        route = Route(self.customers[0])
        i = 0
        while(len(self.routes) < ammount):
            if(route.canAddCustomer(customers[i], self.capacity)):
                route.addCustomer(customers[i])
                customers.remove(customers[i])
            else:
                i += 1
            if(i >= len(customers)):
                route.closeRoute()
                self.addRoute(route)
                route = Route(self.customers[0])
                i = 0

            if(len(customers) == 0):
                customers = self.customers[1::]
                random.shuffle(customers)


class Customer:
    'Cliente'

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
    'Rota com informacoes'

    def __init__(self, base):
        self.customers = []
        self.demand = 0
        self.distance = 0
        self.beginTime = 0
        self.endTime = 0
        self.id = False
        self.customers = [base]

    def closeRoute(self):
        self.addCustomer(self.customers[0])
        self.beginTime = self.customers[1].timeWindow[0] - \
            self.customers[0].distanceOf(self.customers[1])

    # Gera ID unico para a rota
    def getId(self):
        if(self.id):
            return self.id

        id = " ".join(map(lambda customer: str(
            customer.id), self.customers[1:-2]))

        if(self.customers[-1].id == self.customers[0].id):
            self.id = id
        return id

    def isInRoute(self, customerId):
        for c in self.customers:
            if c.id == customerId:
                return True
        return False

    def addCustomer(self, customer):
        self.demand += customer.weigth
        dist = customer.distanceOf(self.customers[-1])
        self.endTime = max(
            customer.timeWindow[0], self.endTime) + dist + customer.serviceTime
        self.distance += dist
        self.customers.append(customer)

    def canAddCustomer(self, customer,  capacity):
        return self.demand + customer.weigth < capacity and self.endTime + customer.distanceOf(self.customers[-1]) < customer.timeWindow[1]
