
#!/usr/bin/python

from gurobipy import *
from Structs import Route, Instance, Customer
from helpers import readFile
import logging
from Instance import Instance
import sys

try:
    file = sys.argv[1] if len(sys.argv) > 2 else "./models/c101.txt"
    instance = Instance(readFile("./models/c101.txt"))
    instance.generateRoutes(1000)

    # Create a new model
    m = Model("roteamento")
    
    R = [x for x in range(len(instance.routes))]
    J = [x for x in range(1, len(instance.customers))]
    x = {}   
    routes = instance.routes

    #print("Custo rota", routes[0].distance)

    # Create variables
    for i in R:   
        x[i] = m.addVar(lb=0, ub=1, vtype="I", name="x(%s)"%(i))
    m.update()   

    # Set objective
    m.setObjective(quicksum(routes[i].distance*x[i] for i in R), GRB.MINIMIZE)
    m.update()   

    #print "TESTE", routes[67].distance

    # Add constraint
    for i in range(1, len(instance.customers)):               
        m.addConstr(quicksum(int(routes[j].isInRoute(i)) * x[j] for j in R) >= 1, "Cliente esta na rota ")
    m.update()

    m.addConstr(quicksum(x[i] for i in R) <= instance.vehicles, "Max veiculos")
    m.update()
    
    # Optimize model
    m.optimize()

    resultado = []
    soma = 0
    for i in range(len(m.getVars())):
        if(m.getVars()[i].x > 0):
            resultado.append(i)
            soma+= instance.routes[i].distance
    
    for r in resultado:
        print(instance.routes[r].getId())

    print "Distance:", soma

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError as e:
    print('Encountered an attribute error', e)
