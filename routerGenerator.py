

def readFile(path):
    file = open(path)
    customers = []
    for line in file:
        fields = line.replace("\n", "").split(" ")
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
