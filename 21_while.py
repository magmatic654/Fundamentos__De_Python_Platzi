# While 
# Es un bucle que comprueba una proposicion logica,
# mientras esta sea verdadera, el ciclo while 
# repetirá el codigo una y otra vez hasta que 
# deje de ser verdadera la proposición

# Se ejecutará infinitamente ya que no tiene salida nunca
''''
while True:
    print('pene')

'''

# Aquí si tiene salida y es cuando counter llegue a 10
'''
counter = 0
while counter < 10:
    counter += 1
    print(counter)
'''

# Llega hasta cuando counter sea  igual 15 pues dentro contiene
# un break que rompe el ciclo  
'''
counter_2 = 0
while counter_2 < 20:
    counter_2 += 1
    if counter_2 == 15:
        break
    print(counter_2)
'''

# solo se ejecutará el codigo a partir de 
# que counter sea mayor que 15
counter_3 = 0
while counter_3 < 20:
    counter_3 += 1
    if counter_3 < 15:
        continue
    print(counter_3)



