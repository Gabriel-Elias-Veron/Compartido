from sympy import *

x = Symbol("x")

a = plot((2*x + 3), (3*x + 1), legend = True, show=False,
         title= "Grafica de dos ecuaciones", 
         xlabel="eje x",
         ylabel="eje y")
c = a[0].line_color = "b"
d = a[1].line_color = "r"
a.show()
print(c, d)