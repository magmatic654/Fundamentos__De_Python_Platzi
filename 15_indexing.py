text = 'Ella sabe Python'
# los corchetes [] en strings devuelven el 
# caracter que ocupe la posición proporcionada 
print(text[0]) 
print(text[1]) 

# nos da un error si no existe la posición
# print(text[999]) 

# para ver el ultimo caracter del texto podemos
# sacar el tamaño de nuestra cadena de caracteres
# con len y restarle uno
size = len(text)
print(text[size - 1])

# Otra forma más sencilla para ver el ultimo caracter 
# del texto es poniendo la posición en -1
print(text[-1])

######################################################## 
# slicing
# puedes meter un rango de números y nos 
# devolverá los caracteres contenidos 
# en ese rango: [n_inicio = 0:n_final = final]
print(text[0:5])
print(text[10:16])
print(text[:10]) # por defecto inicia en la posición 0
print(text[5:-1])
print(text[5:]) # por defecto termina en la ultima posición
print(text[:]) # va del inicio al final
print(text[10:16:1]) # salta los caracteres de uno en uno
print(text[10:16:2]) # salta los caracteres de dos en dos
print(text[::2]) # del inicio al final saltando de dos en dos