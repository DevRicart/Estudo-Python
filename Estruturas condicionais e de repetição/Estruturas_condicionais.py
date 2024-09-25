# # Utilizando apenas if

# saldo = 2000.00
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Saque realizado!")

# if saldo < saque:
#     print("Saldo insuficiente!")

# # Utilizando if e else

# saldo = 2000.00
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Saque realizado!")

# else:
#     print("Saldo insuficiente!")

# # Utilizando elif

# opcao = int(input("Informe uma oção: [1] Sacar \n[2] Extrato: \n"))

# if opcao == 1:
#     valor = float(input("Informe a quantia para o saque: "))

# elif opcao == 2:
#     print(f"Exibindo extrato: {saldo}")

# else:
#     print("Opção inválida")

# ========================================

#Adicionar mais exemplos da aula (importante!)

# Ternário

saldo = 2000
saque = 5000

status = "Sucesso" if saldo  >= saque else "Falha"

print(f"{status} ao realizar o saque!")