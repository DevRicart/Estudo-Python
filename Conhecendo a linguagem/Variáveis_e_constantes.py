# Jeito 1 de declarar variável
age = 26
name = "Ricardo"
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

print(" ")
'''
Jeito 2 de declarar variável
'''
age, name = (25, "Thaina")
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

"""
Python não possui uma palavra reservada para constantes.
Ao invés disso, se usa uma convenção para definir uma constante: Criar a variável apenas com letras maiúsculas
"""

ABS_PATH = '/Users/Ricardo/Documents/Dev/Python'
DEBUG = True
BRAZILIAN_STATES = [
  'SP',
  'RJ',
  'MG',
]
AMOUNT = 30.2

'''
Boas práticas:
O padrão de nomes é snake case.
Escolher nomes sugestivos.
Nome de constantes todo em maiúsculo
'''