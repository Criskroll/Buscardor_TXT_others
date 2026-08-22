# Esto nos ayudara a descargar la libreria re
import re

#ahora podremos buscar dentro del texto información

texto = "hola a ti que lees el codigo, sigueme para aprender mas"
resultado = re.search("sigueme", texto)

print(resultado)