# and
print("AND")
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

# Ejemplos de and
print("10 > 5 and 5 < 10 =>", 10 > 5 and 5 < 10)
print("10 > 5 and 5 > 10 =>", 10 > 5 and 5 > 10)

stock = input("Ingrese el número de stock => ")
stock = int(stock)
print(stock >= 50 and stock <= 500 )

# or
print("OR")
print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)

# Ejemplos de or
role = input("Digita el rol => ")
print(role == 'admin' or role == 'seller')