from sympy import *

x = Symbol("x")
# el codigo symbols sirve para nombrar varias incognitas, ejemplo del codigo:
# "x, y, z = symbols("x y z")"

eq1 = 5*x**3 - 3*x**2 - 6*x - 4
eq2 = - 8*x**3 + 2*x**2 - 3
eq3 = 7*x**2 - 9*x + 1
SumaDeEq = (eq1 + eq2 + eq3)
print(SumaDeEq)

y, a, b = symbols("y a b ")

eq01 = (Rational(1,2)*x**(a+1) - Rational(3,4)*y**(b-1) - Rational(1,6))
eq02 = (Rational(3,2)*x**(a+1) + Rational(1,3)*y**(b-1) + Rational(1,4))

SumaDeEq2= (eq01 + eq02)
print(SumaDeEq2)
