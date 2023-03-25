class NovoBichinhoVirtual:
    def __init__(self):
        self.nome = "Sem nome"
        self.fome = 100
        self.saude = 100
        self.idade = 0
        self.humor = (self.saude + self.fome) / 2

    def set_nome(self):
        self.nome = str(input("Insira o nome do bichinho virtual: "))
        print(f"O novo nome é {self.nome}")

    def perder_saude(self):
        self.saude -= 10
        print("Saúde atual:", self.saude)

    def perder_fome(self):
        self.fome -= 10
        print("Estou com fome.")
        self.perder_saude()

    def alimentar(self, comida: int):
        if self.fome >= 100:
            print(f"{self.nome} não está com fome")
        else:
            self.fome += comida
            if self.fome >= 100:
                self.fome = 100
            print(f"Alimentado.\nFome atual: {self.fome}")

    def brincar(self, tempo: int):
        self.humor += tempo
        if self.humor >= 100:
            self.humor = 100
        print(f"{self.nome} se divertiu. Seu humor agora é {self.humor}")

    def aniversario(self):
        self.idade += 1
        print(f"Feliz aniversário! Agora seu bichinho tem {self.idade} anos!")

    def get_nome(self):
        return self.nome

    def get_fome(self):
        return f"Fome: {self.fome}"

    def get_saude(self):
        return f"Saúde: {self.saude}"

    def get_idade(self):
        return f"{self.nome} tem {self.idade} ano(s)."

    def get_humor(self):
        if self.humor >= 100:
            return f"{self.nome} está muito feliz!! :D"
        elif 100 > self.humor >= 75:
            return f"{self.nome} está contente :)"
        elif 75 > self.humor >= 50:
            return f"{self.nome} está incomodado ;/"
        elif 50 > self.humor >= 25:
            return f"{self.nome} está triste :("
        else:
            return f"{self.nome} está deprimido x("
