class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def esta_carregado(self):
        print("Não estou carregado")

moto = Motocicleta("Amarela", "ABC-1234", 2)

print(moto)
moto.ligar_motor()

carro = Carro("Vermelho", "DEF-5678", 4)
print(carro.cor)

caminhao = Caminhao("Cinza", "GHI-9101", 6)
caminhao.esta_carregado()

carro.esta_carregado() # Erro