name = "Harold"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Harold" + " " + "Edward")
print(10 + 20)
print("Harold" + " " + "12")

age = 19
print("Mi edad es" + " " + str(age))
print(f"Mi edad es {age}")
print("Mi edad es {}".format(age))

age = input("Escribe tu edad => ")
print(type(age))
age = int(age)
print(f"Tu edad en 10 años será {age + 10} años")