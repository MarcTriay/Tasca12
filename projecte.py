import ahorcado
import juego
import llistacompra
import classes
import scraping
import ex6


def menu():
    op = 0
    while op < 1 or op > 7:
        print("""
        \n
        Programa Principal
        1. Llistes
        2. Fitxers
        3. Joc
        4. Classes
        5. Aplicació Llibreria
        6. Servei web
        7. Sortir        
        """)
        op = int(input("Introdueix una opció: "))
        if op <1 or op >7:
            print("Opció no valida, torni a elegir una opció \n")
        else:
            return op

#La primera funció a desenvolupar ha de permetre treballar amb llistes, números aleatoris

#P.Principal
op= 1
while op!=7:
    op = menu()
    match op:
        case 1:
            ahorcado.px1()
        case 2:
            llistacompra.PP_Ex2()
        case 3:
            juego.PP_Ex3()
        case 4:
            classes.pex4()
        case 5:
            scraping.PP_ex5()
        case 6:
            ex6.iniciar_servidor_django()
        case 7:
            print("Gracies per utilitzar el programa,SALUD!")
        case other:
            print("Opció no valida")