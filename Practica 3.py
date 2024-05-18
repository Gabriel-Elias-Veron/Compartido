#Crear un programa que reciba un digito y lo escriba en palabra

digit = int(input("ingresa un numero: "))
letra = ["cero", "uno", "dos", "tres","cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

print("el digito {} es en letra {} ".format(digit, letra[digit]))

