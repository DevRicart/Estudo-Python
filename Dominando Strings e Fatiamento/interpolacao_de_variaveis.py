# Old style % python2

nome = "Ricardo" 
idade = 26 
profissao = "Progamador" 
linguagem = "Python"  
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

# Método format python2

nome = "Guilherme" 
idade = 28 
profissao = "Programador" 
linguagem = "Python"
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome = nome, idade = idade, profissao = profissao, linguagem=linguagem))

pessoa = {"nome": "Ricardo", "idade": 26}

print("Olá, me chamo {nome}. Eu tenho {idade} anos.".format(**pessoa))

#f-string (O MELHOR)

nome = "Guilherme" 
idade = 28 
profissao = "Programador" 
linguagem = "Python" 
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Casas decimais

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f}") # 10 espaços antes da variável