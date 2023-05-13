from pulp import *

problema = LpProblem("Ejercicio_1", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

problema += 4*x1 + x2
problema += 3*x1 + x2 == 3
problema += 4*x1 + 3*x2 >= 6
problema += x1 + 2*x2 <= 4

problema.solve()

print(f"El valor optimo se encuentra en x1 = {x1.varValue}, x2 = {x2.varValue}")
print(f"Con un minimo de Z = {(4*x1.varValue + x2.varValue)}")
