class Macaco:
    def __init__(self):
        self.nome = None
        self.bucho = []

    def set_nome(self):
        self.nome = input("Nome do macaco: ")

    def comer(self, comida):
        if isinstance(comida, Macaco):
            print("Macaco não é canibal, não come macaco.")
        else:
            self.bucho.append(comida)
            print(f"Macaco {self.nome} comeu {comida}.")

    def ver_bucho(self):
        print(f"Macaco {self.nome} possui", *self.bucho, "em seu estômago.")

    def digerir(self):
        print(f"{self.nome} digeriu {self.bucho[0]}")
        del (self.bucho[0])


if __name__ == '__main__':
    macaco1 = Macaco()
    macaco2 = Macaco()

    comidas = ["banana", "melancia", "goiaba", "mamão"]
    macaco1.set_nome()
    macaco2.set_nome()

    for x in comidas:
        macaco1.comer(x)
        macaco1.ver_bucho()
        macaco1.digerir()

    macaco2.comer(macaco1)
