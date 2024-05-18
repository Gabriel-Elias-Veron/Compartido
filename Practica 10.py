from sympy import *

x= Symbol("x")
y=Symbol("y")
a = simplify((3 * x - x * y - 3) / x)
print(a)

from sympy import *
x = Symbol("x")# sirve para sacer las razones trigonometricas
a = sin(x)/cos(x)
a.simplify()
print(a)
