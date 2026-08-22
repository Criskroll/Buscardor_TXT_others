##instalar extensión
#pip install pypdf python-docx
import os
import re
import pypdf

def leer_pdf(nombre_archivo):
# Obtenemos la ruta absoluta de la carpeta donde vive este script
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(directorio_actual, nombre_archivo)
    
# Abrimos el documento PDF y unimos todos sus párrafos en un solo texto 📄
    lector = pypdf.PdfReader(ruta_completa)
    texto_completo = []
    for pagina in lector.pages:
#extraemos el texto de la pagina actual si existe
        texto_pagina = pagina.extract_text()
        if texto_pagina:
            texto_completo.append(texto_pagina)
    
    return "\n".join(texto_completo)

# Nombre del archivo que está en la misma carpeta
nombre_del_archivo = "colocar_nombre_del_archivo.pdf" 

# Cargamos el texto extraído del archivo
texto = leer_pdf(nombre_del_archivo)

# Realizamos la búsqueda
palabra_a_buscar = input("Escribe la palabra que deseas buscar en el PDF: ")
resultado = re.search(palabra_a_buscar, texto, re.IGNORECASE)

palabra_repetida = input("Escribe la palabra de la cual deseas contar las repeticiones: ")
coincidencias = re.findall(rf"\b{palabra_repetida}\b", texto, re.IGNORECASE)
cantidad_repetida = len(coincidencias)

if resultado:
    print(f"¡Palabra encontrada!: '{resultado.group()}' en la posición {resultado.span()}")
    print(f" Total de apariciones encontradas de '{palabra_repetida}' : {cantidad_repetida}\n")
else:
    print("Palabra no encontrada")