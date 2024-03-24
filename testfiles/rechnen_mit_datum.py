#!/usr/bin/python3.6

# https://www.python-lernen.de/python-modul-datetime.htm


# Rechnen mit datum

from datetime import date
heute = date.today()
print(heute)

heute_umf = heute.strftime("%m-%d-%Y. %d.%b.%Y ist ein %A am %d. Tag des %B.")
print(heute_umf)

# mit dem Datum lässt sich rechnen
geburtstag = date(1973,10,29)
heute = date.today()
alter = heute - geburtstag
print(alter.days, "Tage seit Geburt vergangen")