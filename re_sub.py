import re
texto = "Pedido 121231212, clave 5645645656, rut 18.158.860-4"
resultado = re.sub("[0-9]+", "----", texto)
print(resultado)
