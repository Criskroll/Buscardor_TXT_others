import re

password = "Esta es tu clave 111"
# resultado = re.search("[a-z]+", password) # [a-z] +
# resultado = re.search("[A-Z]+", password) # [A-Z] +
# resultado = re.search("[a-zA-Z]+", password) # [A-Z] +
resultado = re.search("[0-9]+", password)

print(resultado)