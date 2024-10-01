import datetime

d = datetime.datetime(2023, 7, 19, 13, 45)
#print(d)

d = d + datetime.timedelta(weeks=1)
#print(d)

# =========================================

from datetime import timedelta, datetime


def lava_jato():
  tempo_pequeno = 30
  tempo_medio = 45
  tempo_grande = 60
  data_atual = datetime.now()

  opcao = input("Qual o tamanho do seu carro? ")
  if opcao == "P" or opcao == "p":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou {data_atual} e a data estimada para o término é: {data_estimada}")

  elif opcao == "M" or opcao == "m":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou {data_atual} e a data estimada para o término é: {data_estimada}")

  elif opcao == "G" or opcao == "g":
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou {data_atual} e a data estimada para o término é: {data_estimada}")
  else:
    print("Opção inválida!")
lava_jato()