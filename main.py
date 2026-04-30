
import logica_servicios

def menu():
    while True:
        print("\n--- MENÚ PHOTOCAMPUS ---")
        print("1. Agregar Servicio")
        print("2. Editar Servicio")
        print("3. Eliminar Servicio")
        print("4. Salir")
        
        op = input("Seleccione: ")
        
        if op == "1":
            logica_servicios.registrar_servicio()
        elif op == "2":
            logica_servicios.editar_servicio()
        elif op == "3":
            logica_servicios.eliminar_servicio()
        elif op == "4":
            break
menu()