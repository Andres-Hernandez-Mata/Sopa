"""
Uso: Obtención de las imágenes que contiene una página Web
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
    src = parsed_body.xpath('//img/@src')
    print(datetime.now(), "\033[0;32m [INFO] %s imagenes encontradas \033[0;0m" % len(src))
    imagenes = bs.find_all("img",src=True)
    imagen_src = [img['src'] for img in imagenes]
    imagen = [img for img in imagen_src if img.endswith('.jpg')]          
    for enlace in imagen:
        print(datetime.now(), "\033[0;32m [INFO] %s \033[0;0m" % enlace)
        descargar = requests.get(enlace)
        name = enlace.split('/')[-1]
        file = open(name, 'wb')
        file.write(descargar.content)
        file.close()
        print(datetime.now(), "\033[0;32m [INFO] Imagen %s descargada... \033[0;0m" % name)

if __name__ == '__main__':
    main()
