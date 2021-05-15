"""
Uso: Obtención de los datos Exif de una fotografía
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Mayo 2020
"""

from exif import Image
import os
from datetime import datetime

clear = lambda: os.system("cls" if os.name=="nt" else "clear")

clear()

with open("tosticentro.jpg", "rb") as imagen:
    img = Image(imagen)
    if img.has_exif:
        print(datetime.now(), "\033[0;32m [INFO] Metadata \033[0;0m")        
        if img.model:
            print(datetime.now(), "\033[0;32m [INFO] Model > %s \033[0;0m" % img.model)                     
        if img.make:
            print(datetime.now(), "\033[0;32m [INFO] Make > %s \033[0;0m" % img.make)
        if img.datetime:
            print(datetime.now(), "\033[0;32m [INFO] Datetime > %s \033[0;0m" % img.datetime)
        if img.gps_latitude:
            print(datetime.now(), "\033[0;32m [INFO] GPS latitude > %s %s \033[0;0m" % (str(img.gps_latitude), img.gps_latitude_ref))
        if img.gps_longitude:
            print(datetime.now(), "\033[0;32m [INFO] GPS longitude > %s %s \033[0;0m" % (str(img.gps_longitude), img.gps_longitude_ref))    
    img.model = "GoPro"
    img.mensaje = "Yo estuve ahi"
    
with open("tosticentro.jpg", "wb") as new_imagen:    
    new_imagen.write(img.get_file())

print("--------------------------------------------------------------------------------------")
print(datetime.now(), "\033[0;31m [INFO] Modificar atributo \033[0;0m")
print(datetime.now(), "\033[0;32m [INFO] Model > %s \033[0;0m" % img.model)    
if img.mensaje:
    print(datetime.now(), "\033[0;31m [INFO] Nuevo atributo \033[0;0m")
    print(datetime.now(), "\033[0;32m [INFO] Mensaje > %s \033[0;0m" % img.mensaje)

print("--------------------------------------------------------------------------------------")
print(datetime.now(), "\033[0;31m [INFO] Borrando atributo \033[0;0m")
del img.mensaje
print(datetime.now(), "\033[0;32m [INFO] Atributo mensaje > %s \033[0;0m" % img.get('mensaje', 'Not found'))

print(datetime.now(), "\033[0;33m [INFO] Guardando imagen... \033[0;0m")
new_imagen.close()

    
