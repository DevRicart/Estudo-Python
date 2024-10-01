# $ pip install pytz
"""
Caso dê problema:
$ python -m venv .env 
$ source .env/bin/activate
"""
import pytz
from datetime import datetime, timezone, timedelta

data = datetime.now(pytz.timezone('Europe/Oslo'))

print(data)

# Sem o pytz

data_oslo = datetime.now(timezone(timedelta(hours=2), "OSL"))
data_sp = datetime.now(timezone(timedelta(hours=-3)))

print("")
print(data_sp)
print(data_oslo)
