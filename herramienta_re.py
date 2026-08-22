# Esto nos ayudara a descargar la libreria re
import re

#ahora podremos buscar dentro del texto información

texto = "hola a ti que lees el codigo, sigueme para aprender mas"
resultado = re.search("sigueme", texto)

# Las búsquedas con re.search() son sensibles a mayúsculas y minúsculas (case-sensitive). 
# Al buscar "SIGUEME" en un texto que contiene "sigueme", 
# la función no encuentra ninguna coincidencia y devuelve None. 
# Por lo tanto, el programa se salta el if y ejecuta el else, imprimiendo "Palabra no encontrada".

if resultado:
    print(resultado)
else:
    print("Palabra no encontrada")