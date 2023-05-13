from pulp import *

problema = LpProblem("Ejercicio_3", LpMaximize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

problema += x1 + 2*x2
problema += x1 + 3*x2 <= 5000
problema += x1 + x2 <= 3000
problema += x1 + x2 >= 1500

problema.solve()

print(f"El valor optimo se encuentra en x1 = {x1.varValue}, x2 = {x2.varValue}")
print(f"Con un minimo de Z = {(x1.varValue + 2*x2.varValue)}")