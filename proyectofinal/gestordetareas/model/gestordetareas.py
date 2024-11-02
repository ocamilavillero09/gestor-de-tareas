from gestordetareas.excepciones import CampoVacioError, TareaNoEncontradaError, CategoriaNoEncontradaError

class GestorTareas:
    def __init__(self):
        """Inicializa el gestor con usuarios y tareas vacías."""
        self.usuarios = {}
        self.categorias = {}

    def registrar_usuario(self, nombre_usuario, contrasena, correo):
        """Registra un nuevo usuario."""
        if not nombre_usuario or not contrasena or not correo:
            raise CampoVacioError("nombre_usuario, contrasena o correo")
        if nombre_usuario in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena, correo)
            print(f"Usuario {nombre_usuario} registrado exitosamente.")

    def crear_categoria(self, nombre, descripcion):
        """Crea una nueva categoría."""
        if not nombre or not descripcion:
            raise CampoVacioError("nombre o descripcion")
        if nombre in self.categorias:
            print("La categoría ya existe.")
        else:
            self.categorias[nombre] = Categoria(nombre, descripcion)
            print(f"Categoría '{nombre}' creada.")

    def eliminar_tarea(self, titulo):
        """Elimina una tarea existente."""
        for categoria in self.categorias.values():
            for tarea in categoria.tareas:
                if tarea.titulo == titulo:
                    categoria.eliminar_tarea(tarea)
                    print(f"Tarea '{titulo}' eliminada.")
                    return
        raise TareaNoEncontradaError(titulo)

    def obtener_categoria(self, nombre):
        """Obtiene una categoría por su nombre."""
        categoria = self.categorias.get(nombre)
        if not categoria:
            raise CategoriaNoEncontradaError(nombre)
        return categoria

 
