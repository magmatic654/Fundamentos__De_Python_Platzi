import random

# retorna la opción aleatoria de la maquina
def computerRandom():
    option = options(randomNumber(3))
    return option

# retorna un número aleatorio dentro de un rango del 1
# al número que elijas
def randomNumber(max):
    return random.randint(1, max)

# Pasa los números a la opción del juego (piedra, papel, tijera)
def options(random_number):
    if random_number == 1:
        return 'piedra'
    elif random_number == 2:
        return 'papel'
    else:
        return 'tijera'

user_option = input('Elije piedra, papel o tijera => ').lower()
computer_option = computerRandom()

# Mensajes de estados del juego
def winMessage():
    print(f'{user_option} gana a {computer_option}')
    print('Has ganado')

def loseMessage():
    print(f'{user_option} pierde con {computer_option}')
    print('Has perdido')

def drawMessage():
    print(f'{user_option} empata con {computer_option}')
    print('Empate')

# Lógica del juego
if user_option == computer_option:
    drawMessage()
elif user_option == 'piedra':
    if computer_option == 'tijera':
        winMessage()
    else:
        loseMessage()
elif user_option == 'papel':
    if computer_option == 'piedra':
        winMessage()
    else:
        loseMessage()
elif user_option == 'tijera':
    if computer_option == 'papel':
        winMessage()
    else:
        loseMessage()