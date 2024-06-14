# Archivo: shopping_list.py

class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self):
        item = input("Ingresa un artículo para la lista de compras: ")
        self.items.append(item)

    def view_list(self):
        print("Mi Lista de Compras:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")

    def delete_item(self):
        try:
            numero_item = int(input("Ingresa el número del artículo que deseas eliminar: "))
            del self.items[numero_item - 1]
        except (ValueError, IndexError):
            print("Número de artículo inválido.")

def PP_Ex2():
    # Crear una nueva lista de compras
    my_list = ShoppingList()

    # Agregar artículos a la lista
    while True:
        add_more = input("¿Deseas agregar más artículos a la lista de compras? (si/no): ")
        if add_more.lower() == "no":
            break
        my_list.add_item()

    # Ver la lista
    my_list.view_list()

    # Eliminar un artículo
    my_list.delete_item()

    # Ver la lista actualizada
    my_list.view_list()