import datetime

d = datetime.date(1999, 5, 18)
print(d)


from datetime import date # Forma mais comum

data = date(1997, 12, 10)
print(data)

# ============================================

from datetime import date, datetime, time # Importando mais de um ao mesmo tempo

data_hora = datetime(1666, 6, 6, 6, 6, 6)
print(data_hora)

print(datetime.today())

# ============================================

hora = time(10, 20, 0)
print(hora)

