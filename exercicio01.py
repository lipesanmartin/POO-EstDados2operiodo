class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        print(f"A bola de {self.material} é {self.cor}.")

    def troca_cor(self):
        novacor = input("Insira uma nova cor da bola: ")
        self.cor = novacor

    def mostra_cor(self):
        print(f"A bola de {self.material} é {self.cor}.")


bola = Bola("branca", 10, "borracha")
bola.troca_cor()
bola.mostra_cor()
