import random


class NovoBichinhoVirtual:
    def __init__(self):
        self.nome = "Sem nome"
        self.fome = random.randint(1, 101)
        self.saude = random.randint(1, 101)
        self.idade = 0
        self.humor = (self.saude + self.fome) / 2

    def set_nome(self):
        self.nome = str(input("Insira o nome do bichinho virtual: "))
        print(self.get_nome())

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
        return f"O nome do bichinho é {self.nome}"

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

    def get_atributos(self):
        print(
            f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\n"
            f"Humor: {self.get_humor()}\nIdade: {self.idade}")

    def menu(self):
        while True:
            try:
                action = int(
                    input("Insira a ação que gostaria de realizar:\n1) Renomear\n2) Checar fome\n3) Checar humor\n"
                          "4) Checar saude\n5) Checar idade\n6) Alimentar\n7) Brincar\n"
                          "8) Checar nome\n9) Fazer aniversário\n\nAção: "))
                break
            except (TypeError, ValueError):
                print("Por favor, insira um número inteiro.")
        if action == 1:
            print(self.set_nome())
        elif action == 2:
            print(self.get_fome())
        elif action == 3:
            print(self.get_humor())
        elif action == 4:
            print(self.get_saude())
        elif action == 5:
            print(self.get_idade())
        elif action == 6:
            while True:
                comida = int(input("Quanta comida você gostaria de dar? (0 a 100): "))
                if comida in range(0, 101):
                    self.alimentar(comida)
                    break
                else:
                    print("Valor inválido")

        elif action == 7:
            while True:
                tempo = int(input("Quanto tempo você gostaria de brincar? (0 a 100): "))
                if tempo in range(0, 101):
                    self.brincar(tempo)
                    break
                else:
                    print("Valor inválido")
        elif action == 8:
            self.aniversario()
        elif action == 9:
            print(self.get_nome())
        else:
            self.get_atributos()


if __name__ == '__main__':
    bicho = NovoBichinhoVirtual()
    while True:
        bicho.menu()
        if bicho.idade == 30 or bicho.saude == 0 or bicho.fome == 0:
            print(f"{bicho.nome} faleceu RIP")
            break
