from sympy import *

x = Symbol("x")

a = plot((x**2 + 2), (x, 20, 20), title= "Parabola", xlabel="eje de x",
         ylabel="x**2 + 2")
pprint(a)

#xlabel y ylabel sirve para escribir cosas en la lado de la x e y...
# title se utiliza para para nombrar al grafico...