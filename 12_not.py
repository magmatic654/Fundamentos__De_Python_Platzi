# not
print("not True =>",not True)
print("not False =>", not False)

# not and
print("NOT AND")
print("not (True and True) =>", not (True and True))
print("not (True and False) =>", not ( True and False))
print("not (False and True) =>", not ( False and True))
print("not (False and False) =>", not ( False and False))

stock = input("Ingrese el número de stock => ")
stock = int(stock)
print(not (stock >= 50 and stock <= 500 ))