#!/usr/bin/python

from gurobipy import *

try:

    # link:     https://www.dcc.fc.up.pt/~jpp/code/gurobi_book/vrp.py

    # Create a new model
    m = Model("roteamento")
    
    # Create variables
    
    R = {} #lista de rodas
    x = {}     
    c = {}
    
    for i in R:   
        x[i] = m.addVar(ub=1, vtype="I", name="x(%s)"%(i))
        
    # Set objective
    m.setObjective(quicksum(c[i]*x[i] for i in V), GRB.MINIMIZE)

    # Add constraint: x + 2 y + 3 z <= 4
    #m.addConstr(x + 2 * y + 3 * z <= 4, "c0")

    # Add constraint: x + y >= 1
    #m.addConstr(x + y >= 1, "c1")

    # Optimize model
    m.optimize()

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')