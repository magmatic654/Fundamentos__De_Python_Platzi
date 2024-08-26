# Las listas son un conjunto de cosas a las cuales se 
# les puede meter cualquier tipo de dato
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'Hello'] # Puede ser de cualquier tipo de datos juntos
print(types)

# imprimiendo listas por posición
print(numbers[0]) # Primera posición de la lista 
print(tasks[0])

# text = 'Hola'
# text[0] = 'W' Las cadenas de texto son inmutables

# las listas son mutables
tasks[1] = 'watch platzi couses' 
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

# slicing aplicado a listas
print(numbers[:3])

# in en listas (retorna si hay un elemento 
# especifico dentro de la lista)
print(True in types)
print('Hello' in types)