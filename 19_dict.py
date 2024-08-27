# Diccionario
# Los diccionarios contienen claves y valores. 
# Las claves o keys, son aquellos elementos con los 
# que los podremos identificar los elementos.
# las claves o values, son aquellos valores que tienen
# las claves, pueden ser strings, listas, tuplas, numbers
# incluso otro diccionario.
my_dict = {}
print(type(my_dict))

my_dict = {
    #Llave  #Valor
    'name': 'Harold',
    'last_name': 'Rodriguez Navarro',
    'age': 22
}
# Imprime en pantalla el diccionario
print(my_dict)
print(type(my_dict))

# buscar los valores dando el nombre de la llave
print(my_dict['age'])
print(my_dict['last_name'])

# get 
# devuelve la clave de una llave y permite manejar 
# el caso en el que la llave no exista retornando 
# un none
print(my_dict.get('unvalor'))

# in comprueba si la llave se encuentra dentro de 
# nuestro diccionario, con esto se puede prevenir 
# un error para el caso que queramos buscar los valores
# dando el nombre de una llave
print('name' in my_dict)
print('avion' in my_dict)