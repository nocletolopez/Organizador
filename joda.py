from reportlab.pdfgen import canvas
from PIL import Image
import os

def convertir_a_pdf_desde_texto(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as archivo_entrada:
        contenido = archivo_entrada.read()

        # Crear un documento PDF
        pdf = canvas.Canvas(archivo_salida)
        pdf.drawString(100, 800, contenido)
        pdf.save()

def convertir_a_pdf_desde_imagen(archivo_entrada, archivo_salida):
    imagen = Image.open(archivo_entrada)

    # Crear un documento PDF
    pdf = canvas.Canvas(archivo_salida, pagesize=imagen.size)
    pdf.drawImage(archivo_entrada, 0, 0, width=imagen.width, height=imagen.height)
    pdf.save()

def convertir_a_pdf(archivo_entrada, archivo_salida):
    extension = os.path.splitext(archivo_entrada)[1].lower()

    if extension == '.txt':
        convertir_a_pdf_desde_texto(archivo_entrada, archivo_salida)
    elif extension in ('.png', '.jpg', '.jpeg', '.gif', '.bmp'):
        convertir_a_pdf_desde_imagen(archivo_entrada, archivo_salida)
    else:
        print("Tipo de archivo no compatible para la conversión a PDF.")

def main():
    archivo_entrada = 'archivo_entrada.txt'  #
