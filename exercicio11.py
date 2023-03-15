class Carro:
    def __init__(self, autonomia):
        self.autonomia = autonomia
        self.combustivel = 0

    def adicionar_gasolina(self, litros):
        self.combustivel = litros
        if self.combustivel > 100:
            self.combustivel = 100  # volume maximo do tanque apenas como exemplo
        return self.combustivel

    def andar(self, distancia):   # autonomia = distancia / litros
        gasto = distancia / self.autonomia
        self.combustivel -= gasto
        if self.combustivel < 0:
            self.combustivel = 0
        return self.combustivel

    def obter_gasolina(self):
        return self.combustivel


meuFusca = Carro(15)
meuFusca.adicionar_gasolina(20)
meuFusca.andar(100)
meuFusca.obter_gasolina()
print(meuFusca.obter_gasolina())
