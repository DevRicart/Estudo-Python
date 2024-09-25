'''
A identação em python é muito importante, 
não só para ajudar visualmente como em outras 
linguagens, como também é o que define o inicio 
e fim dos blocos.
'''
def sacar(self, valor: float) -> None: # Inicio do bloco do método

    if self.saldo >= valor: # Inicio do bloco do if
        
        self.saldo -= valor

    # fim do bloco do if

# fim do bloco do método

# =======================

def saque(valor):
    saldo = 500

    if saldo >= valor:
        print(f"Valor sacado: {valor}")
    else:
        print("Erro: Valor de saque maior que o saldo.")

saque(100)