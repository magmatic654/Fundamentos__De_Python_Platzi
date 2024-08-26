# CRUD Create, Read, Update & Delete

# Create
numbers = [1,2,3,4,5]

###############################################################
# Read
print(numbers)

###############################################################
# Update
numbers[-1] = 10
print(numbers)

# Añadir valores nuevos a la lista 
# append los añade al final de la lista
numbers.append(120)
print(numbers)

# insert los añade en la posición que quieras
numbers.insert(0, True)
print(numbers)
numbers.insert(3, 'change')
print(numbers)

# Unir dos listas con signo de suma
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

# Encontrar la posicion de un elemento en una lista
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

###############################################################
# Delete
# remove elimina el elemento que quieras
new_list.remove('todo 1')
print(new_list)

# pop por defecto elimina el último elemento de la lista
# si le envias una posición eliminará ese elemento
new_list.pop() # ultima posición
print(new_list)

new_list.pop(0) # primera posición
print(new_list)

###############################################################
# Más métodos
# reverse invierte la lista
new_list.reverse()
print(new_list)

# sort ordena lista de numeros o en orden de abecedario 
# pero sin mezclarse numeros y caracteres
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings_1 = ['aw', 'aa', 'cd', 'fg']
strings_1.sort()
print(strings_1)