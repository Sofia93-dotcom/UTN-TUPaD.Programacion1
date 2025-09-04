#ejercicio 1
for i in range(0,101):
    print(f"{i}")

print("///////////////////////////")
#ejercicio 2
numero=int(input("Ingrese un numero:"))
cant_digitos=len(str(numero))
print(f"La cantidad de digitos del numero {numero}, es:{cant_digitos}")
print("////////////////////////////////")
#ejercicio 3
suma=0
valor_1=int(input("Ingrese un valor:"))
valor_2=int(input("Ingrese el segundo valor:"))
menor=min(valor_1,valor_2)
mayor=max(valor_1,valor_2)
for i in range(menor+1,mayor):
    suma=suma+i
print("La suma de los numeros dados es:", suma)
print("///////////////////////////////////////////")
#ejercicio 4

suma=0
numero=int(input("ingrese un numero:"))

while numero>0:
    suma=suma+numero
    numero=int(input("Ingrese un numero(0 para salir:)"))
    
print("El total de la suma de los numeros acumulados es:", suma)

#ejercicio 5
import random
aleatorio=random.randint(0,9)
intentos=0
numero=int(input("Intente adivinar el numero entre 0 y 9:"))
intentos=intentos+1
while numero!=aleatorio:
    numero=int(input("Ingrese nuevamente un numero entre 0 y 9"))
    intentos=intentos+1
print("La cantidad de intentos para acertar el numero son de:",intentos)
print("/////////////////////////////////////////////////")

#ejercicio 6
for i in range(100,-1,-2):
    print(i)

print("/////////////////////////////////////////")
#ejercicio 7

numero=int(input("Ingrese un numero entero positivo:"))
suma=0
for i in range(0,numero+1):
    
    suma=suma+i
print(f"La suma de los numeros comprendidos entre o y {numero}, es {suma}")    

print("////////////////////////////////////////////////////")

#ejercicio 8


cantidad=0
par=0
impar=0
positivo=0
negativo=0
limite=100
while cantidad<limite:
    numero=int(input("Ingrese un numero entero:"))
    cantidad+=1
    if numero%2==0:
        
        par+=1
    else:
        impar+=1
        
         
    if numero>0:
        
        positivo+=1
    elif numero<0:
        negativo+=1
        
        
print("La cantidad de numeros pares ingresados son:",par)
print("La cantidad de numeros impares ingresado son:",impar)                   
print("La cantidad de numeros negativos ingresados son:",negativo)                   
print("La cantidad de numeros positivos ingresados son:",positivo) 

print("////////////////////////////////////")

#ejercicio 9

cantidad=0
suma=0
limite=100
while cantidad<limite:
    numeros=int(input("Ingrese un nº entero:"))
    cantidad+=1
    suma+=numeros
media=suma/cantidad
print("La media de los numeros ingresados es:", media) 

print("////////////////////////////////////////////")
#ejercicio 10
numero=int(input("Ingrese un nº:"))
invertido=int(str(numero)[::-1])
print(f"El nº invertido de {numero} es:{invertido}")
    

        







