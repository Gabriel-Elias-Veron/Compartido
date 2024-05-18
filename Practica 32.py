from json.encoder import INFINITY
from sympy import *

x = Symbol("x")
p = exp(-(x-10)**2/2) / sqrt(2 * pi)
inte = Integral(p, (x,11,12)).doit().evalf()
inte1 = Integral(p, (x,oo,oo)).doit().evalf()
#doit sirve para ejecutar el calculo y evalf sirve para mostrar su forma digital
print(inte)
print(inte1)