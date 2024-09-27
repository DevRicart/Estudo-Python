numeros = set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

fruta = set("abacaxi") # ("b", "a", "c", "x", "i")

carros = set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

print(fruta)

# Convertendo set em lista

numeros2 = {0, 1, 4, 2, 3, 1, 3, 4}

numeros2 = list(numeros2)

print(numeros2)

# ========================================

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}

# ========================================

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_a.intersection(conjunto_b) # {2, 3}

# ========================================

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# ========================================

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# ========================================

conjunto_a.issuperset(conjunto_b) # False
conjunto_a.issuperset(conjunto_b) # True

# ========================================

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

# ========================================

sorteio = {1, 2}

sorteio.add(25) # {1, 2, 25}
sorteio.add(42) # {1, 2, 25, 42}
sorteio.add(2)  # {1, 2, 25, 42} Pois o número 2 já está inserido

# ========================================

sorteio.clear() # {}

# ========================================

sorteio.copy() #{}

# ========================================

numeros = {1, 2, 3, 4, 5, 6, 6, 7, 8, 9}

numeros.discard(1)
numeros.discard(3)
#numeros = {2, 4, 5, 6, 7, 8, 9} Funciona mesmo se tentar remover um que não existe

# ========================================

numeros.pop() # {4, 5, 6, 7, 8, 9}

# ========================================

numeros.remove(5) # {4, 6, 7, 8, 9} Dá erro removendo numeros que nao existem

# ========================================

#len

#in
