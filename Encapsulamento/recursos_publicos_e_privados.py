# Público: Pode ser acessado de fora da classe.
# Privado: Só pode ser acessado pela classe.
# Para definir uma variável como privadas, você deve começar ela com um underline(underscore). Isso não garante que ela não sera acessada, mas é uma convenção universal em python.

class Conta:
  def __init__(self, numero_agencia, saldo=0):
    self._saldo = saldo
    self.numero_agencia = numero_agencia

  def depositar(self, valor):
    # ...
    self._saldo += valor

  def sacar(self, valor):
    # ...
    self._saldo -= valor