# las tuplas son inmutables, es decir, una vez creadas
# no se pueden modificar
numbers = (1, 2, 3, 4, 5)
strings = ('Harold', 'Rodrigo', 'Mathew', 'Harold')

print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print('0 =>', strings[0])
print('-1 =>', strings[-1])
print(type(strings))

# CRUD - Solo en listas (no existe en tuplas)
# [].append('')

# index para buscar elementos en tuplas
print(strings.index('Harold'))
print(strings.count('Harold'))

# Se puede asignar a una variable una lista 
# dada una tupla con list
my_list = list(strings)
print(my_list)
print(type(my_list))
my_list[1] = 'Marcos'
print(my_list)

# pasar una lista a una tupla tambien es posible
# con el mismo proceso 
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))