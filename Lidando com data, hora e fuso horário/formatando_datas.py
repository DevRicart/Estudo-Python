from datetime import datetime

d = datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %a %H:%M")) # 19/07/2023 14:20

# Convertendo String para datetime

date_string = "20/07/2023 15:30"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d) # 2023-07-20 15:30:00

# ===========================================================
# Copiar exemplos da aula