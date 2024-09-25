# For /For else

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end='\n')
  
else:
  print("Fim") #Executa o final do laço

# ====================

# range(stop) -> range object
# range(start, stop[, step]) -> range object

# For range

for numero in range(0, 11):
  print(numero, end=" ")

# Exibindo a tabuada do 5
for numero in range(0, 51, 5):
  print(numero, end=" ")

# ====================

# While

opcao = -1

while opcao != 0:
  opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n "))

  if opcao == 1:
    print("Sacando...")
  elif opcao ==2:
    print("Exibindo o extrato...")

# Break

while True:
  nnumero = int(input("Informe um número: "))

  if numero == 10:
    break

  print(numero)

# Continue

for numero in range(100):

  if numero % 2 == 0:
    continue

  print(numero)