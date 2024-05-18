from sympy import *

x = Symbol("x")
y = Symbol("y")

print(x+y+x-y)# si quiero poner 2y tengo que escribirlo de estra manera (2 * y)

a = expand((x+y)**2)# expand es una palabra reservada de la libreria sirve para reslver ecuaciones...
print(a)

