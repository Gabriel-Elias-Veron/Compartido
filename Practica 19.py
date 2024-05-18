from sympy import *

x = Symbol("x")

a = x**2 + 3*x + 2
c = solve(a)

print(c)

ab = x**2 + 5*x + 4
d = solve(ab, dict=True)#con este codigo obtenemos el resultado de la ecuacion cuadratica
print(d)

ac = -4**2 + 5*-4 + 4
print(ac)


ad = x**2 + x + 1
problem = solve(ad, dict=True)
print(problem)

ae = -1/2 - sqrt(3)*I/2**2 + -1/2 - sqrt(3)*I/2 + 1
print(ae)



a, b, c = symbols("a b c")
af = a*x**2 + b*x + c
eq = solve(af, x, dict = True)# me devuelve la formula para resolver "x"
print(eq)

