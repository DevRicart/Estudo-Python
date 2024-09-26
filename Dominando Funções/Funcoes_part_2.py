# Positional only - Tudo o que está até a barra é somente por posição.

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# ===========================================================================================

# Keyword only - Tudo depois do asterístico só consegue ser passado por nome, por chave.

def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# ===========================================================================================

# Híbrido, Keyword and positional only.

def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro3(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# ===========================================================================================

# Objetos de primeiras classe.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b
    

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")

exibir_resultado(10, 10, somar)

op = somar

print(op(1,23))

# ===========================================================================================

# Escopo local e escopo global

salario = 2000 # Escopo global

def salario_bonus(bonus):
    global salario
    salario += bonus

    return salario

print(salario_bonus(500))


# ===========================================================================================

def listagem():
    lista.append(2) # A lista é um objeto imutável, portanto, toda operação realizada mesmo dentro de uma função, irá refletir no objeto que está fora dela por referência.


lista = [1]
listagem()
print(lista)

# Deste modo se cria uma cópia e se modifica esta cópia, assim não alterando o objeto lista original.
def listagem2():
    lista_aux = lista2.copy()
    lista_aux.append(4)
    print(lista_aux)
    print(lista2)

lista2 = [3]

listagem2()