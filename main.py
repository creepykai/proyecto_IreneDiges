from controladores.gestionar_libros import crear_libro, modificar_libro

def menu_libros() -> None:
    libro_creado = None

    while True:
        print("\n--- MENÚ DE GESTIÓN DE LIBROS ---")
        print("1. Crear libro")
        print("2. Modificar libro")
        print("3. Mostrar libro")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            libro_creado = crear_libro()

        elif opcion == "2":
            if libro_creado is not None:
                modificar_libro(libro_creado)
            else:
                print("Primero debes crear un libro para poder modificarlo.")

        elif opcion == "3":
            if libro_creado is not None:
                print(libro_creado)
            else:
                print("No hay ningún libro creado.")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


menu_libros()