class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_lados(self):
        self.base = int(input("Insira o novo valor da base: "))
        self.altura = int(input("Insira o novo valor da altura: "))

    def retornar_lados(self):
        print("A base do retângulo é:", self.base)
        print("A altura do retângulo é:", self.altura)

    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro


base = int(input("Insira o valor da base do retângulo em m: "))
altura = int(input("Insura o valor da altura do retângulo em m: "))

comodo = Retangulo(base, altura)
comodo.retornar_lados()
print(f"A área de pisos necessários para esse cômodo é {comodo.area()} m².")
print(f"O perímetro do rodapé é {comodo.perimetro()} m.")
