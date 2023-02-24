'''Codigo para descomprimir archivos, usar las librerias datetime, math y re. Para buscar
un formato de texto en un grupo de carpetas, subcarpetas y archivos. Parte de formaciones
realizadas en mi proceso de aprendizaje de programación usando el lenguaje Python'''


import shutil
import re
import os
import time
import datetime
from pathlib import Path
import math

#esto fue para descomprimir el archivo donde estaban las indicaciones del proyecto
#ruta="C:\\Users\\CONSORCIO HPH\\Desktop\\PY\D9\\PROYECTO"

#Destino="Proyecto_descomprimido"

#shutil.unpack_archive("Proyecto+Dia+9.zip","Proyecto_9","zip")

inicio=time.time()

ruta="C:\\Users\\CONSORCIO HPH\\Desktop\\PY\\D9\\PROYECTO\\Proyecto_9\\Mi_Gran_Directorio"

mi_patron= r'N\D{3}-\d{5}'
hoy=datetime.date.today()
numeros_encontrados=[]
archivos_encontrados=[]

def buscar_numero(archivo, patron):
    este_archivo=open(archivo, "r")
    texto=este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ""

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado= buscar_numero(Path(carpeta,a), mi_patron)
            if resultado!="":
                numeros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice=0
    print("-"*50)
    print(f'fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('ARCHIVO\t\t\t numero Serie')
    print("-----------\t\t-----------")
    for a in archivos_encontrados:
        print(f'{a}\t {numeros_encontrados[indice]}')
        indice+=1
    print('\n ')
    print(f'Numeros encontrados: {len(numeros_encontrados)}')
    fin=time.time()
    duracion=fin-inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)}')
    print("-" * 50)

crear_listas()
mostrar_todo()

