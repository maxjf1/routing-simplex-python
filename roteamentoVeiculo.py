#!/usr/bin/python

from gurobipy import *
from Structs import Route

try:
 
    # Create a new model
    m = Model("roteamento")
    
    R = {} # lista de rotas
    J = {1, 2, 3, 5, 100} # lista de clientes  
    x = {}     
    c = {}
    
    # Create variables
    for i in R:   
        x[i] = m.addVar(ub=1, vtype="I", name="x(%s)"%(i))
    m.update()   

    # Set objective
    m.setObjective(quicksum(R[i].custo()*x[i] for i in R), GRB.MINIMIZE)
    m.update()   

    # Add constraint
    for i in R:         
        model.addConstr(quicksum(int(R[i].isInRoute(j))*x[i] for j in J) == 1, "Cliente (%s) esta na rota (%s)"%(j, i))
    m.update()

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
    print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')