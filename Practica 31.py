#calculo integral

from re import X
from sympy import *

x, k =symbols('x k')

f = k*x 
inte = Integral(f, x).doit()
print(inte)

inte2 = Integral(f, (x, 0, 2)).doit()
print(inte2)

