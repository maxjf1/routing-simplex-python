from helpers import distance

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