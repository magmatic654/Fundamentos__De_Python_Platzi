text = 'Ella sabe programar en Python'

# in sirve para comprobar si un texto está dentro de otro texto 
print('Javascript' in text) # output => False
print('Python' in text) # output => True

if 'Python' in text:
    print('Elegiste bien!')
else:
    print('Bien!')

# len devuelve el número de caracteres 
# de nuestro texto (los espacios también cuentan)
size = len(text)
print(size)

# upper devuelve nuestro texto pero 
# con los caracteres en mayusculas
print(text.upper())

# lower devuelve nuestro texto pero 
# con los caracteres en minusculas
print(text.lower())

# count devuelve el número de veces que
# se repite un caracter en especifico
print(text.count('a'))

# swapcase devuelve el texto con las mayusculas y minusculas
# invertidas
print(text.swapcase())

# startswith devuelve True o False en funcion de si el texto 
# base inicia igual que el texto proporcionado
print(text.startswith('Ella'))

# endswith devuelve True o False en funcion de si el texto 
# base finaliza igual que el texto proporcionado
print(text.endswith('JS'))

# replace remplaza una cadena de caracteres 
# que especifiquemos por otra que queramos
print(text.replace('Python', 'Rust'))

text_2 = 'este es un titulo'
print(text_2)

# capitalize pone el primer caracter de 
# la cadena de texto en mayuscula
print(text_2.capitalize())

# title cambia a mayusculas cada inicio de 
# palabra entre nuestra cadena de textos
print(text_2.title())

# isdigit devuelve si la cadena de textos es un número
print(text_2.isdigit())
print('20'.isdigit())