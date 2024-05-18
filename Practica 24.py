from sympy import *
x = Symbol("x")

ineq_obj = x**2 + 2 < 0
conv = ineq_obj.lhs# Con lhs nos permite convertir la ecuacion en un objeto...
p = Poly(conv,x)# Con este codigo hacemos un objeto de polinomio...(x**2 + 2)
rel = ineq_obj.rel_op# con este codigo hacemos que la inecuaacion sea una relacion...(<)
respuesta1 = solve_poly_inequality(p,rel)# si al imprimir no sale nada significa que el resultado de la ecuacion no es menor a 0
print(respuesta1)

eq=plot(x**2 + 2)
pprint(eq)