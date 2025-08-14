#ejercicio 1
print ("Hola mundo")
#..................................



#ejercicio 2
nombre=input("Ingrese su nombre:")
print(f"Hola {nombre}!")

#........................................


#ejercicio 3
nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
lugar_residencia= input("Ingrese su lugar de residencia: ")
edad= input("Ingrese su edad: ")
print(f"Soy {nombre}  {apellido}, tengo {edad} años y vivo en {lugar_residencia} ")

#......................................



#ejercicio 4

import math

radio= float(input("Ingrese el radio de un circulo"))
area= math.pi*(radio**2)
perimetro= 2*math.pi *radio

print(f"El area es: {area} , y el perimetro es: {perimetro}  ")

#.......................................
#ejercicio 5
segundos= int (input("Ingrese la cantidad de segundos : "))
horas= int(segundos/3600) 
print(f"las horas equivalentes a {segundos} segundos es: {horas}")


#...........................................



#ejercicio 6
numero=int(input("Ingrese un numero: "))

resultado1=numero*1
resultado2=numero*2
resultado3=numero*3
resultado4=numero*4
resultado5=numero*5
resultado6=numero*6
resultado7=numero*7
resultado8=numero*8
resultado9=numero*9
resultado10=numero*10

print(f"{numero} *1={resultado1}")
print(f"{numero} *2={resultado2}")
print(f"{numero} *3={resultado3}")
print(f"{numero} *4={resultado4}")
print(f"{numero} *5={resultado5}")
print(f"{numero} *6={resultado6}")
print(f"{numero} *7={resultado7}")
print(f"{numero} *8={resultado8}")
print(f"{numero} *9={resultado9}")
print(f"{numero} *10={resultado10}")


#.....................................

#ejercicio 7
numero1=int(input("Ingrese un numero distinto de cero: "))
numero2=int(input("Ingrese un segundo numero distinto de cero: "))

print(numero1+numero2)

print(numero1//numero2)

print(numero1*numero2)

print(numero1- numero2)

#........................................

#ejercicio 8
altura=float(input("Ingrese su altura: "))
peso=float(input("ingrese su peso: "))
imc=peso/(altura**2)
print("Su indice de masa corporal es" , imc)


#.......................................
#ejercicio 9

temp_celsius=int(input("Ingrese temperatura en grados Celsius: "))
grado_f=float(9/5*temp_celsius)+32
print("La equivalencia en fahrenheit es: " , grado_f)

#.......................................

#ejercicio 10

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
promedio=(num1+num2+num3)/3

print(f"El promedio es: {promedio}")
