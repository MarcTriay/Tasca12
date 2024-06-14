import random

# Lista de palabras para adivinar
palabras = ["python", "programacion", "computadora", "teclado", "pantalla"]

# Función para elegir una palabra al azar de la lista
def elegir_palabra():
    return random.choice(palabras)

# Función principal del juego
def px1():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    intentos = 6  # Número de intentos permitidos

    while intentos > 0:
        mostrar_palabra = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print("Paraula: ", " ".join(mostrar_palabra))
        print(f"Intents restants: {intentos}")

        letra = input("Adivina una lletra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introdueix una única lletra.")
            continue

        if letra in letras_adivinadas:
            print("Has adivinat la lletra.")
            continue

        letras_adivinadas.add(letra)
        if letra in palabra:
            print("¡Ben fet! La lletra está dins la paraula.")
            if set(palabra).issubset(letras_adivinadas):
                print(f"Felicitats! Has adivinat la paraula: {palabra}")
                break
        else:
            intentos -= 1
            print("Hem sap greu, la lletra no está en la paraula.")

        if intentos == 0:
            print(f"Has perdut. La paraula era: {palabra}")
