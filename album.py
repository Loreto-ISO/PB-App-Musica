class Album:
    
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

        print(f"{cancion.titulo} fue asociada"
              f" al álbum {self.titulo}")

        pass
    
    def mostrar_album(self):

        print(f"Título: {self.titulo}")
        print(f"Año: {self.anio} ")

        if len(self.canciones) == 0:
            print("El álbum está vacío")
        else:
            for cancion in self.canciones:
                print(f" {cancion.titulo} "
                      f" {cancion.genero}")
