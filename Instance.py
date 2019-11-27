from Customer import Customer
from Route import Route
import random


class Instance:
    'Instancia do problema'
    customers = []
    routes = []
    routesIds = []
    vehicles = 0
    capacity = 0

    def __init__(self, file, nCustomers=0):
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
            if nCustomers and len(self.customers) >= nCustomers+1:
                break

    def addRoute(self, route, it=0):
        'Adiciona rota a lista de rotas, se nao presente'
        if not route.getId() or route.getId() in self.routesIds:
            return False
        self.routes.append(route)
        self.routesIds.append(route.getId())
        # print it, "\tRoute: ", len(self.routes), \
        #       "\tD:", round(route.distance, 2), \
        #       "\tP:", route.demand, \
        #       "\tT:", round(route.beginTime, 2), ":", round(route.endTime, 2), \
        #       "\t", route.getId()
        return True

    def generateRoutes(self, ammount=20000, alpha=0.2, maxLoops =300000 ):
        'gera N rotas randomicas'
        random.seed(42)
        self.routes = []
        randomRange = int((len(self.customers)-1) * alpha)
        customers = self.customers[1::]
        customersIgnored = []
        route = Route(self.customers[0])
        def sortFunc(c): return c.distanceOf(route.customers[-1])
        customers.sort(key=sortFunc)
        it = 0
        while(len(self.routes) < ammount):
            it += 1
            if it == (maxLoops/2):
                print "Atingindo numero maximo de execucoes. abrindo alpha"
                randomRange = len(customers)-1
            if it > maxLoops:
                print "Maximo de execucoes sem resultados atingido.", len(self.routes), "rotas geradas"
                break

            i = random.randint(
                0, randomRange)
            nextCustomer = customers[i % len(customers)]
            if(route.canAddCustomer(nextCustomer, self.capacity)):
                route.addCustomer(nextCustomer)
                customers.remove(nextCustomer)
                customers.extend(customersIgnored)
                customersIgnored = []
                customers.sort(key=sortFunc)
            else:
                customersIgnored.append(nextCustomer)
                customers.remove(nextCustomer)

            if(len(customers) == 0):
                route.closeRoute()
                if(self.addRoute(route, it=it)):
                    it = 0
                route = Route(self.customers[0])
                customers.extend(customersIgnored)
                customersIgnored = []

                if(len(customers) == 0):
                    customers = self.customers[1::]
                customers.sort(key=sortFunc)
