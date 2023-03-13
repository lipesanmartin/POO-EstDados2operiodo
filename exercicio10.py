class BombaCombustivel:
    def __init__(self, quantidade):
        self.tipo = ""
        self.preco = 0.0
        self.quantidade = quantidade
        self.abastecer = 0

    def abastecer_valor(self):
        valor = float(input(f"Insira o quanto quer abastecer de {self.tipo}: "))
        self.abastecer = valor / self.preco
        print(f"Você abasteceu {self.abastecer}L por R$ {valor}")
        self.quantidade -= self.abastecer

    def abastecer_litro(self):
        litros = float(input(f"Insira a quantidade de litros de {self.tipo} que gostaria de abastecer: "))
        self.abastecer = litros * self.preco
        print(f"Você abasteceu {litros}L por R$ {self.abastecer}")

    def alterar_valor(self):
        self.preco = float(input(f'Insira o novo preço do combustível "{self.tipo}".'))
        print(f"{self.tipo} agora custa R$ {self.preco} por L.")

    def alterar_combustivel(self):
        while True:
            escolha = int(input("Escolha qual combustível gostaria de usar para abastecer:\n1 - Álcool\n2 - "
                                "Gasolina\n3 -"
                                "GNV"))
            if escolha not in range(1, 4):
                print("Escolha inválida. Tente novamente.")
            else:
                if escolha == 1:
                    self.tipo = "álcool"
                    break
                elif escolha == 2:
                    self.tipo = "gasolina"
                    break
                elif escolha == 3:
                    self.tipo = "GNV"
                    break
            print(f"Você escolheu f{self.tipo}")

    def alterar_quantidade_bomba(self):
        self.quantidade -= self.abastecer

    def encher_bomba(self):
        self.quantidade += float(input("Insira a quantidade em L para encher a bomba: "))
        print(f"Bomba agora possui {self.quantidade} L de {self.tipo}")


volume_inicial = int(input("Insira o conteùdo inicial da bomba em L: "))

bomba = BombaCombustivel(volume_inicial)
bomba.alterar_combustivel()
bomba.alterar_valor()
bomba.abastecer_valor()
bomba.alterar_quantidade_bomba()
bomba.abastecer_litro()
bomba.alterar_quantidade_bomba()
bomba.encher_bomba()



