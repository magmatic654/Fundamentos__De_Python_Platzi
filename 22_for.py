# for
# se utiliza cuando ya tenenemos un número de iteraciones
# dadas, se itera dentro de un elemento

# range crea un número de iteraciones hasta un valor dado
'''
for i in range(1, 21):
    print(i)
'''

my_list = [59, 38, 19, 7, 19, 47, 5, 53]
for element in my_list:
    print(element)

my_tuple = ('harold', 'edward', 'martín', 'ulises')
for element in my_tuple:
    print(element)

product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for key in product:
    print(key, '=>', product[key])

# Uso de items en el for para llave-valor
for key, value in product.items():
    print(key, '=>', value)

people = [
    {
        'name': 'harold',
        'age': 34
    },
    {
        'name': 'nico',
        'age': 40
    },
    {
        'name': 'paula',
        'age': 28
    }
]

for person in people:
    print('name =>', person['name'])
    print('name =>', person['age'])