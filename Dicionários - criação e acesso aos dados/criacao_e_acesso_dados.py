"""
Um dicionário é um conjunto não-ordenado de pares chave:valor  
"""

pessoa = {
  "nome": "Ricardo",
  "idade": 26,  
}

# Ou

pessoa = dict(nome="Ricardo", idade=26)

# Adiciona uma nova chave
pessoa["telefone"] = "4002-8922" # {"nome": "Ricardo", "idade": 26, "telefone": "4002-8922"}

# Acessando valores do dicionário

pessoa["nome"] # Ricardo
pessoa["idade"] # 26
pessoa["telefone"] # "4002-8922"

pessoa # {"nome": "Ricardo", "idade": 26, "telefone": "4002-8922"}

# Alterando valores

pessoa["nome"] = "Thaina" 
pessoa["idade"] = 25
pessoa["telefone"] = "2569-6969"

pessoa # {"nome": "Thaina", "idade": 25, "telefone": "2569-6969"}

# ==================================================================

contatos = { 
  "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, 
  "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"}, 
  "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 
  "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"] # "3443-2121"
print(telefone)

# ==================================================================

# for chave in contatos:
#   print(chave, contatos[chave])

# for chave, valor in contatos.items(): # O método .items() retorna uma lista de tuplas
#   print(chave, valor)