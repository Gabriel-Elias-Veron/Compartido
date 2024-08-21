# Programa que tenga almacenados nombres de paises
# y que muestre los paises que tengan cierto tipos de letras

pais = ["Mexico", "Peru", "España", "Argentina", "Chile", "Bolivia", "Ecuador"]

for i in pais:
    if len(i) >= 6:
        print(i)