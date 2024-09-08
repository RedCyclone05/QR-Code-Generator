"""
Este script Python organiza imágenes en carpetas basadas en un patrón de nombres específico. 
Analiza el nombre de cada imagen en la misma carpeta que el script y crea una carpeta para cada grupo único encontrado.

Pasos del proceso:
1. Obtiene la ruta del directorio donde se encuentra el script en ejecución.
2. Lee todos los archivos en ese directorio.
3. Utiliza expresiones regulares para extraer el grupo del nombre de cada archivo de imagen.
4. Crea una carpeta para cada grupo único encontrado (por ejemplo, "QR Grupo's").
5. Mueve cada imagen a la carpeta correspondiente según su grupo.
6. Imprime las imágenes organizadas por grupo al final del proceso.

"""

import os
import shutil
import re

# Obtener la ruta del directorio donde está este script
directorio_script = os.path.dirname(__file__)

# Ruta de la carpeta donde están las imágenes (misma carpeta del script)
carpeta_imagenes = directorio_script

# Obtener la lista de archivos en la carpeta
archivos = os.listdir(carpeta_imagenes)

# Expresión regular para extraer el grupo del nombre del archivo
patron = r'QR ([^.]+)\.'

# Diccionario para almacenar las listas de imágenes por grupo
imagenes_por_grupo = {}

# Iterar sobre cada archivo en la carpeta
for archivo in archivos:
    ruta_completa = os.path.join(carpeta_imagenes, archivo)
    if os.path.isfile(ruta_completa):
        # Extraer el grupo del nombre del archivo usando expresión regular
        match = re.search(patron, archivo)
        if match:
            grupo = match.group(1)

            # Crear la carpeta del grupo si no existe
            carpeta_grupo = os.path.join(directorio_script, f"QR {grupo}'s")
            if not os.path.exists(carpeta_grupo):
                os.makedirs(carpeta_grupo)

            # Mover el archivo a la carpeta del grupo correspondiente
            shutil.move(ruta_completa, os.path.join(carpeta_grupo, archivo))

            # Agregar el archivo a la lista de imágenes por grupo
            if grupo in imagenes_por_grupo:
                imagenes_por_grupo[grupo].append(archivo)
            else:
                imagenes_por_grupo[grupo] = [archivo]

# Imprimir las imágenes por grupo
print("Imágenes organizadas por grupo:")
for grupo, imagenes in imagenes_por_grupo.items():
    print(f"Grupo '{grupo}': {imagenes}")
