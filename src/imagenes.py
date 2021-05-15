"""
Uso: Obtención de la lista de imágenes que contiene una página Web
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Mayo 2020
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def main():
    os.system('cls')
    url = 'https://www.uanl.mx/enlinea'
    print(datetime.now(), "\033[0;32m [INFO] Buscando... %s \033[0;0m" % url)
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'lxml')            
    imagenes = bs.find_all("img",src=True)
    imagen_src = [img['src'] for img in imagenes]
    imagen = [img for img in imagen_src if img.endswith('.jpg')]
    print(datetime.now(), "\033[0;32m [INFO] %s imagenes encontradas \033[0;0m" % len(imagen))
    for enlace in imagen:
        print(datetime.now(), "\033[0;32m [INFO] %s \033[0;0m" % enlace)

if __name__ == '__main__':
    main()

