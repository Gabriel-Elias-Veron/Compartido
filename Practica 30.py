from ast import Try
from sympy import *

def grad_ascent(x0,f1x,x):
    epsilon = 1e-6
    sept_size = 1e-4
    x_old = x0
    x_new = x_old + sept_size * f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + sept_size * f1x.subs({x:x_old}).evalf()

        return x_new

if __name__ == '__main__':
    f = input("ingresa una funcion de una variable: ")
    var = input("ingresa la variable para derivar: ")
    var0 = float("ingresa el valor iniciar de la variable: ")
    Try:
        f = symplify(f)
        except SymplifyError:
            print('has ingresado la funcion incorrectamente')
        else:
            var = Symbol("var")
            d = Derivative(f, var).doit()
            var_max = grad_ascent(var0, d, var)
            print('{0}: {1}'.format(var.name, var_max))
            print('el maximo valor es: {0}'.format(f.subs({var:var_max})))