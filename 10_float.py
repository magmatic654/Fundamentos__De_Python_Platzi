x = 3.3
print(x) #output: 3.3
y = 1.1 + 2.2

print(y) #output: 3.3000000000000003

# Nos resulta como falso, ya que la operación 
# mátematica manejada en python nos dá un 
# resultado inpresiso 
print(x == y)

# Arreglando por metodo de strings
y_str = format(y, ".2g")
print('str =>', y_str)
print(y_str == str(x))

print('*'*10)
# Arreglando matematicamente
print(y, x)

tolerance = 0.00001 #Nivel de tolerancia para comparar

# Comparamos el valor absoluto de la diferencia 
# de "x" e "y" y si esta operacion es menor que
# la tolerancia dada, entonces lo damos como una 
# igualdad retornando True
print(abs(x - y) < tolerance) 