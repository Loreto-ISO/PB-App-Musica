class Artista:

    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

        print(f"{cancion.titulo} fue asociada"
              f" al artista {self.nombre}")

    def mostrar_informacion(self):

        print("\n ---Artista ---")
        print(f"Nombre {self.nombre}")
        print(f"Genero {self.genero}")
        print("canciones")

        if len(self.canciones) == 0: #logica de negocio de una aplicacion
            print("no tiene canciones registradas")
        else:
            for cancion in self.canciones:
                print(f"- {cancion.titulo}")

