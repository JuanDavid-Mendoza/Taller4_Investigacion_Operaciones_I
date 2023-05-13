from pulp import *

problema = LpProblem("Ejercicio_3", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)

problema += 12*x1 + 8*x2 + 2*x3
problema += 6*x1 + 5*x2 + 4*x3 == 600
problema += x1 + x2 + x3 <= 300

problema.solve()

print(f"El valor optimo se encuentra en x1 = {x1.varValue}, x2 = {x2.varValue}, x3 = {x3.varValue}")
print(f"Con un minimo de Z = {(12*x1.varValue + 8*x2.varValue + 2*x3.varValue)}")