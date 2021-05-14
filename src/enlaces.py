"""
Uso: Obtención de la lista de enlaces que contiene una página Web
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Mayo 2020
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from lxml import html
import os

def main():
    os.system('cls')
    url = 'https://www.uanl.mx/enlinea'
    print(datetime.now(), "\033[0;32m [INFO] Buscando... %s \033[0;0m" % url)
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'lxml')
    parsed_body = html.fromstring(response.text)
    href = parsed_body.xpath('//a/@href')
    print(datetime.now(), "\033[0;32m [INFO] %s enlaces encontrados \033[0;0m" % len(href))
    enlaces = bs.find_all("a",href=True)    
    direcciones = [enlace['href'] for enlace in enlaces]
    for link in direcciones:
        if not link == '#':
            print(datetime.now(), "\033[0;32m [INFO] %s \033[0;0m" % link)

if __name__ == '__main__':
    main()