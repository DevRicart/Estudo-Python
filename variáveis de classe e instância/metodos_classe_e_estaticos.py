'''
Geralmente usamos métodos de classe para criar métodos de fábrica
Geralmente usamos métodos estáticos para criar funções utilitárias
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #Eu preciso ter acesso ao contexto da classe
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod #Eu não preciso de contexto nem da classe e nem da instancia do obj
    def e_maior_idade(idade):
        return idade >= 18
    
p = Pessoa("Guilherme", 28)
print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1994, 3, 21, "Guilherme")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
