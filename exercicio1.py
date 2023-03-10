class Bola:
    def __init__(self):
        self.cor = "branca"
        self.circunferencia = 10
        self.material = "borracha"
        print(f"A bola de {self.material} é {self.cor}.")

    def troca_cor(self):
        novacor = input("Insira uma nova cor da bola: ")
        self.cor = novacor

    def mostra_cor(self):
        print(f"A bola de {self.material} é {self.cor}.")


bola = Bola()
bola.troca_cor()
bola.mostra_cor()
