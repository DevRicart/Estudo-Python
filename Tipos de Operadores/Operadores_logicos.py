# print(not 1000 > 1500)
# # True

# contatos_emergencia = []
# print(not contatos_emergencia)
# # True

# print(not "saque 1500")
# # False

# print(not "")
# # True

# ====================

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))