def suma (num1,num2):
    suma=num1+num2
    return suma

def resta (num1,num2 ):
    resta = num1-num2
    return resta
    
def multiplicacion(num1, num2):
    multiplicacion = num1*num2
    return round(multiplicacion,2)

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

if proceso=="2":
    num1=float(input("Digite primer numero resta: "))
    num2=float(input("Digite segundo numero resta: "))
    print("Su resta es ",resta(num1, num2))

if proceso=="3":
    num1=float(input("Digite numero de multiplicaicon: "))
    num2=float(input("Digite numero de multiplicaicon: "))
    print("Su resultado de multiplicacion es: ",multiplicacion(num1,num2))

if proceso=="4":
      num1=float(input("ingrese el primer numero "))
      num2=float(input("ingrese el segundo numero "))
      print("resultado:",divicion(num1,num2))
