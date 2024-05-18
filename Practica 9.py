from sympy import *

x = Symbol("x")
y = Symbol("y")

a = expand((x+y)**5)
print(a)
b = expand((x-2)**4)
print(b)
c = expand((cos(x+y)), trig=True)# con trig podemos ver como se resuleve la identidad trigonometrica
print(c)
