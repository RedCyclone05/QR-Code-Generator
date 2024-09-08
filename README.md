# QR Maker

## Descripción

Este proyecto consiste en un conjunto de scripts para generar códigos QR a partir de enlaces web especificados en un archivo CSV y organizar las imágenes resultantes en carpetas según una clasificación dada.

## Funcionalidades

El proyecto consta de dos partes principales:
1. **QR_Generator.py**: Lee un archivo CSV (`Data.csv`) donde la primera columna contiene enlaces URL y la segunda columna contiene nombres de secciones. Genera códigos QR correspondientes a cada enlace y los guarda como imágenes PNG con nombres asociados a las secciones especificadas.
   
2. **Folder_Creator.py**: Organiza las imágenes generadas por `QR_Generator.py` en carpetas según los nombres de las secciones. Cada carpeta contendrá todas las imágenes asociadas a una misma sección.

