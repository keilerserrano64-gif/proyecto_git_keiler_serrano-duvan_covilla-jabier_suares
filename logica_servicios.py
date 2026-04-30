import gestorjson  

def registrar_servicio():
    print("\n--- REGISTRO DE NUEVO SERVICIO FOTOGRÁFICO ---")
    
    nombre = input("Nombre del paquete (ej. Premium Boda): ")
    
    while True:
        try:
            precio = float(input("Precio del servicio: $"))
            break
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico para el precio.")

    print("Tipos de evento: Boda, Retrato, Producto, Social, Corporativo")
    tipo_evento = input("Tipo de evento: ")

    while True:
        try:
            duracion = float(input("Duración estimada (en horas): "))
            break
        except ValueError:
            print("Error: Ingrese la duración en formato numérico (ej. 2.5).")

    nuevo_servicio = {
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo_evento,
        "duracion_horas": duracion
    }

    servicios = gestorjson.cargar_datos()
    servicios.append(nuevo_servicio)
    gestorjson.guardar_datos(servicios)
    
    print(f"\n¡Servicio '{nombre}' registrado con éxito!")