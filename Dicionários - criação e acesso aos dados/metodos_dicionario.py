# clear()
# copy()
# fromkeys()

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

# get()

contatos = { "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} } 

contatos["chave"] # KeyError

contatos.get("chave") # None 
contatos.get("chave", {}) #{} 
contatos.get("guilherme@gmail.com", {}) # "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

# items()
# keys()