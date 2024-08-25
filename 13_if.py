# Condicional if
if True:
    print("Debería ejecutarse")

if False:
    print("Nunca se ejecuta")


pet = input('¿Cúal es tu mascota favorita? ')
if pet == 'perro':
    print('Genial, tienes buen gusto')
elif pet == 'gato':
    print('Espero tengas suerte')
elif pet == 'pez':
    print('eres lo maximo')
else:
    print("no tienes ninguna mascota interesante")

'''
stock = int(input("Digita el stock => "))

if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
    print('el stock es incorrecto')
'''
