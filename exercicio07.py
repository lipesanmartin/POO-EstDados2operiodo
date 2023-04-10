class BichinhoVirtual:
    def __init__(self):
        self.nome = "Sem nome"
        self.fome = 100
        self.saude = 100
        self.idade = 0

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

    def alimentar(self):
        if self.fome >= 100:
            print("Fome: ", self.fome)
        else:
            self.fome += 10
            print(f"Alimentado.\nFome: {self.fome}")

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
