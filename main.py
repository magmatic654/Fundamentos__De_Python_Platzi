import random

# Opciones disponibles de juego
options = ('piedra', 'papel', 'tijera')

# # Version #1
###############################################
# # retorna la opción aleatoria de la maquina
# def computerRandom():
#     option = options(randomNumber(3))
#     return option

# # retorna un número aleatorio dentro de un rango del 1
# # al número que elijas
# def randomNumber(max):
#     return random.randint(1, max)

# # Pasa los números a la opción del juego (piedra, papel, tijera)
# def options(random_number):
#     if random_number == 1:
#         return 'piedra'
#     elif random_number == 2:
#         return 'papel'
#     else:
#         return 'tijera'

# Version #2
###############################################
# Funciones
def computerRandom():
    # choice elije un elemento aleatorio dentro de una tupla o lista
    option = random.choice(options) 
    return option

def winMessage():
    print(f'{user_option} gana a {computer_option}')
    print('User ganó!')

def loseMessage():
    print(f'{user_option} pierde con {computer_option}')
    print('Computer ganó!')

def drawMessage():
    print(f'{user_option} empata con {computer_option}')
    print('Empate')


# Lógica del juego
rounds = 1
user_wins = 0
computer_wins = 0

while True:
    # Mensajes de inicio del juego
    print('*'*10)
    print('ROUND', rounds)
    print('*'*10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('Elije piedra, papel o tijera => ').lower()
    computer_option = computerRandom()

    if not user_option in options:
        print('La opción no es valida')
        continue

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        drawMessage()
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            winMessage()
            user_wins += 1
        else:
            computer_wins += 1
            loseMessage()
    elif user_option == 'papel':
        if computer_option == 'piedra':
            user_wins += 1
            winMessage()
        else:
            computer_wins += 1
            loseMessage()
    elif user_option == 'tijera':
        if computer_option == 'papel':
            user_wins += 1
            winMessage()
        else:
            computer_wins += 1
            loseMessage()
    rounds += 1

    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    elif user_wins ==2:
        print('El ganador es el usuario')
        break

    print('')