from helpers import max

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
        'Finaliza uma rota, adicionando o ponto de partida ao final e calculando valores'
        self.addCustomer(self.customers[0])
        self.beginTime = self.customers[1].timeWindow[0] - \
            self.customers[0].distanceOf(self.customers[1])

    def getId(self):
        'Gera ID unico para a rota, composto pelos IDs dos clientes presentes nela. Realiza cache do valor se possivel'

        if(self.id):
            return self.id

        id = " ".join(map(lambda customer: str(
            customer.id), self.customers[1:-2]))

        if(self.customers[-1].id == self.customers[0].id):
            self.id = id
        return id

    def isInRoute(self, customerId):
        'Verifica se um cliente esta na rota'
        for c in self.customers:
            if c.id == customerId:
                return True
        return False

    def addCustomer(self, customer):
        'Adiciona cliente a rota'
        self.demand += customer.weigth
        dist = customer.distanceOf(self.customers[-1])
        self.endTime = max(
            customer.timeWindow[0], self.endTime) + dist + customer.serviceTime
        self.distance += dist
        self.customers.append(customer)

    def canAddCustomer(self, customer,  capacity):
        'Verifica se um cliente pode ser adicionado na rota'
        return self.demand + customer.weigth < capacity and self.endTime + customer.distanceOf(self.customers[-1]) < customer.timeWindow[1]
