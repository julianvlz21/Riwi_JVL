inventario = []

def agregar_productos(id, nombre, precio, cantidad):#Se crea un diccioanrio que gruarde los valores para cada producto, para posteriormente agregar el producto a la lista
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("\n\033[1;32m===============¡¡¡Registro exitoso!!!===============\033[0m")

def mostrar_inventario(inventario):
    if not inventario:
        print("\n\033[34mInventario vacio\033[0m")
    else:
        for producto in inventario:
            print(f"\033[34m{producto['id']}.\033[0m Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas(inventario):
    total_precio = sum(valor['precio']*valor['cantidad']for valor in inventario)
    print(total_precio)

    total_inventario = sum(cantidad['cantidad']for cantidad in inventario)
    print (total_inventario)

#Validaciones
def validar_datos():
    while True:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        try:
            if nombre == "" or precio <= 0 or cantidad <= 0:
                print("Datos erroneos, intente de nuevo")
                continue
            break
        except:
            ("\n\033[1,31m¡¡¡Valor invalido, intenta de nuenvo!!!\033[0m")
        return nombre, precio, cantidad
        
        


#menú para usuario
while True:
    print("\n\033[1;34m------------------------MENÚ REGISTRO INVENTARIO------------------------\033[0m")
    print("""
    \033[1;34m 1.\033[0m Agregar producto
    \033[1;34m 2.\033[0m Mostrar inventario
    \033[1;34m 3.\033[0m Calcular estadísticas
    \033[1;34m 4.\033[0m Salir

""")    
    opcion = input("Selecciona una de las opciones: ")

    if opcion == "1":
        validar_datos

    elif opcion == "2":
        mostrar_inventario(inventario)




# def si_0_negativo(valor):

#     return int(valor) <= 0

# def si_vacio (valor):

#     return valor == str("")

    # try:
    #     opcion = input("Seleccione una opción: ")
    #     if opcion == "1":
    #         print("\033[32m CAPACIDAD PARA 20 PRODUCTOS\033[0m") 
    #         cantidad = input("\nCuántos producto va a agregar: ")
    #         if si_0_negativo(cantidad) or si_vacio(cantidad):
    #             print("Valor invalido")
    #         elif int(cantidad) > 20:
    #             print("\033[32m CAPACIDAD PARA 20 PRODUCTOS\033[0m") 
    #         else:
    #             for n in range(int(cantidad)):
    #                 while True:
    #                     nombre = input("\nEscribe el nombre del productos: ")
    #                     if si_vacio(nombre):
    #                         print("\033[34m NOMBRE OBLIGATORIO\033[0m")
    #                     else:
    #                         precio = float(input("Agrega un precio al producto: "))
    #                         cantidad_pro= int(input("Escribe la cantidad de productos: "))
    #                         contador += 1

    #                         if si_0_negativo(precio) or si_0_negativo(cantidad_pro):
    #                             print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
    #                         else:    
    #                             break
    #                 agregar_productos(contador,nombre,precio,cantidad)

    # except:
    #     print("\n¡¡¡Valor invalido, intenta de nuenvo!!!")