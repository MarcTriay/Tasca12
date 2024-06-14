class Futbolista:
    def __init__(self, nom, edat):
        # Inicializa el nombre y la edad del futbolista
        self.nom = nom
        self.edat = edat

    def xerrar(self):
        # Método abstracto para hablar
        pass

    def mourem(self):
        # Método abstracto para moverse
        pass

    def quisoc(self):
        # Método para imprimir que es un futbolista
        print("Sóc un futbolista")


class Messi(Futbolista):
    def __init__(self, nom, edat):
        # Inicializa el nombre y la edad de Messi utilizando el constructor de la clase base
        super().__init__(nom, edat)

    def xerrar(self):
        # Implementa el método para que Messi hable
        print("Hola, sóc el Messi!")

    def mourem(self):
        # Implementa el método para que Messi se mueva con el balón
        print("Em moc amb el baló")

    def quisoc(self):
        # Implementa el método para que Messi se identifique
        print("Sóc el Messi")


class Ronaldo(Futbolista):
    def __init__(self, nom, edat):
        # Inicializa el nombre y la edad de Ronaldo utilizando el constructor de la clase base
        super().__init__(nom, edat)

    def xerrar(self):
        # Implementa el método para que Ronaldo hable
        print("Hola, sóc el Ronaldo!")

    def mourem(self):
        # Implementa el método para que Ronaldo se mueva driblando
        print("Em moc driblant")

    def quisoc(self):
        # Implementa el método para que Ronaldo se identifique
        print("Sóc el Ronaldo")


class Neymar(Futbolista):
    def __init__(self, nom, edat):
        # Inicializa el nombre y la edad de Neymar utilizando el constructor de la clase base
        super().__init__(nom, edat)

    def xerrar(self):
        # Implementa el método para que Neymar hable
        print("Oi, sóc el Neymar!")

    def mourem(self):
        # Implementa el método para que Neymar se mueva regateando
        print("Em moc regatejant")

    def quisoc(self):
        # Implementa el método para que Neymar se identifique
        print("Sóc el Neymar")

def pex4():
    # Programa Principal
    # Crea una lista de objetos de los futbolistas Messi, Ronaldo y Neymar
    a = [Messi("Leo", 34), Ronaldo("Cristiano", 36), Neymar("Neymar Jr.", 29)]

    # Itera sobre cada futbolista en la lista
    for e in a:
        # Llama a los métodos xerrar, mourem y quisoc de cada futbolista
        e.xerrar()
        e.mourem()
        e.quisoc()
