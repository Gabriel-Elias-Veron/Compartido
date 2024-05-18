from sympy import *

x = Symbol("x")
y = Symbol("y")

a = 3*x - (2*y - (5*x + 3* y))
#recordar de revisar los signos, 
# porque si falta uno da error se syntaxis...

print(a)

m, n = symbols("m n")
#siempre respetar el orden de las variables 
# si primero ponemos la m cuando tengamos que ponerla 
# dentro de los parentecis la m iria primero...
b = 4*m +((6*m - 3*n)-(9*n - 5*m)+(8*m-2*n))
print(b)

a, b = symbols("a b")

c = Rational(2,3)*a - \
    (Rational(-1,5)*b - (2*a - Rational(3,5)*b) + Rational(2,3)*a) - Rational(1,2)*b
print(c)