#!/usr/bin/python

from gurobipy import *

try:

    # Create a new model
    m = Model("roteamento")

    custoRota = tuplelist([("rota1", 5), ("rota2", 15), ("rota3", 10)])
    rotaSelecionada = tuplelist([("rota1", 1), ("rota2", 0), ("rota3", 1)])
    rotaCliente = tuplelist([("rota1", "cliente1", 1), ("rota1", "cliente2", 1), ("rota1", "cliente3", 0)])
    a = m.addVars(rotaSelecionada, name="a")
    c = m.addVars(custoRota, name="c")
    x = m.addVars(rotaCliente, name="x")


except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')