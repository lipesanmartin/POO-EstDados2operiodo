class BichinhoVirtual:
    def __init__(self):
        self.nome = "Sem nome"
        self.fome = False
        self.saude = 100
        self.idade = 0

    def alterar_nome(self):
        self.nome = str(input("Insira o nome do bichinho virtual: "))
        print(f"O novo nome é {self.nome}")

    def perder_saude(self):
        self.saude -= 1
        print("Saúde atual:", self.saude)

    def alterar_fome(self):
        if self.saude < 60:
            self.fome = True
            print("Estou com fome.")

    def alimentar(self):
        self.fome = False
        self.saude = 100
        print("Alimentado", "Saúde: 100")

    def aniversario(self):
        self.idade += 1
        print(f"Feliz aniversário! Agora seu bichinho tem {self.idade} anos!")




