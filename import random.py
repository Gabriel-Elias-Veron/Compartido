import random

def adivina_el_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    intentos = 0
    max_intentos = 10  # Puedes ajustar el número máximo de intentos según tus preferencias

    print("¡Bienvenido a Adivina el Número!")
    print(f"Adivina un número entre 1 y 100. Tienes un máximo de {max_intentos} intentos.")

    while intentos < max_intentos:
        # Pedir al usuario que ingrese un número
        try:
            intento = int(input("Tu intento: "))
        except ValueError:
            print("¡Ups! Ingrese un número válido.")
            continue

        # Verificar si el número es correcto
        if intento == numero_secreto:
            print(f"¡Felicidades! ¡Has adivinado el número {numero_secreto} en {intentos + 1} intentos!")
            break
        elif intento < numero_secreto:
            print("El número es mayor. ¡Sigue intentando!")
        else:
            print("El número es menor. ¡Sigue intentando!")

        intentos += 1

    if intentos == max_intentos:
        print(f"¡Agotaste tus {max_intentos} intentos! El número secreto era {numero_secreto}.")

# Iniciar el juego
adivina_el_numero()
