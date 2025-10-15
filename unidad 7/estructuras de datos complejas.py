#Actividades
#1)
precios_frutas={"banana":1200, "Anana":2500, "Melon":3000, "Uva":1450}
#Añadir las siguientes frutas con sus respectivos precios: naranja=1200, manzana=1500,pera=2300
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)

print("*"*50)
#ejercicio 2
#actualizar los precios de las frutas: banana=1330, manzana=1700,melon=2800
precios_frutas["banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melon"]=2800

print(precios_frutas)

print("*"*50)
#ejercicio 3
#crear una lista que contenga unicamente las frutas sin los precios
lista_frutas=list(precios_frutas.keys())
print(lista_frutas)

print("*"*50)
#ejercicio 4
#escribi un programa que permita almacenar y consultar numeros telefonicos.
#luego, pedi un nombre y mostrale el numero asociado, si existe.
contactos={"Sofia":1164485144, "Rosa":1125698470, "Raul":1159748256, "Melissa":1259861, "Alexis":11458723}
contacto=input("Ingrese el nombre del contacto:").strip().title()
if contacto in contactos:
    print(contactos[contacto])
else:
    print("El contacto solicitado no se encuentra agendado")

print("*"*50)
#ejercicio 5: solicita al usuario una frase e imprime: las palabras unicas(usando un set), un diccionario con
# #la cantidad de veces que aparece cada palabra

#pedir frase al usuario:
frase=input("Ingrese una frase:").strip().title()
palabras=frase.split()#para separar las palabras
print(set(palabras))   
#un diccionario con la cantidad de veces que aparece cada palabra
diccionario=dict.fromkeys(palabras,0)#inicializo el value en 0
for i in palabras:
    diccionario[i]+=1 

print(diccionario)    

print("*"*50)
#ejercicio 6: permiti ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#luego, mostra el promedio de cada alumno
#pedir al usuario que ingrese los nombres de los alumnos:
promedios={}
for i in range(3):
    alumno=input(f"Ingrese el nombre del alumno {i+1}:").strip().title()
    notas=tuple(float(notas) for notas in input(f"Ingrese las 3 notas de {alumno} separadas por espacios:").split())
    promedio=sum(notas)/len(notas)
    promedios[alumno]=promedio

print("\nEl promedio de cada alumno es:")
print(promedios)  

print("*"*50)
#ejercicio 7: dado dos sets de numeros, representando dos listas de estudiantes que aprobaron parcial 1 y parcial 2:
#Mostra los que aprobaron ambos parciales
#mostra los que aprobaron solo uno de los dos
#mostra la lista total de estudiantes que aprobaron al menos un parcial(sin repetir)

parcial_1={10,7,8,6,2,5}#numeros que identifican a cada estudiante
parcial_2={7,8,10,3,9,5}

#mostrar los que aprobaron ambos parciales:
ambos_parciales= parcial_1 & parcial_2
print(f"Los alumnos que aprobaron ambos parciales son: {ambos_parciales}")

#mostrar los que aprobaron solo uno de los dos:
solo_uno= parcial_1^parcial_2
print(f"Los alumnos que aprobaron solo uno de los dos parciales son: {solo_uno}")

#mostrar la lista total de estudiantes que aprobaron al menos un parcial(sin repetir)
lista_total=parcial_1|parcial_2
print(f"La lista total de estudiantes que aprobaron al menos un parcial son: {lista_total}")

print("*"*50)
#ejercicio 8: arma un diccionario donde las claves sean nombres de productos y los valores su stock
#permitir al usuario: consultar el stock de un producto ingresado, agregar unidades al stock si el producto existe
#agregar un nuevo producto si no existe

productos={"remeras":50,"jeans":20,"shorts":67,"sandalias":23}
#consultar el stock de un producto ingresado:
consultar_stock=input("Ingrese el nombre del producto del cual desea ver su stock:").strip().lower()
if consultar_stock in productos:
    print(f"El producto {consultar_stock} tiene {productos[consultar_stock]} unidades")
else:
    print("El producto ingresado no se encuentra actualmente")

#agregar unidades al stock si el producto ya existe:
unidades=input("Ingrese el nombre del producto del cual desea agregar unidades:").strip().lower()
if unidades in productos:
    agregar=int(input("Ingrese las unidades del producto:"))
    productos[unidades]+=agregar
    print("Se agrego la cantidad de unidades correctamente")
else:
    print("La cantidad de unidades que desea agregar no corresponde a un producto existente")

#agregar un nuevo producto si no existe:
agregar_nuevo=input("Ingrese el producto que desea agregar:").strip().lower()
if agregar_nuevo not in productos:
    agregar_stock=int(input("Ingrese la cantidad de unidades para el producto ingresado:"))
    productos[agregar_nuevo]=agregar_stock
else:
    print("El producto que desea agregar ya existe")

#mostrar diccionario actualizado:


print("\nProductos Actualizados:")
print(productos)

print("*"*50)
#ejercicio 9: crea una agenda donde las claves sean tuplas de (dia,hora) y los valores sean eventos
#permitir consultar que actividad hay en que dia y hora

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "19:00"): "Médico",
    ("miércoles", "10:00"): "Clase de ruso",
    ("jueves", "15:00"): "Clase de inglés",
    ("viernes", "17:00"): "Cine"
}
#permitir consultar que actividad hay en que dia y hora:
dia=input("Ingrese el dia que desea consultar:").strip().lower()
horario=input("Ingrese la hora:").strip()

if(dia,horario) in agenda:
    print(agenda[(dia,horario)])
else:
    print("El dia o horario ingresados son incorrectos")

print("*"*50)
#ejercicio 10: dado un diccionario que mapea nombres de paises con sus capitales, construi un nuevo diccionario donde:
#las capitales sean las claves, los paises sean los valores

original={"Argentina":"Buenos Aires","Noruega":"Oslo","Suecia":"Estocolmo","Francia":"Paris"}
invertido=dict(zip(original.values(),original.keys()))
print(original)
print(invertido)


    






