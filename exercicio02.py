class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        print("O lado do quadrado é", self.lado)

    def set_lado(self):
        self.lado = int(input("Insira o novo lado do quadrado: "))

    def retornar_lado(self):
        print("O lado do quadrado agora é", self.lado)

    def area(self):
        area = self.lado * self.lado
        print(f"A área do quadrado de lado {self.lado} é {area}.")


side = int(input("Insira o lado do quadrado: "))

quadrado = Quadrado(side)
quadrado.set_lado()
quadrado.retornar_lado()
quadrado.area()
