
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
    # Verificamos si el inventario tiene elementos para evitar errores
    if not inventario:
        return
    # Suma todas las existencias disponibles en el almacén
    total_inventario = sum(cantidad['cantidad'] for cantidad in inventario)
    print(f"Hay \033[1;32m{total_inventario}\033[0m productos en el inventario")

    #Se realiza cálculos financieros básicos sobre el total de productos.
    total_precio = sum(valor['precio'] * valor['cantidad'] for valor in inventario)
    print(f"El valor total de los productos: \033[1;32m${total_precio}\033[0m")

    producto_mas_caro = max(inventario, key=lambda p: float(p['precio']))
    producto_mayor_stock = max(inventario, key=lambda c: int(c['cantidad']))

    for producto in inventario:
        # Comparamos el precio numérico con el precio del producto más caro encontrado
        if producto.get('precio') == producto_mas_caro['precio']:
            print(f"Producto con mayor valor: \033[1;34m{producto['nombre']}\033[0m | Precio: \033[1;32m${producto['precio']}\033[0m")
        
    for producto in inventario:
        # Comparamos la cantidad numérica con la cantidad del producto con más stock
        if producto.get('cantidad') == producto_mayor_stock['cantidad']:
            print(f"Producto con mayor existencias: \033[1;34m{producto['nombre']}\033[0m | Cantidad: \033[1;34m{producto['cantidad']}\033[0m")
    
def bucar_producto (inventario, nombre_producto):
    if not inventario:
        return
    for producto in inventario:
        if nombre_producto.lower() == producto['nombre'].lower():
            print(f"\033[34m{producto['id']}.\033[0m Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def actualizar_productos (inventario):
    for producto in inventario:
        print(f"\033[1;34m id: {producto['id']}.\033[0m Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

    id = int(input("selecciona el id: "))
    for producto in inventario:
        if producto.get("id") == id:
        
            print("\n1. para cambiar precio \
                \n2. para cambiar cantidad")
            
            opcion = input("seliciona una de las opciones: ")

            if opcion == "1":
                    precio = float(input("nuevo precio para el producto: "))
                    producto['precio'] = precio
                    
                    return print(f"precio del producto \033[34m{producto['nombre']}\033[0m actualizado.")
                
            elif opcion == "2":
                    cantidad = int(input("nuevo precio para el producto: "))
                    producto['cantidad'] = cantidad
                    
                    return print(f"precio del producto \033[34m{producto['nombre']}\033[0m actualizado.") 
            
def eliminar_producto (inventario, id):
    for producto in inventario:
        if producto.get("id") == id:
            inventario.remove(producto)
            return print(f"producto \033[34m{producto['nombre']}\033[0m eliminado")
        
# Funciones de validación para asegurar la integridad de los datos
def si_vacio(valor):
    return valor == ""

def si_0_negativo(valor):
    return int(valor) <= 0
