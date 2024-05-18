#calculo diferencial y integral
from sympy import *

t = Symbol("t")

eq = 5*t**2 + 2*t +8
#aplicamos la derivada con respecto a t

Deriv = Derivative(eq,t).doit()
print(Deriv)