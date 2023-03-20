class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)
        print(f"Macaco {self.nome} comeu {comida}.")

    def ver_bucho(self):
        print(f"Macaco {self.nome} possui", *self.bucho, "em seu estômago.")

    def digerir(self):
        del(self.bucho[0])


nome1 = str(input("Nomeie o primeiro macaco: "))
nome2 = str(input("Nomeie o segundo macaco: "))

macaco1 = Macaco(nome1)
macaco2 = Macaco(nome2)

comidas = ["banana", "melancia", "goiaba", "mamão"]

for x in comidas:
    macaco1.comer(x)
    macaco1.ver_bucho()
    macaco1.digerir()

macaco2.comer(macaco1)
