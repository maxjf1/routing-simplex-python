
#!/usr/bin/python

from gurobipy import *
from Structs import Route, Instance, Customer
from helpers import readFile, measure
import logging
from Instance import Instance
import sys

def main():
    try:
        file = sys.argv[1] if len(sys.argv) >1 else "./models/c101.txt"
        print "Running for instance " + file
        instance = Instance(readFile(file), 25)
        print "Generating routes..."
        measure(lambda : instance.generateRoutes(10000))

        # Create a new model
        m = Model("roteamento")
        
        R = [x for x in range(len(instance.routes))]
        J = [x for x in range(1, len(instance.customers))]
        x = {}   
        routes = instance.routes

        # Create variables
        for i in R:   
            x[i] = m.addVar(lb=0, ub=1, vtype="I", name="x%s"%(i))
        m.update()   

        # Set objective
        m.setObjective(quicksum(routes[i].distance*x[i] for i in R), GRB.MINIMIZE)
        m.update()   

        # Add constraint
        for i in range(1, len(instance.customers)):               
            m.addConstr(quicksum(int(routes[j].isInRoute(i)) * x[j] for j in R) == 1, "Cliente esta na rota x%s"%(i))
        m.update()

        m.addConstr(quicksum(x[i] for i in R) <= instance.vehicles, "Max veiculos")
        m.update()
        
        # Optimize model
        m.write("Modelo.lp")
        m.optimize()

        resultado = []
        soma = 0
        for i in range(len(m.getVars())):
            if(m.getVars()[i].x > 0):
                resultado.append(i)
                soma+= instance.routes[i].distance
        
        print "\nRoutes:" 
        for r in resultado:
            print instance.routes[r].getId()

        print "\nDistance:", soma

    except GurobiError as e:
        print('Error code ' + str(e.errno) + ": " + str(e))

    except AttributeError as e:
        print('Encountered an attribute error', e)

measure(main)
