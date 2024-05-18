from sympy import *

x, y = symbols("x  y")

eq1 = 2*x + 3*y -6
eq2 = 3*x + 2*y -12
a = solve((eq1,eq2), dict=True)
pprint(a)

respuesta1 = eq1.subs({x:24/5, y:-6/5})
pprint(respuesta1)
resp2 = eq2.subs({x:24/5, y:-6/5})
# si apaece un -15(recordando que adelante del menos quince hay un -1.33226762955019e) 
# es porque esta aproximado al resultado deseado en este caso el 0...
pprint(resp2)

# esta es otra forma de sustituir los valores de una ecuacion y
#  esta es mas directa y precisa porque toma la solucion general de la ecuacion anterior...
sol1 = solve((eq1, eq2), dict=True)
sol1 = sol1[0]
b = eq1.subs({x:sol1[x],y:sol1[y]})
print(b)
c= eq2.subs({x:sol1[x],y:sol1[y]})
print(c)