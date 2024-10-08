"""
João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde João iforme: Cor, modelo, ano e valor da bicicleta vendida. 
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!    
"""

class Bicicletaria:
    # Atributos da classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor 
    
    # Métodos da classe
    def buzinar(self):
        print("Fon fon")

    def parar(self):
        print("*A bicicleta está parando*")

    def correr(self):
        print("*A bicicleta está correndo*")

b1 = Bicicletaria("Vermelha", "Caloi", 2020, 500)
b1.buzinar()

print(b1.cor)