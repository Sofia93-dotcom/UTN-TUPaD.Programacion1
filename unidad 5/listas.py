#ejercicio 1: crear una lista con las notas de 10 estudiantes.
#mostrar la lista completa
#calcular y mostrar el promedio
#indicar la nota mas alta y la mas baja
notas=[9.8,7,8,6,3,7.4,9,10,8.6,4,5]
print(notas)
suma=sum(notas)
cantidad=len(notas)
promedio= sum(notas)/len(notas)
nota_mas_alta=max(notas)
nota_mas_baja=min(notas)
print(f"el promedio es: {promedio}")
print(f"la nota mas alta es: {nota_mas_alta}")
print(f"la nota mas baja es:{nota_mas_baja}")
print("/////////////////////////////////////////////////////////")
#ejercicio 2: pedir al usuario que cargue 5 productos en una lista.
#mostrar la lista ordenada alfabeticamente usando metodo sorted()
#preguntar al usuario que producto desea eliminar y actualizar la lista.
productos=[]
for p in range(5):
    prod=input("ingrese un producto:")
    productos.append(prod)
lista_ordenada=sorted(productos)    
print(f"la lista ordenada alfabeticamente es:{lista_ordenada}")
eliminar_producto=input("¿que producto desea eliminar de la lista?")
if eliminar_producto in lista_ordenada:
    lista_ordenada.remove(eliminar_producto)
    print(f"la lista ahora es:{lista_ordenada}")
else:
    print("el producto que desea eliminar no existe")    

print("///////////////////////////////////////////////////////////")
#ejercicio 3: generar una lista con 15 numeros enteros al azar entre 1 y 100.
#crear una lista con los pares y otra con los impares
#mostrar cuantos numeros tiene cada lista
import random
numeros=[]
for i in range(15):
    aleatorio=random.randint(1,100)
    numeros.append(aleatorio)
print(f"los numeros generados son:{numeros}")    
pares=[]
impares=[]
for n in numeros:
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print(f"los numeros pares son:{pares}")
print(f"los numeros impares son:{impares}")
cantidad_pares=len(pares)
cantidad_impares=len(impares)
print(f"la lista de pares tiene {cantidad_pares} numeros")
print(f"la lista impares tiene´{cantidad_impares} numeros")  

print("////////////////////////////////////////////////////////")
#ejercicio 4: dada una lista con valores repetidos: 1- crear una nueva lista sin elementos repetidos
#2-mostrar el resultado
datos=[1,3,5,3,7,1,9,5,3]
nueva_lista=[]
for d in datos:
    if d not in nueva_lista:
        nueva_lista.append(d)
print(nueva_lista)  

print("///////////////////////////////////////////////////////")
#ejercicio 5: crear una lista con los nombres de 8 estudiantes presentes en clase.
#preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente
#mostrar la lista final actualizada
estudiantes=["Sofia","Ana","Rosa","Raul","Matias","Melissa","Ludmila","Teo"]
print(estudiantes)
opcion_1=input("¿Desea agregar un nuevo estudiante?(si/no)").lower()
if opcion_1=="si":
   nuevo_estudiante=input("Ingrese el nombre del nuevo estudiante:").title()
   estudiantes.append(nuevo_estudiante)
else:
    print("Usted no ha agregado a ningun estudiante nuevo a su lista")
opcion_2=input("¿Desea eliminar a algun estudiante?(si/no)").lower()
if opcion_2=="si":
    eliminar_estudiante=input("¿A quien desea eliminar?").title()
    if eliminar_estudiante  in estudiantes:
       estudiantes.remove(eliminar_estudiante)
    elif eliminar_estudiante not in estudiantes:
        print("El estudiante no se encuentra en su lista")   
else:
    print("Usted no ha eliminado a ningun estudiante de su lista")    

   
print(f"la lista actualizada es: {estudiantes}")

print("/////////////////////////////////////////////////////////////////")
#ejercicio 6: Dada una lista con 7 numeros, rotar todos los elementos una posicion hacia la derecha
#(el ultimo pasa a ser el primero)
lista_numeros=[1,2,3,4,5,6,7]
numeros_invertidos= lista_numeros[-1:] + lista_numeros[:-1]
print(numeros_invertidos)

