#!/usr/bin/python

from gurobipy import *
from Structs import Route, Instance, Customer
from main import readFile
try:
    
    instance = Instance(readFile("./models/c101.txt"))
    instance.generateRoutes(200)

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
    for i in R:               
        m.addConstr(quicksum(int(routes[i].isInRoute(j))*x[i] for j in J) >= 1, "Cliente esta na rota ")
    m.update()

    # Optimize model
    m.optimize()

    print "teste", x


except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError as e:
    print('Encountered an attribute error', e.message)