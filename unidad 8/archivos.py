#Objetivo: Comprender y aplicar el uso de archivos de texto en Python, desarrollando un pequeño
#programa que lea, procese y almacene informacion sobre productos de manera persistente.
#Se busca que el estudiante manipule datos a traves de estructuras como listas y diccionarios
#integrando lectura,escritura y buenas practicas con archivos.

#Actividades:
#1)-Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con 3 productos
#cada linea debe tener: nombre,precio,cantidad

#crear archivo productos.txt:
print("1. Creando archivo")
archivo_productos=open("productos.txt","w")
archivo_productos.write(" Cartuchera,2000,50\n")

archivo_productos.write("Goma,500,35\n")
archivo_productos.write("Lapiz,1000,50\n")
archivo_productos.close()


#2)-Leer y mostrar productos:Crear un programa que abra productos.txt, lea cada linea, la procese con .strip()
#y.split(",") y muestre los productos en el siguiente formato:
#producto: lapicera|precio:$120.5|cantidad:30

print("Leyendo y mostrando los productos...")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()           # quita el salto de línea
        partes = linea.split(",")        # separa por comas
        # unir las partes con “|” en el formato pedido
        print(" | ".join(parte.strip() for parte in partes))

print("*"*50)      

#3)-Agregar productos desde teclado:Modificar el programa para que luego de mostrar los productos, le pida
#al usuario que ingrese un nuevo producto(nombre,precio,cantidad)y lo agregue al archivo sin borrar el contenido existente
with open("productos.txt","r") as archivo:
    for linea in archivo:
        print(linea)
agregar_nuevo_producto=input("Ingrese un nuevo producto(nombre):").strip()  
agregar_precio=input("Ingrese el precio del producto:").strip()
agregar_cantidad=input("Ingrese la cantidad del producto ingresado:").strip()
print("Agregando nuevo producto...")
with open("productos.txt","a")as archivo:
    archivo.write(f"{agregar_nuevo_producto},{agregar_precio},{agregar_cantidad}\n")
    print(f"Producto agregado correctamente: {agregar_nuevo_producto},{agregar_precio},{agregar_cantidad}")

print("*"*50)
#4)-cARGAR PRODUCTOS EN UNA LISTA DE DICCIONARIOS: AL LEER EL ARCHIVO, CARGAR LOS DATOS EN UNA LISTA LLAMADA "PRODUCTOS"
#donde cada elemento sea un diccionario con claves: nombre,precio,cantidad
#leer el archivo:
print("Mostrando productos...")
productos=[]
with open("productos.txt","r") as archivo:
    for linea in archivo:
        linea=linea.strip()
        partes=linea.split(",")
        nombre=partes[0]
        precio=partes[1]
        cantidad=partes[2]

        #crear diccionario
        diccionario_productos={"nombre": nombre,"precio": precio,"cantidad": cantidad}
        productos.append(diccionario_productos)
print(productos)

print("*"*50)
#5)- buscar producto por nombre: pedir al usuario que ingrese el nombre de un producto
#recorrer la lista de productos y si lo encuentra, mostrar todos sus datos
#ai no existe,mostrar un msj de error.
producto=input("Ingrese el nombre del producto:").strip().lower()
encontrado=False
with open("productos.txt","r")as archivo:
    for linea in archivo:
        linea=linea.strip()
        if producto in linea.lower():
            partes=linea.split(",")
            nombre = partes[0].strip()
            precio = partes[1].strip()
            cantidad = partes[2].strip()

            print(f"las caracteristicas del producto son nombre: {nombre}, precio:{precio}, cantidad: {cantidad}")
            encontrado=True
if not encontrado:
    print("Error. El producto no existe")

print("*"*50)
#6)- guardar los productos actualizados:Despues de haber leido, buscado o agregado productos, sobresscribir el archivo productos.txt
#escribiendo nuevamente todos los productos actualizados de la lista.
print("Escribiendo productos actualizados...")
with open("productos.txt", "w", ) as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

productos=open("productos.txt","r")
contenido=productos.read()
print(contenido)
productos.close()





        


 






