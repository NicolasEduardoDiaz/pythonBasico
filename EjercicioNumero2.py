num1 = input("Ingresar el numero 1: ")
num2 = input("Ingresar el numero 2: ")
num3 = input("Ingresar el numero 3: ")
if (num1 > num2) and (num2 > num3):
    mayor = num1 
elif (num2 > num3): 
    mayor = num2
else :
    mayor = num3
print(mayor)