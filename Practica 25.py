from sympy import *

x = Symbol("x")

eq1 = ((x - 1) / (x + 2) > 0)
conv = eq1.lhs
# como la ecuacion es una fraccion debemos obtener el numerador y el denominador

numer, denom = conv.as_numer_denom()# se utiliza para designar variables que luego van a ser usadas en otra parte del codigo
p1 = Poly(numer)
p2 = Poly(denom)
rel= eq1.rel_op
# solucionar la inecuacion
resul= solve_rational_inequalities([[((p1,p2), rel)]])
pprint(resul)
