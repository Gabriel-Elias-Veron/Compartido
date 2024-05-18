from sympy import *
#sumatorias
x, n, y = symbols("x n y")
a= summation(x, (n, 1, 8))
print(a)

b = summation(x + n*y, (n, 1, 5) )

print(b)


#serie de productosss

c = product(x,(n, 0, 6))# nos la devuelve en forma de potencia 
print(c)

d = product(x - n*y, (n, 0, 5))
print(d)