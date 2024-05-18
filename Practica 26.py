from sympy import *

x = Symbol("x")

eq = limit(1/x,x, S.Infinity)#infinito se puede escribir de dos formas con dos "oo" o con S.Infinity
print(eq)

eq1 = limit(1/x,x,0).doit()# primero va la fraccion despues va la variable a la cual le estoy aplicando limites "x" y despuesel limite
print(eq1)#.doit sirve para ejecucar la funcion 

eq2 = limit(sin (x) / x, x, 0).doit()
print(eq2)

