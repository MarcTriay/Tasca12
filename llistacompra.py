# Archivo: shopping_list.py

class ShoppingList:
    def __init__(self):
        # Inicializa la lista de artículos como una lista vacía
        self.items = []

    def add_item(self):
        # Solicita al usuario que ingrese un artículo para agregar a la lista
        item = input("Ingresa un artículo para la lista de compras: ")
        # Agrega el artículo ingresado a la lista de artículos
        self.items.append(item)

    def view_list(self):
        # Muestra la lista de compras
        print("Mi Lista de Compras:")
        # Itera sobre los artículos en la lista, enumerándolos
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")

    def delete_item(self):
        try:
            # Solicita al usuario que ingrese el número del artículo a eliminar
            numero_item = int(input("Ingresa el número del artículo que deseas eliminar: "))
            # Elimina el artículo correspondiente de la lista
            del self.items[numero_item - 1]
        except (ValueError, IndexError):
            # Muestra un mensaje de error si el número ingresado es inválido
            print("Número de artículo inválido.")

def PP_Ex2():
    # Crear una nueva lista de compras
    my_list = ShoppingList()

    # Bucle para agregar artículos a la lista hasta que el usuario decida detenerse
    while True:
        add_more = input("¿Deseas agregar más artículos a la lista de compras? (si/no): ")
        if add_more.lower() == "no":
            break
        my_list.add_item()

    # Ver la lista de compras
    my_list.view_list()

    # Solicitar al usuario que elimine un artículo de la lista
    my_list.delete_item()

    # Ver la lista de compras actualizada
    my_list.view_list()
