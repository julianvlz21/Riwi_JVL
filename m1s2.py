# Inicialización de la base de datos y el identificador único
inventario = []
contador = 0

def agregar_productos(contador, nombre, precio, cantidad_):
    #Crea un diccionario para el producto y lo guarda en la lista de inventario.
    producto = {
        "id": contador,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad_
    }
    inventario.append(producto)
    print("\n\033[1;32m===============¡¡¡Registro exitoso!!!===============\033[0m")

def mostrar_inventario(inventario):
    #Recorre la lista y muestra los detalles de cada producto si no está vacía.
    if not inventario:
        print("\n\033[34mInventario vacio\033[0m")
    else:
        #Uso de for para recorer la lista inventario y mostrar caracteristicas del producto
        for producto in inventario:
            # Uso de f-strings para formatear la salida con colores
            print(f"\033[34m{producto['id']}.\033[0m Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas(inventario):
    #Se realiza cálculos financieros básicos sobre el total de productos.
    
    total_precio = sum(valor['precio'] * valor['cantidad'] for valor in inventario)
    print(f"El valor total de los productos: \033[1;32m${total_precio}\033[0m")

    # Suma todas las existencias disponibles en el almacén
    total_inventario = sum(cantidad['cantidad'] for cantidad in inventario)
    print(f"Hay \033[1;32m{total_inventario}\033[0m productos en el inventario")

# Funciones de validación para asegurar la integridad de los datos
def si_vacio(valor):
    return valor == ""

def si_0_negativo(valor):
    return int(valor) <= 0

# Bucle principal de la interfaz de usuario
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
        cantidad = input("\nCuántos producto va a agregar: ")
        # Validación de que la entrada sea un número antes de procesar
        while not cantidad.isdigit():
            print("\n\033[1;31m ¡¡¡Valor invalido, intenta de nuevo!!!\033[0m")
            cantidad = input("\nCuántos producto va a agregar: ")
            
        if si_0_negativo(cantidad):
            print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
        else:
            # Ciclo para capturar múltiples productos según la cantidad indicada
            for n in range(int(cantidad)):
                while True:
                    nombre = input("\nEscribe el nombre del productos: ")
                    contador += 1 # Incremento del ID único
                    try:
                        precio = float(input("Agrega un precio al producto: "))
                        cantidad_ = int(input("Escribe la cantidad de productos |valor entero|: "))

                        # Verificación múltiple de seguridad
                        if si_vacio(nombre) or si_0_negativo(precio) or si_0_negativo(cantidad_):
                            print("\n\033[1;31m =====!!!DATO ERRONEO¡¡¡=====\033[0m")
                            continue
                        else:
                            break
                    except ValueError:
                        # Manejo de error en caso de ingresar letras donde van números
                        print("\n\033[1;31m¡¡¡Valor invalido, intente de nuenvo!!!\033[0m")
                    
                agregar_productos(contador, nombre, precio, cantidad_)
    
    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        calcular_estadisticas(inventario)

    elif opcion == "4":
        print("\033[1;32m================PROGRAMA FINALIZADO================\033[0m")
        break

    else:
        print("\n\033[1;31m =====!!!DATO ERRONEO¡¡¡=====\033[0m")