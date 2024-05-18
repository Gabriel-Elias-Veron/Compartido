from sympy import *

x = Symbol('x')

eq = x**5 - 30*x**3 + 50*x
deri = Derivative(eq, x).doit()
print(eq, deri)
puntos_criticos = solve(deri)
#los puntos criticos
p1 = puntos_criticos[0]
p2 = puntos_criticos[1]
p3 = puntos_criticos[2]
p4 = puntos_criticos[3]
#segunda derivada de la funcion
eq2 = Derivative(eq,x,2).doit()
#sustituir cada una de las ecuaciones 
subs = eq2.subs({x:p1}).evalf()
print(subs)
subs1 = eq2.subs({x:p2}).evalf()
print(subs1)
subs2 = eq2.subs({x:p3}).evalf()
print(subs2)
subs3 = eq2.subs({x:p4}).evalf()
print(subs3)

