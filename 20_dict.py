person = {
    'name': 'harold',
    'last_name': 'Rodriguez Navarro',
    'langs': ['python', 'javascript'],
    'age': 99
}
print(person)

# Modificar los valores de nuestro diccionario person
person['name'] = 'edward' # Cambiar valor
person['age'] -= 50 # Operar valor
person['langs'].append('go') # Añadir valor
print(person)

# Eliminar atributos
# del elimina el atributo del diccionario que se le pase
del person['last_name']
print(person)

# pop elimina el atributo que queramos 
person.pop('age') # necesita si o si un argumento o dará un error

# items Devuelve en un array pares de tuplas con las claves y valores de nuestro diccionario
print('items:',person.items())

# keys Devueve en lista unicamente las llaves de nuestro diccionario
print('keys:',person.keys())

# values Devuelve en lista unicamente los valores de nuestro diccionario
print('values:',person.values())