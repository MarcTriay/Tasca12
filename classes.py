class Futbolista:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def xerrar(self):
        pass

    def mourem(self):
        pass

    def quisoc(self):
        print("Sóc un futbolista")


class Messi(Futbolista):
    def __init__(self, nom, edat):
        super().__init__(nom, edat)

    def xerrar(self):
        print("Hola, sóc el Messi!")

    def mourem(self):
        print("Em moc amb el baló")

    def quisoc(self):
        print("Sóc el Messi")


class Ronaldo(Futbolista):
    def __init__(self, nom, edat):
        super().__init__(nom, edat)

    def xerrar(self):
        print("Hola, sóc el Ronaldo!")

    def mourem(self):
        print("Em moc driblant")

    def quisoc(self):
        print("Sóc el Ronaldo")


class Neymar(Futbolista):
    def __init__(self, nom, edat):
        super().__init__(nom, edat)

    def xerrar(self):
        print("Oi, sóc el Neymar!")

    def mourem(self):
        print("Em moc regatejant")

    def quisoc(self):
        print("Sóc el Neymar")

def pex4():

#    Programa Principal
    a = [Messi("Leo", 34), Ronaldo("Cristiano", 36), Neymar("Neymar Jr.", 29)]

    for e in a:
        e.xerrar()
        e.mourem()
        e.quisoc()

