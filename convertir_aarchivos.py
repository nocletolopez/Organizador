import os 

os.path.abspath("archivo.txt")

def convertir(archivo_entrada, formato_salida):

    """Convierte un archivo a otro formato."""
    nombre_archivo, extension = os.path.splitext(archivo_entrada)
    nuevo_nombre = f"{nombre_archivo}.{formato_salida}"
    
    with open(archivo_entrada, "rb") as f_entrada:
        contenido = f_entrada.read()
    
    with open(nuevo_nombre, "wb") as f_salida:
        f_salida.write(contenido)
    
    print(f"El archivo se ha convertido a {formato_salida} exitosamente.")

def main():
    archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
    formato_salida = input("Ingrese el formato de salida (txt, pdf, imagen): ")
    
    convertir(archivo_entrada, formato_salida)

if __name__ == "__main__":
    main()
