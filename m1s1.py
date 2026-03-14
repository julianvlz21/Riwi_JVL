nombre = str(input("\nEscribe el nombre del productos: "))

while True:
    try:
        precio = float(input("Agrega un precio al producto: "))
        cantidad = int(input("Escribe la cantidad de productos: "))

        if precio < 0 or cantidad <= 0:
            print("El valor no puede ser 0 o negaitivo") 
            continue
    except:
        print("\n¡¡¡Valor invalido, intenta de nuenvo!!!")
        
    costo_total = precio * cantidad