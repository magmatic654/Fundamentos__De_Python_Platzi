"""lives = 3
print(type(lives))
age = 19
butgetJanuary = 100
butgetFebruary = 200
butgetMarch = 300
butgetaverage = (butgetJanuary + butgetFebruary + butgetMarch)/3
print("El presupuesto promedio es: ", butgetaverage)
print("type butgetaverage", type(butgetaverage))

temperature = 12.12
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number = 4500000000000000000.1
print(number)

number_b = 0.0000000000000001
print(number_b)"""

# Practice

# Presupuesto de x meses

butgetInput = input("¿Cuantos meses deseas calcular? ")
butgetInputint = int(butgetInput)

butgetList = []

i = 0
while i < butgetInputint :
  butgetXMonth = input(f"¿Cual es el presupuesto del mes {i+1}? ") 
  butgetXMonthInt = int(butgetXMonth)
  butgetList.append(butgetXMonthInt)
  i+=1

butgetListSum = sum(butgetList)
butgetListAverage = butgetListSum/i

print(butgetListAverage)