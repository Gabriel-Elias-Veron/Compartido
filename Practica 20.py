from sympy import *

a, u, t, s = symbols("a u t s ")

eq = u*t + Rational(1,2)*a*t**2 - s
eq1 =solve(eq, t, dict=True)
print(eq1)#-u - sqrt(2*a*s + u**2))/a
pprint(eq1)# imprime en forma de grafico

