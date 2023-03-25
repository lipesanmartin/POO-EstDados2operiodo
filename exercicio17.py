from exercicio16 import NovoBichinhoVirtual

bicho1 = NovoBichinhoVirtual()
bicho2 = NovoBichinhoVirtual()
bicho3 = NovoBichinhoVirtual()
bicho4 = NovoBichinhoVirtual()
bicho5 = NovoBichinhoVirtual()

fazenda = [bicho1, bicho2, bicho3, bicho4, bicho5]

while True:
    for bichos in fazenda:
        print(f"Menu para o bichinho. {bichos.get_nome()}")
        bichos.menu()