print("///////////////////////////////////////////////////")
#ejercicio 7: crear una matriz(lista anidada) de 7x2 con las temperaturas minimas y maximas de una semana.
#calcular el promedio de las minimas y el de las maximas
#mostrar en que dia se registro la mayor amplitud termica.
temperaturas=[
    [10,18],
    [12,20],
    [9,22],
    [11,21],
    [11,23],
    [13,23],
    [11,22],
]
dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
#calcular el promedio de las minimas y el de las maximas, para eso primero hago las respectivas sumas
suma_minimas=0
suma_maximas=0
promedio_minimas=0
promedio_maximas=0
maxima=0
minima=0
#luego debo mostrar en que dia se registro la mayor amplitud termica.
#inicializo variables
amplitud= maxima-minima
mayor_amplitud=0
dia_mayor_amplitud=""
#bucle que recorra las temperaturas
for i in range(7):#i seria el indice de cada fila(sublista)(7 en total)
    minima=temperaturas[i][0]#accedo primero al indice de cada sublista y luego al primer elemento
    maxima=temperaturas[i][1]
    suma_minimas+=minima
    suma_maximas+=maxima
    amplitud=maxima-minima
    if amplitud>mayor_amplitud:
        mayor_amplitud=amplitud
        dia_mayor_amplitud=dias[i]
promedio_minimas=suma_minimas/7
promedio_maximas=suma_maximas/7
#muestro los resultados
print(f"El promedio de las temperaturas minimas es: {promedio_minimas}")
print(f"El promedio de las temperaturas maximas es de: {promedio_maximas}")
print(f"El dia en el cual se registro la mayor amplitud termica fue el dia: {dia_mayor_amplitud}")

print("///////////////////////////////////////////////////////////////")
#ejercicio 8: Crear una matriz con las notas de 5 estudiantes en 3 materias.
#mostrar el promedio de cada estudiante
#mostrar el promedio de cada materia
notas= [
    [2,3,6],
    [7,9,8],
    [10,10,9],
    [9,9,8],
    [8,5,9]
]
alumnos=["Sofia","Matias","Raul","Rosa","Melissa"]
#ahora debo mostrar el promedio de cada estudiante, debo primero hacer los calculos
suma=0
promedio=0
for i in range(5):
    suma=sum(notas[i])
    promedio=suma/3
    print(f"El promedio del/la estudiante{alumnos[i]} es : {promedio}")
#calculo el promedio de cada materia
materias=["Ingles","Matematica","Programacion"]

for j in range(3):
    suma=0
    for i in range(5):
        suma+=notas[i][j]
        promedio=suma/5
        print(f"El promedio de la materia{materias[j]} es: {promedio}")


print("/////////////////////////////////////////////////////")
#ejercicio 9
tablero=[
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]
#permitir que 2 jugadores ingresen posiciones(fila,columa)para colorar X o O
for i in range(3):
    for j in range(3):
        jugada=input("ingrese X o O:")
        tablero [i][j]=jugada
        for fila in tablero:
            print(fila)
            print()

#ejercicio 10: una tienda registra las ventas de 4 productos durante 7 dias, en una matriz de 4x7:
#mostrar el total vendido por cada producto
#mostrar el dia con mayores ventas totales
#indicar cual fue el producto mas vendido en la semana
#1. matriz de 4x7
ventas=[
    [4,13,5,6,3,8,9],
    [6,7,4,5,9,2,5],
    [4,7,9,10,2,5,7],
    [12,4,5,2,6,8,9]
]

productos=["Harina","pan","leche","arroz"]
dias=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
totales_ventas = [sum(fila) for fila in ventas]
mayor_total=max(totales_ventas)
dia_mayores_ventas=""
producto_mas_vendido=productos[0]
total_vendido=0
for i in range(4):#filas
    for j in range(7):#columnas
        total_vendido=sum(ventas[i])
        dia_mayores_ventas=max(ventas[i])
        indice_dia = ventas[i].index(dia_mayores_ventas)
indice_producto=totales_ventas.index(mayor_total)
producto_mas_vendido=productos[indice_producto]    

print(f"el total vendido por cada producto es de:{total_vendido}")
print(f"el dia con mayores ventas fue: {dia_mayores_ventas}")
print(f"el producto mas vendido de la semana fue: {producto_mas_vendido}")


    
    













