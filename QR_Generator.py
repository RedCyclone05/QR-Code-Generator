# Este programa lee un archivo CSV y convierte los links de la primera columna en codigos QR 
# y los guarda con el nombre del elemento correspondiente de la segunda columna.

# Es necesario correr estos dos comandos en terminal si es la primera vez que se usa 
# "pip install pandas" y "pip install qrcode[pil]"
# Se necesitan ambas o dara error, es importante asegurarse que al dar enter se comience la instalación.

import pandas as pd
import qrcode
import re  # Importar la biblioteca re para usar expresiones regulares

# Función para generar código QR
def generar_qr(texto, section):
    qr = qrcode.QRCode(
        version=5, # Va de 1 a 40 y representa la cantidad de informacion que puede guardar
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=25, # Ajustar tamaño de imagen
        border=4,
        
    )
    qr.add_data(texto)
    qr.make(fit=True)

    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    nombre_archivo = f"QR {section}"
    imagen_qr.save(nombre_archivo + ".png")



# Función para sanitizar los nombres de archivo
def sanitize_filename(name):
    # Convertir el nombre a cadena de texto si no lo es
    name = str(name)
    # Reemplazar caracteres no permitidos en nombres de archivo con '_'
    return re.sub(r'[\/:*?"<>|]', '_', name)


# Leer el archivo CSV
def leer_csv(nombre_archivo):
    # Cargar el CSV desde la celda A2
    df = pd.read_csv(nombre_archivo, header=None, skiprows=1)

    # Asignar nombres a las columnas
    df.columns = ["links", "Section"]

    # Mostrar las variables para comprobar lectura
    print("Columna 'links':")
    print(df['links'])
    print("\nColumna 'Section':")
    print(df['Section'])

    # Generar los códigos QR
    for index, row in df.iterrows():
        nombre_archivo_qr = sanitize_filename(row['Section'])
        contenido_qr = row['links']
        generar_qr(contenido_qr, nombre_archivo_qr)


# Nombre del archivo CSV (ajusta el nombre según tu archivo)
nombre_archivo_csv = 'Data.csv'

# Llamar a la función para leer el CSV y generar los códigos QR
leer_csv(nombre_archivo_csv)


