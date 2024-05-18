from sympy import *
x = Symbol('x')
f = abs(x - 5)
inte = Integral(f, (x, -5, 5)).doit()
print(inte)

u = Symbol('u')

gu = (u**2 - 1)/(u**2 + 1)
gx = Integral(gu, (u, 2*x, 3*x)).doit()
deri = Derivative(gx, x).doit()
pprint(deri)