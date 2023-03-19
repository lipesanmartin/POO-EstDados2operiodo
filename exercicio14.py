class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def set_nome(self):
        self.nome = str(input("Insira o nome do funcionário: "))
        return self.nome

    def set_salario(self):
        self.salario = float(input(f"Insira o salário do funcionário {self.nome}: "))
        return self.salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return f"Salário é R$ {self.salario:.2f}"

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)
        return self.salario


jose = Funcionario("José", 1500.00)
print(jose.get_nome())
print(jose.get_salario())
jose.aumentar_salario(10)
print(jose.get_salario())
