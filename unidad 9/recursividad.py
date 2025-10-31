#1)- Crea una función recursiva que calcule el factorial de un nº. Luego, utiliza esa función para calcular y mostrar
#en pantalla el factorial de todos los números enteros entre 1 y el nº que indique el usuario

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(5))    

numero=int(input("Ingrese un número :  ").strip())
for i in range(1,numero+1):
    print(f"El factorial de {i} es : {factorial(i)}")

print("*"*40) 
#2)- Crea una función recursiva que calcule el valor de la serie Fibonacci en la posición indicada.
# #Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(numero):
    if numero==0:
        return 0
    elif numero==1:
        return 1
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)

print(fibonacci(10))  

posicion=int(input("Ingrese la posición: "))
for i in range(posicion+1):
    print(fibonacci(i))


print("*"*40)
#3)-Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula
#n**m=n*n(m-1). Prueba esta función en un algoritmo general

def potencia(base,exponente):
    if exponente==0:
        return 1
    else:
        return base*potencia(base,exponente-1)
print(potencia(2,4))  

#algoritmo general
base=int(input("Ingrese la base:"))
exponente=int(input("Ingrese el exponente:"))

print(potencia(base,exponente))
print("*"*40)
#Crear una función recursiva que reciba un nº entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def binario(numero):
  if numero==0:
      return "0"
  elif numero==1:
      return "1"
  else:
      return  binario(numero // 2) + str(numero % 2)
print(binario(10))  

print("*"*40)
#5)-Implementá una función recursiva llamada es_palindormo(palabra)que reciba una cadena de texto sin espacios ni tildes y devuelva True si es un palindromo
#o False si no lo es. La solución debe ser recursiva y no se debe usar [::-1] ni la función reversed()

def es_palindromo(palabra):
    if len(palabra)==1:
        return True
    elif palabra[0]!=palabra[-1]:#comparo la primera con la última letra
        return False

    else:
        return es_palindromo(palabra[1:-1])
print(es_palindromo("oso")) 

print("*"*40)
#6)- Escribi una función recursiva llamada suma:digitos(n) que reciba un nº entero positivo y devuelva la suma de todos sus digitos.
def suma_digitos(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (n%10)+suma_digitos(n//10)
print(suma_digitos(345))   

print("*"*40)
#7)-Un niño esta construyendo una piramide con bloques. En el nivel mas bajo coloca n bloques
#en el siguiente nivel uno menos(n-1) y asi sucesivamente hasta llegar aql ultimo nivel con un solo bloque.
def contar_bloques(n):
    if n==0:
        return 0
    else:
        return n+contar_bloques(n-1)
print(contar_bloques(10))    

print("*"*40)
#8)-Escribi una función recursiva llamada contar_digito(numero,digito)que reciba un número entero positivo(numero)
#y un digito(entre 0 y 9) y devuelva cuantas veces aparece ese digito dentro del numero
def contar_digito(numero,digito):
    if numero==0:
        return 0
    else:
     
     ultimo = numero % 10  # tomo el último dígito
     resto = numero // 10     # quito el último dígito
    if ultimo == digito:
            return 1 + contar_digito(resto, digito)
    else:
             return contar_digito(resto, digito)    
       
             
       

        
    

  
   
    





    
    
   
        
    



