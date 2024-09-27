frutas = ["laranja", "maçã", "uva"]
vegetais = [] # Lista vazia

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 420000000, 2020, 2900, "São Paulo", True]

# ==================================

print(frutas[2]) 
print(frutas[-3])

# ==================================

# Matriz

matriz = [
    [1, "a", 2], 
    ["b", 3, 4],
    [6, 5, "c"]  
] 

matriz[0]      # [1, "a", 2]
matriz[0][0]   # 1
matriz[0][-1]  # 2
matriz[-1][-1] # "c"

# ==================================

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"] 
lista[:2] # ["p", "y"] 
lista[1:3] # ["y", "t"] 
lista[0:3:2] # ["p", "t"] 
lista[::] # ["p", "y", "t", "h", "o", "n"] 
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

# ==================================

# Percorrer uma lista

carros = ["gol", "celta", "palio"] 

for carro in carros:
  print(carro)

carros = ["Ferrari", "Opala", "Dodge viper"] 
for indice, carro in enumerate (carros): 
  print(f"{indice}: {carro}")

# ==================================

# Compreensão de listas

numeros = [1, 30, 21, 2, 9, 65, 34] 
pares = [] 

for numero in numeros: 
  if numero % 2 == 0: 
    pares.append(numero)
print(pares)

# comprehension

numeros = [1, 30, 21, 2, 9, 65, 34] 
pares = [numero for numero in numeros if numero % 2 == 0]

[n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 