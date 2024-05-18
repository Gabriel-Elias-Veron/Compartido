from sympy import *

x = Symbol("x")
y = Symbol("y")
a = Symbol("a")
b = Symbol("b")

z = -10 * x ** (2 * a) * y ** b + 5 * x ** (2 * a) * y ** b\
     - 6 * x ** (2 * a) * y ** b + 11 * x ** (2 * a ) * y ** b

print(z)