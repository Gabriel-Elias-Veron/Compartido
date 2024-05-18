from sympy import * 
from sympy.core.sympify import SympifyError# esta sirve para saber cual es el error por el cual no podes resolver ña ecuacion

def derivada(f, var):
    var = Symbol(var)
    d = Derivative(f, var).doit()
    print(d)

if __name__ == "__main__":

    f = input("ingresa la ecuacion que quieres derivar: ")   
    var = input("ingresa la variable con la que quieres derivarla: ")

    try:
    f = sympify(f)
    else SympifyError:
        print("la funcion es invalida")
    else:
        derivada(f, var)
# es una calculadora de ecuaciones pero en visual studio no funciona