from sympy import *

x, y = symbols("x y")

a = (x**2 + 2*x + 1) / ((x+1)*((sin(x)/cos(x))**2 + 1))
print(a.simplify())
print(a)
# primera opcion
X = 3
Y = 2

b = (X+Y)**2
print(b)
#segunda opcion
eq = (x+y)**2
c = eq.subs({x:3,y:2})
# hay dos formas de resolver las ecuaciones, se utiliza 
# una palabra clave de la libreria sympy subs que sirve 
# para sustituir una variable por un valor...
print(c)