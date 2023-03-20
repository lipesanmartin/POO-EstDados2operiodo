class ContaInvestimento:
    def __init__(self, numero, nome, saldo, juros):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.juros = juros

    def adicione_juros(self):
        self.saldo += self.saldo * (self.juros / 100)


conta = ContaInvestimento(123123, "Pedrinho", 1000, 10)
for x in range(5):
    conta.adicione_juros()
print(conta.saldo)
