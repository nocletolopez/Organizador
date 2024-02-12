import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

ruta = BASE_DIR/ "archivo.txt"
print(ruta)

def convertir_a_txt(ruta, archivo_salida):
    """Convierte un archivo a formato TXT."""
    with open(ruta, "rb") as f_entrada:
        contenido = f_entrada.read()
    with open(archivo_salida, "w") as f_salida:
        f_salida.write(contenido.decode("utf-8"))

def convertir_a_pdf(ruta, archivo_salida):
    """Convierte un archivo a formato PDF."""
    from pdfrw import PdfWriter

    with open(ruta, "rb") as f_entrada:
        contenido = f_entrada.read()
    pdf_writer = PdfWriter()
    pdf_writer.addpage(contenido)
    pdf_writer.write(archivo_salida)

def convertir_a_imagen(ruta, archivo_salida):
    """Convierte un archivo a formato de imagen."""
    from PIL import Image

    with open(ruta, "rb") as f_entrada:
        imagen = Image.open(f_entrada)
    imagen.save(archivo_salida)

def main():
    """Función principal del programa."""
    # Obtener el nombre del archivo de entrada
    ruta = input("Ingrese el nombre del archivo de entrada: ")

    # Obtener el formato de salida
    formato_salida = input("Ingrese el formato de salida (txt, pdf, imagen): ")

    # Validar el formato de salida
    if formato_salida not in ["txt", "pdf", "imagen"]:
        print("Formato de salida no válido.")
        return

    # Generar el nombre del archivo de salida
    archivo_salida = Path(ruta).with_suffix("." + formato_salida)

    # Convertir el archivo
    if formato_salida == "txt":
        convertir_a_txt(ruta, archivo_salida)
    elif formato_salida == "pdf":
        convertir_a_pdf(ruta, archivo_salida)
    elif formato_salida == "imagen":
        convertir_a_imagen(ruta, archivo_salida)

    # Mostrar un mensaje de éxito
    print(f"El archivo se ha convertido a {formato_salida} exitosamente.")

if __name__ == "__main__":
    main()
