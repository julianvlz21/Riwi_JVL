
def agregar_productos(contador, nombre, precio, cantidad_, inventario):
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

def actualizar_productos (inventario):
    for producto in inventario:
            # Uso de f-strings para formatear la salida con colores
            print(f"\033[34m{producto['id']}.\033[0m Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    
    id = input("selecciona el id: ")
    for producto in inventario:
        
        print("1. para cambiar precio \
            2. para cambiar cantidad")
        opcion = input("seliciona una de las opciones: ")
        if opcion == "1":
            if producto.get("id") == id:
                precio = input("nuevo precio para el producto: ")
                producto['precio'] = precio
                
                return print(f"precio del producto \033[34m{producto['nombre']}\033[0m actualizado.")
            
        if opcion == "2":
            if producto.get("id") == id:
                cantidad = input("nuevo precio para el producto: ")
                producto['cantidad'] = cantidad
                
                return print(f"precio del producto \033[34m{producto['nombre']}\033[0m actualizado.") 

# Funciones de validación para asegurar la integridad de los datos
def si_vacio(valor):
    return valor == ""

def si_0_negativo(valor):
    return int(valor) <= 0
