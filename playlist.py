

class Playlist:

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.canciones = []

    def agregar_cancion(self, cancion):

        self.canciones.append(cancion)

        print(f"{cancion.titulo} fue agregada"
              f" a la playlist {self.nombre}.")
        
    
    def eliminar_cancion(self, cancion):

        if cancion in self.canciones:

            self.canciones.remove(cancion)

            print(f"{cancion.titulo} fue eliminada "
                  f" de la playlist")
        else:
            print("La canción no está en la Playlist.")


    def mostrar_playlist(self):
        print("\n ---PLAYLIST---")
        print(f"Descripcion: {self.descripcion}")

        if len(self.canciones) == 0:
            print("La playlist está vacia")

        else:
            for cancion in self.canciones:
                print(f"{cancion.titulo}"
                      f"({cancion.genero})")