name = "Harold"
last_name = "Rodriguez Navarro"
age = 19

print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Harold"
print(quote)

quote2 = "She said 'Hello'"
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("v1 ",template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("v2 ",template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3 ", template)

template = f"Hola mi nombre es {name}, mi apellido es {last_name} y mi edad es {age} años"
print("v4", template)