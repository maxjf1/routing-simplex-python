from Customer import Customer
from Route import Route
import random

class Instance:
    'Instancia do problema'
    customers = []
    routes = []
    vehicles = 0
    capacity = 0

    def __init__(self, file):
        'Le conteudo do arquivo de instancia'
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
        'Adiciona rota a lista de rotas, se nao presente'
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
        'gera N rotas randomicas'
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

