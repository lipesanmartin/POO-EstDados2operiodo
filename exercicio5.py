class ContaCorrente:
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alternar_nome(self):
        self.nome = str(input("Insira o novo nome: "))
        print(self.nome)

    def deposito(self):
        while True:
            deposito = float(input("Quanto quer depositar? "))
            if deposito > 0:
                self.saldo += deposito
                break
            else:
                print("Valor inválido")
        print(f"Seu saldo é {conta.saldo:.2f}")

    def saque(self):
        while True:
            saque = float(input("Quanto quer sacar? "))
            if saque > 0:
                self.saldo -= saque
                break
            else:
                print("Valor inválido")
        print(f"Seu saldo é {conta.saldo:.2f}")


conta = ContaCorrente(123456, "João", 500)
conta.alternar_nome()
conta.deposito()
conta.saque()
