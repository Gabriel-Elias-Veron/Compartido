from sympy import *

a = Symbol("a")
b = Symbol("b")
# se puede presentar de difererntes formas las ecuaciones con nuemros decimales o 
#con fracciones...
c = 0.5*a ** 3 * b - 3*a*b ** 3\
     - 5*a ** 3 * b + 0.75*a*b ** 3 - (2/3)*a ** 3 * b

d = Rational(1,2)*a ** 3 * b - 3*a*b ** 3\
     - 5*a ** 3 * b + Rational(3,4)*a*b ** 3 - Rational(2,3)*a ** 3 * b

print(c)
print(d)

