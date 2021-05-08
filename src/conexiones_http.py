"""
Uso: Conexiones HTTP | urlopen | beautifulSoup
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Mayo 2020
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from datetime import datetime

os.system("cls")

print(datetime.now(), "\033[0;32m [HTML] Urlopen \033[0;0m \n")
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read().decode())

print(datetime.now(), "\033[0;32m [HTML] BeautifulSoup \033[0;0m \n")
html = urlopen("http://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), features="lxml")
print(bs.html)

print()
print(datetime.now(), "\033[0;32m [INFO] BeautifulSoup <h1></h1> \033[0;0m \n")
print(bs.html.body.h1)

