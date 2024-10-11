class Estudante:
    escola = "FGV" #Atributo de Classe

    def __init__(self, nome, matricula):
        self.nome = nome #Atributo de instância
        self.matricula = matricula #Atributo de instância
    
    def __str__(self) -> None:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovana", 2)

mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "EPGE" #Altera em todos os objetos da classe
aluno_1.matricula = 3 #Altera apenas aquele objeto
mostrar_valores(aluno_1, aluno_2)