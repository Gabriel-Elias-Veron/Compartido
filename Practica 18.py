from sympy import *

x, y = symbols("x y")

a = x**3 + 3*x**2*y + 3*x*y**2 + y**3
b = factor(a)
#la palabra factor sirve para factorizar a las ecuaciones...
print(b)