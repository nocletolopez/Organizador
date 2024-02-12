import os

def organizar_archivos(ruta_carpeta):
  """
  Organiza los archivos en una carpeta según su extensión.

  Parámetros:
    ruta_carpeta: La ruta a la carpeta que se desea organizar.
  """

  # Lista de extensiones
  extensiones = [".txt", ".pdf", ".jpg", ".png", ".docx", ".json", ".mp4", ".csv"]

  # Crea una carpeta para cada extensión
  for extension in extensiones:
    carpeta_extension = os.path.join(ruta_carpeta, extension)
    if not os.path.exists(carpeta_extension):
      os.makedirs(carpeta_extension)

  # Mueve los archivos a las carpetas correspondientes
  for archivo in os.listdir(ruta_carpeta):
    nombre_archivo, extension = os.path.splitext(archivo)
    ruta_archivo = os.path.join(ruta_carpeta, archivo)
    ruta_destino = os.path.join(ruta_carpeta, extension, archivo)
    if extension in extensiones:
      os.rename(ruta_archivo, ruta_destino)

# Ruta de la carpeta a organizar
ruta_carpeta = "C:\Coder Python"

# Organiza los archivos
organizar_archivos(ruta_carpeta)

print("Los archivos se han organizado correctamente.")
