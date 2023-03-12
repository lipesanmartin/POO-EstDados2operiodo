class Ponto:
    def __init__(self, x, y):
        self.coordx = x
        self.coordy = y

    def valores_ponto(self):
        print(f"Coordenadas do ponto:\nX:{self.coordx}\nY: {self.coordy} ")


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro(self):
        x = self.largura / 2
        y = self.altura / 2
        print(f"O centro do retângulo é nas coordenadas:\nX: {x}\nY: {y}")



