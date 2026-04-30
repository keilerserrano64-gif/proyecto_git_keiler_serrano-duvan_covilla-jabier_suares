def editar_servicio():
    servicios = gestorjson.cargar_datos()
    nombre_buscar = input("\nIngrese el nombre del paquete a editar: ")
    encontrado = False

    for servicio in servicios:
        if servicio['nombre'].lower() == nombre_buscar.lower():
            print(f"\nServicio encontrado: {servicio['nombre']}")
            
            # Pedir nuevos datos (o presionar Enter para mantener actual)
            nuevo_precio = input(f"Nuevo precio (actual: {servicio['precio']}): ")
            if nuevo_precio: servicio['precio'] = float(nuevo_precio)
            
            nueva_duracion = input(f"Nueva duración (actual: {servicio['duracion_horas']}h): ")
            if nueva_duracion: servicio['duracion_horas'] = float(nueva_duracion)
            
            nuevo_tipo = input(f"Nuevo tipo de evento (actual: {servicio['tipo_evento']}): ")
            if nuevo_tipo: servicio['tipo_evento'] = nuevo_tipo
            
            encontrado = True
            break
    
    if encontrado:
        gestorjson.guardar_datos(servicios)
        print("¡Servicio actualizado correctamente!")
    else:
        print("No se encontró ningún paquete con ese nombre.")
def eliminar_servicio():
    servicios = gestorjson.cargar_datos()
    nombre_eliminar = input("\nIngrese el nombre del paquete que desea eliminar: ")
    
    # Creamos una lista nueva sin el elemento que coincide con el nombre
    nueva_lista = [s for s in servicios if s['nombre'].lower() != nombre_eliminar.lower()]
    
    if len(nueva_lista) < len(servicios):
        gestorjson.guardar_datos(nueva_lista)
        print(f"El servicio '{nombre_eliminar}' ha sido eliminado.")
    else:
        print("No se encontró el servicio. No se realizaron cambios.")