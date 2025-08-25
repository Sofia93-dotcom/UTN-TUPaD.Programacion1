#ejercicio 1
edad=int(input("Ingrese su edad:"))
#condicion
if edad >= 18:
    print("Es mayor de edad")

#..............................................................
#ejercicio 2
nota=int(input("Ingrese su nota:"))
#condicion
if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")    

#..............................................................
# ejercicio 3 
num=int(input("Ingrese un numero:"))
if num % 2==0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")   

#..........................................................
#ejercicio 4
edad=int(input("Ingrese su edad"))
if edad <12:
    print("Niño/a")
elif edad >=12 and edad <18:
    print("Adolescente") 
elif edad  >=18 and edad <30:
    print("Adulto/a joven")
else:
    print("Adulto/a") 

#.........................................................
#ejercicio 5
contrasenia=input("Ingrese una contraseña:")
if len(contrasenia) >=8 and len(contrasenia) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") 

#........................................................
#ejercicio 6
from statistics import mode, median, mean
import random
numeros_aleatorios= [random.randint(1, 100) for i in range (50)]
#calcular la moda, mediana y media
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
#imprimir por pantalla los resultados
print("moda=", moda)
print("mediana=", mediana)
print("media=", media)
#condicion
if media>mediana and mediana>moda:
    print("hay sesgo positivo")
elif media<mediana and mediana<moda:
    print("hay sesgo negativo")
else:
    print("no hay sesgo")    

    

#................................................................
#ejercicio 7
frase=input("Ingrese una frase o palabra:")
if frase.lower().endswith(("a","e","i","o","u")):
    print(f"{frase}!")
else:
    print(f"{frase}")    

#............................................................
#ejercicio 8 
nombre=input("Ingrese su nombre:")
print("Si quiere su nombre en mayusculas escriba 1")
print("Si quiere su nombre en minusculas escriba 2")
print("si quiere su nombre con la primera letra mayusculas escriba 3")
opcion=int(input("Ingrese el numero de la opcion deseada:"))
#condicion
if opcion==1:
    print(nombre.upper())
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.title())
else:
    print(f"{nombre}")            


#.................................................................
#ejercicio 9
magnitud=float(input("Ingrese la magnitud de un terremoto"))
#condicion
if magnitud <3:
    print("Muy leve(imperceptible)")
elif magnitud >=3 and magnitud <4:
    print("Leve(ligeramente perceptible)")
elif magnitud >=4 and magnitud<5:
    print("Moderado(sentido por personas, pero generalmente no causa daños)")
elif magnitud>=5 and magnitud<6:
    print("Fuerte(puede causar daños en estructuras debiles)")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte(puede causar daños significativos)")
elif magnitud>=7:
    print("Extremo(puede causar graves daños a gran escala)")
else:
    print(f"{magnitud}")   

#......................................................................
#ejercicio 10
hemisferio=input("Ingrese el hemisferio donde se encuentra(N/S):").upper()

mes=int(input("Ingrese el mes del año actual:"))
dia=int(input("Ingrese el dia de la fecha :"))


#condicion
if hemisferio=="N":
    if (mes==12 and dia >=21) or (mes in [1, 2]) or (mes==3 and dia<=20):
        print("Usted se encuentra en invierno")
    elif (mes==3 and dia>=21) or (mes in [4,5,6]) or (mes==6 and dia<=20):
        print("Usted se encuentra en primavera")
    elif (mes==6 and dia>=21) or (mes in[7,8,9]) or (mes==9 and dia<=20):
        print("usted se encuentra en verano")
    elif (mes==9 and dia>=21) or (mes in[10,11]) or (mes==12 and dia<=20):
        print("usted se encuentra en otoño")
elif hemisferio=="S":
    if(mes==12 and dia>=21) or(mes in[1,2]) or(mes==3 and dia<=20):
                 print("Usted se encuentra en verano")
    elif (mes==3 and dia>=21) or (mes in [4,5,6]) or (mes==6 and dia<=20):
        print("Usted se encuentra en otoño")
    elif (mes==6 and dia>=21) or (mes in[7,8,9]) or (mes==9 and dia<=20):
        print("usted se encuentra en invierno")
    elif (mes==9 and dia>=21) or (mes in[10,11]) or (mes==12 and dia<=20):
        print("usted se encuentra en primavera") 
else:
    print("Hemisferio incorrecto")                     

        








       


