#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#programa principal
#llamo a la funcion

imprimir_hola_mundo()
print("*"*50)

#Ejercicio 2
def saludar_usuario(nombre):
    print("Hola", nombre)

#Programa principal
saludar_usuario("Sofia")
print("*"*50)

#Ejercicio 3: Crear una funcion llamada informacion_persona(nombre, apellido, edad, residencia) que recina 4 parametros
#e imprima: "Soy [nombre] [apellido], tengo [edad] y vivo en [residencia]".Pedir los datos al usuario
#y llamar a esta funcion con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f" Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#programa principal: Pedir datos al usuario
nombre=input("Ingrese su nombre:").title().strip()
apellido=input("Ingrese su apellido:").title().strip()
edad=int(input("Ingrese su edad:"))
residencia=input("Ingrese su residencia:").title().strip()

informacion_personal(nombre,apellido,edad,residencia)

print("*"*50)

#Ejercicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parametro y devuelva el area del circulo.
#Calcular_perimtero_circulo(radio) que reciba el radio como parametro y devuelva el perimetro del circulo.
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#definicion de funciones
import math
def calcular_area_circulo(radio):
    area=math.pi*(radio**2)
    print("El área del círculo es: ", area)

def calcular_perimetro_circulo(radio):
    perimetro=2*math.pi*radio
    print("El perímetro del círculo es:", round(perimetro,2))


#programa principal: llamar a ambas funciones para mostrar los resultados
radio=int(input("Ingrese el radio:"))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

print("*"*50)
#ejercicio 5: crear una funcion llamada segundos_a_horas(segundos) que reciba una cantidad de segundos
#como parametro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos
#y mostrar el resultado usando esta funcion.

#definir funciones
def segundos_a_horas(segundos):
    horas= segundos/3600
    return horas

#programa principal: solicitar los segundos al usuario:
segundos=int(input("Ingrese la cantidad de segundos:"))
horas=segundos_a_horas(segundos)
print(f"La cantidad de segundos ingresados: {segundos}, equivalen a {horas} horas")

print("*"*50)
#ejercicio 6: Crear una funcion llamada tabla_multiplicar(numero) que reciba un nº como parámetro 
#e imprima la tabla de multiplicar de ese nº del 1 al 10.
#pedir al usuario el nº y llamar a la función.

#función
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero}x{i} = {numero*i}")


#programa principal:
numero=int(input("Ingrese un nº:"))
tabla_multiplicar(numero)

print("*"*50)
#ejercicio 7: Crear una función llamada operaciones_basicas(a,b) que reciba dos numeros
#como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
#Mostrar los resultados de forma clara.

#funcion
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    return(suma, resta, multiplicacion, division)

#programa principal
num1=int(input("Ingrese el primer nº:"))
num2=int(input("Ingrese el segundo nº:"))
resultados=operaciones_basicas(num1,num2)

print("\nLos resultados de las operaciones son:")
print(f"Suma = {resultados[0]}")
print(f"Resta = {resultados[1]}")
print(f"Multiplicacion = {resultados[2]}")
print(f"División = {resultados[3]}")

print("*"*50)
#ejercicio 8: Crear una funcion llamada calcular_imc(peso,altura) que reciba el peso en kilogramos
#y la altura en metros, y devuelva el indice de masa corporal(IMC). Solicitar al usuario los datos y llamar a la funcion
#para mostrar el resultado con dos decimales.

#funcion:
def calcular_imc(peso,altura):
    imc=peso/altura**2
    return imc

#programa principal:
peso=float(input("Ingrese su peso en kilogramos:"))
altura=float(input("Ingrese su altura en metros:"))
imc=calcular_imc(peso,altura)
print(f"su indice de masa corporal es: {imc:.2f}")

print("*"*50)
#ejercicio 9: Crear una función llamada celsius_a_farenheit(celsius) que reciba una temperatura en grados celsius 
#y devuelva su equivalente en Farenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#función:
def celsius_a_farenheit(celsius):
    farenheit=(celsius*9/5)+32
    return farenheit
#programa principal:
temperatura=int(input("Ingrese una temperatura en grados Celsius:"))
farenheit=celsius_a_farenheit(temperatura)
print(f"El equivalente en Farenheit para la temperatura en Celsius {temperatura} es : {farenheit}")

print("*"*50)
#ejercicio 10: Crear una funcion llamada calcular_promedio(a,b,c) que reciba 3 numeros como parametros
#y devuelva el promedio de ellos.
#solicitar los numeros al usuario y mostrar el resultado usando esta funcion.

#funcion:
def calcular_promedio(a,b,c):
    promedio= (a+b+c)/3
    return promedio
#programa principal:
num1=float(input("Ingrese el primer número:"))
num2=float(input("Ingrese el segundo número:"))
num3=float(input("Ingrese el tercer número:"))

promedio=calcular_promedio(num1,num2,num3)
print("\nLas notas ingresadas son:")
print(num1)
print(num2)
print(num3)
print(f"El promedio de las tres notas es de: {promedio}")
   

