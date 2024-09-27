"""
Tuplas são muito parecidas com as listas, a principal
diferença é que tuplas são imutáveis, euqnato listas são mutáveis.  
"""
# Defina utilizando tuple ou colocando uma vírgula ao final

frutas = ("laranja", "pera", "uva",) 
letras = tuple("python") 
numeros = tuple ([1, 2, 3, 4]) 
pais = ("Brasil",)

# =================================

frutas = ("maçã", "laranja", "uva", "pera",) 
frutas [0] # maçã 
frutas [2] # uva


# =================================

matriz = ( 
  (1, "a", 2), 
  ("b", 3, 4), 
  (6, 5, "c"), 
) 
matriz [0] # (1, "a", 2) 
matriz[0][0] #1 
matriz[0][-1] #2 
matriz[-1][-1] # "c"

# =================================

tupla = ("p", "y", "t", "h", "o", "n",) 
tupla [2:] # ("t", "h", "o", "n") 
tupla[:2] # ("p", "y") 
tupla [1:3] # ("y", "t") 
tupla [0:3:2] # ("p", "t") 
tupla[::] # ("p", "y", "t", "h", "o", "n") 
tupla[::-1] # ("n", "o", "h", "t", "y", "p")

# =================================

