from gestordetareas.excepciones import CampoVacioError, TareaNoEncontradaError, CategoriaNoEncontradaError

class UIConsola:
    def __init__(self, gestor_tareas):
        """Inicializa la interfaz de consola."""
        self.gestor_tareas = gestor_tareas
        self.opciones = {
            "1": self.crear_cuenta,
            "2": self.cambiar_contraseña,
            "3": self.iniciar_sesion,
            "4": self.crear_tarea,
            "5": self.editar_tarea,
            "6": self.crear_categoria,
            "7": self.agrupar_tareas_por_categoria,
            "8": self.eliminar_tarea,
            "9": self.generar_informe,
            "0": self.salir
        }

    def mostrar_menu(self):
        """Muestra el menú principal."""
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear cuenta")
        print("2. Cambiar contraseña")
        print("3. Iniciar sesión")
        print("4. Crear tarea")
        print("5. Editar tarea")
        print("6. Crear categoría de tareas")
        print("7. Agrupar tareas por categorías")
        print("8. Eliminar tarea")
        print("9. Generar informe")
        print("0. Salir")

    def ejecutar_app(self):
        """Ejecuta la aplicación y muestra el menú en un bucle."""
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción: ").strip()  # Limpiamos espacios en blanco
            if opcion.isdigit() and opcion in self.opciones:
                accion = self.opciones[opcion]
                try:
                    accion()
                except CampoVacioError as e:
                    print(f"Error: {e.message}")
                except TareaNoEncontradaError as e:
                    print(f"Error: {e.message}")
                except CategoriaNoEncontradaError as e:
                    print(f"Error: {e.message}")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")
            else:
                print("Opción no válida, intenta de nuevo.")

    # Métodos para las opciones del menú...
