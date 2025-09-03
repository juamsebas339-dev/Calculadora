def suma (num1,num2):
    suma=num1+num2
    return suma

def divicion (num1,num2):
    if num2 != 0:
        divicion=num1/num2
        return divicion
    else:
        return "Error divisor = a 0"


print ("Calculadora")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. divicion")
proceso=input("Que opcion deseas realizar (1-4): ")
if proceso=="1":
      num1=float(input("ingrese el primer numero "))
      num2=float(input("ingrese el segundo numero "))
      print("resultado:",suma(num1,num2))
if proceso=="4":
      num1=float(input("ingrese el primer numero "))
      num2=float(input("ingrese el segundo numero "))
      print("resultado:",divicion(num1,num2))

 