#!/usr/bin/python3.6

https://draeger-it.blog/python-27-rechnen-mit-zeitdifferenzen-am-datetime-modul/

# zeit von jetzt, gestern und heute ausgeben

from datetime import datetime, timedelta

# zeit von jetzt, gestern und heute ausgeben
# benötigte Module: datetime, timedelta

jetzt = datetime.now()
print("jetzt -> ",jetzt)
morgen = jetzt + timedelta(days = 1)
print("morgen -> ",morgen)
gestern = jetzt - timedelta(days = 1)
print("gestern -> ", gestern)

print("----------------------------")

# timedalte ohne einen festen bezug
# benötigte Module: datetime, timedelta

diff = timedelta(weeks=12, hours=5)
now = datetime.now()
print(now-diff)