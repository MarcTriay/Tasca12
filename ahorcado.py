import random

# Lista de palabras para adivinar
palabras = ["python", "programacion", "computadora", "teclado", "pantalla"]

# Función para elegir una palabra al azar de la lista
def elegir_palabra():
    return random.choice(palabras)

# Función principal del juego
def px1():
    # Elige una palabra aleatoria de la lista
    palabra = elegir_palabra()
    # Conjunto para almacenar las letras adivinadas
    letras_adivinadas = set()
    # Número de intentos permitidos
    intentos = 6

    while intentos > 0:
        # Crea una lista que muestra la palabra con letras adivinadas y guiones para las no adivinadas
        mostrar_palabra = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print("Paraula: ", " ".join(mostrar_palabra))
        print(f"Intents restants: {intentos}")

        # Solicita al usuario que adivine una letra
        letra = input("Adivina una lletra: ").lower()
        
        # Verifica que el input es una única letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introdueix una única lletra.")
            continue

        # Verifica si la letra ya ha sido adivinada
        if letra in letras_adivinadas:
            print("Has adivinat la lletra.")
            continue

        # Añade la letra adivinada al conjunto
        letras_adivinadas.add(letra)

        # Verifica si la letra está en la palabra
        if letra in palabra:
            print("¡Ben fet! La lletra está dins la paraula.")
            # Verifica si todas las letras de la palabra han sido adivinadas
            if set(palabra).issubset(letras_adivinadas):
                print(f"Felicitats! Has adivinat la paraula: {palabra}")
                break
        else:
            # Reduce el número de intentos si la letra no está en la palabra
            intentos -= 1
            print("Hem sap greu, la lletra no está en la paraula.")

        # Si se agotan los intentos, el usuario pierde
        if intentos == 0:
            print(f"Has perdut. La paraula era: {palabra}")
