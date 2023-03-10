class Televisao:
    def __init__(self):
        while True:
            self.canal = int(input("Insira o canal inicial (0 a 99): "))
            if 99 > self.canal >= 0:
                print("Canal:", self.canal)
                break
            else:
                print("Canal inexistente.")
        self.volume = 50
        print("Volume:", self.volume)

    def aumentar_volume(self):
        if self.volume >= 100:
            print("Volume máximo.")
        else:
            self.volume += 1
            print("Volume:", self.volume)

    def diminuir_volume(self):
        if self.volume == 0:
            print("Mudo.")
        else:
            self.volume -= 1
            print("Volume:", self.volume)


tv = Televisao()
for x in range(0, 52):  # exemplo
    tv.aumentar_volume()
for x in range(0, 102):  # exemplo
    tv.diminuir_volume()
