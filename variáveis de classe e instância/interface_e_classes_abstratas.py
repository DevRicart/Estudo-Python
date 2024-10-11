'''
Interfaces definem o que uma classe deve fazer e não como.
O conceito de interface é definir um contrato, onde são declarados
os métodos (o que deve ser feito) e suas espectivas assinaturas. Em python
utilizamos classes abstratas para criar contratos. Classes abstratas não podem
ser instanciadas. 
Python nao possui o tipo específico Interface
'''
# =============================================================================
'''
Por padrão, o Python não fornece classes abstratas. O python vem com um módulo 
que fornece a vase para definir as classes abstratas, e o nome do módulo é ABC.
O ABC funciona decorando métodos da classe base como abstratos e, em seguida,
registrando classes concretas como implementações da base abstrata. Um método
se torna abstrado quando decorado com @abstractmethod
'''
# Criando classes abstratas com o módulo ABC

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")


class ControleAr(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado")

    def desligar(self):
        print("Desligando o ar condicionado")


controle = ControleAr()
controle.ligar()
controle.desligar()

# https://docs.python.org/pt-br/3/library/abc.html