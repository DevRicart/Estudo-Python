"""
Objetivo Geral: 
Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.


Desafio:
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

Saque: ✔
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

Depósito: ✔
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

Extrato: ✔
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

Novas funções:
Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

Criar usuário (cliente):
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro bairro cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

Criar conta corrente:
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

Dica:
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
"""
def menu():
    menu = """
           ================ MENU ================

            [d] Depositar
            [s] Sacar
            [e] Extrato
           [cc] Criar conta
           [lc] Listar contas
           [nu] Novo usuário
            [q] Sair

           ======================================
        => """
    return input(menu)


def sacar_dinheiro(*, saldo, extrato, numero_atual_saques, limite_saques):
    
    saque = float(input("Digite a quantidade a ser sacada: "))

    if numero_atual_saques >= limite_saques:
        print("Você ultrapassou seu limite diário de saques!")

    elif saque > 0 and saque <= 500:
        print("Sacando...")
        saldo = saldo - saque
        numero_atual_saques += 1
        saques_restantes = limite_saques - numero_atual_saques
        extrato = extrato + f"Saque:    R$ {saque:.2f}\n".replace('.', ',')
        saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
        print(f"Saque realizado com sucesso! \nSaldo restante: R$ {saldo_formatado}")
        print(f"Saques restantes: {saques_restantes}")
        

    elif saque > saldo:
        print("Não foi possível sacar este valor pois não há saldo suficiente")
        saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
        print(f"Saldo atual: R$ {saldo_formatado}")

    elif saque > 500:
        print("Não é permitido sacar mais do que R$ 500,00 de uma única vez")
  
    return saldo, extrato, numero_atual_saques


def depositar_dinheiro(saldo, extrato, /):
    deposito = float(input("Digite a quantidade a ser depositada: "))

    if deposito > 0:
        print("Depositando...")
        saldo = saldo + deposito
        extrato = extrato + f"Depósito: R$ {deposito:.2f}\n".replace('.', ',')
        saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
        print(f"Depósito realidado com sucesso! \nSaldo atual: R$ {saldo_formatado}")
            
    else:
        print("Valor digitado é inválido!")
    return saldo, extrato


def extrato_bancario(saldo, /, *, extrato):
    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    saldo_formatado = f'{saldo:.2f}'.replace('.', ',')
    print(f"\nSaldo: R$ {saldo_formatado}")
    print("\n=========================================")


def main():
    LIMITE_SAQUES = 3
    numero_atual_saques = 0
    saldo = 2000
    extrato = ""

    while True:
        opcao = menu()
        

        if opcao == "s":
            saldo, extrato, numero_atual_saques = sacar_dinheiro(saldo=saldo, extrato=extrato, limite_saques=LIMITE_SAQUES, numero_atual_saques=numero_atual_saques)
                 
        elif opcao == "e":
            extrato_bancario(saldo, extrato=extrato)

        elif opcao == "d":
            saldo, extrato = depositar_dinheiro(saldo, extrato)

        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Opção inválida")

main()