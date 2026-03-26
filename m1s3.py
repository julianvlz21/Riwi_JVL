#Traemos el archivo con las funciones a aplicar
import servicios_m1s3

# Inicialización de la base de datos y el identificador único
inventario = []
contador = 0

# Bucle principal de la interfaz de usuario
while True:
    print("\n\033[1;34m------------------------MENÚ REGISTRO INVENTARIO------------------------\033[0m")
    print("""
    \033[1;34m 1.\033[0m Agregar producto
    \033[1;34m 2.\033[0m Mostrar inventario
    \033[1;34m 3.\033[0m Calcular estadísticas
    \033[1;34m 5.\033[0m Actualizar precio o
    \033[1;34m 9.\033[0m Salir
    """)    
    opcion = input("Selecciona una de las opciones: ")

    if opcion == "1":
        cantidad = input("\nCuántos producto va a agregar: ")
        # Validación de que la entrada sea un número antes de procesar
        while not cantidad.isdigit():
            print("\n\033[1;31m ¡¡¡Valor invalido, intenta de nuevo!!!\033[0m")
            cantidad = input("\nCuántos producto va a agregar: ")
            
        if servicios_m1s3.si_0_negativo(cantidad):
            print("\n\033[1;31m =====!!!El valor no puede ser 0 o negaitivo¡¡¡=====\033[0m")
        else:
            # Ciclo para capturar múltiples productos según la cantidad indicada
            for n in range(int(cantidad)):
                while True:
                    nombre = input("\nEscribe el nombre del productos: ")
                    try:
                        precio = float(input("Agrega un precio al producto: "))
                        cantidad_ = int(input("Escribe la cantidad de productos |valor entero|: "))

                        # Verificación múltiple de seguridad
                        if servicios_m1s3.si_vacio(nombre) or servicios_m1s3.si_0_negativo(precio) or servicios_m1s3.si_0_negativo(cantidad_):
                            print("\n\033[1;31m =====!!!DATO ERRONEO¡¡¡=====\033[0m")
                            continue
                        else:
                            contador += 1 # Incremento del ID único
                            break
                    except:
                        # Manejo de error en caso de ingresar letras donde van números
                        print("\n\033[1;31m¡¡¡Valor invalido, intente de nuenvo!!!\033[0m")
                    
                servicios_m1s3.agregar_productos(contador, nombre, precio, cantidad_, inventario)
    
    elif opcion == "2":
        servicios_m1s3.mostrar_inventario(inventario)

    elif opcion == "3":
        servicios_m1s3.calcular_estadisticas(inventario)

    elif opcion == "5":
        servicios_m1s3.actualizar_productos(inventario)
    elif opcion == "9":
        print("\033[1;32m================PROGRAMA FINALIZADO================\033[0m")
        break

    else:
        print("\n\033[1;31m =====!!!DATO ERRONEO¡¡¡=====\033[0m")