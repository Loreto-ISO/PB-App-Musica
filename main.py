from contenido import Contenido
from cancion import Cancion
from podcast import Podcast
from artista import Artista
from playlist import Playlist
from usuario import Usuario

def main():
    
    # CREAR CANCION
    cancion_uno = Cancion("Beat it",4.50, "Pop")
    cancion_dos = Cancion("Bad", 3.25, "Pop")

    # CREAR Podcast
    podcast_uno = Podcast("Ultima luna", 35, "Comedia", 15)

    #CREAR ARTISTA

    nuevo_artista = Artista("Michael Jackson", "Pop")

    #Asociar las canciones al artista
    nuevo_artista.agregar_cancion(cancion_uno)
    nuevo_artista.agregar_cancion(cancion_dos)

    nuevo_artista.mostrar_informacion()

    #CREAR PLAYLIST

    nueva_playlist = Playlist("Favoritos", "canciones que mes gustan")

    # nueva_playlist.mostrar_playlist()

    #AGREGAR CANCIONES A LA PLAYLIST

    nueva_playlist.agregar_cancion(cancion_uno)
    nueva_playlist.agregar_cancion(cancion_dos)

    # CREAR USUARIO
    nuevo_usuario = Usuario("Eric", "ea@gmail.com", True)
    nuevo_usuario.crear_playlist(nueva_playlist)

    nuevo_usuario.mostrar_informacion()


if __name__=="__main__":
    main()









    # # CREAR CANCION
    # cancion_uno = Cancion("Beat it",4.50, "Pop")
    # cancion_dos = Cancion("Bad", 3.25, "Pop")

    # # CREAR Podcast
    # podcast_uno = Podcast("Ultima luna", 35, "Comedia", 15)

    # #CREAR ARTISTA

    # nuevo_artista = Artista("Michael Jackson", "Pop")

    # #Asociar las canciones al artista
    # nuevo_artista.agregar_cancion(cancion_uno)
    # nuevo_artista.agregar_cancion(cancion_dos)

    # nuevo_artista.mostrar_informacion()

    # #CREAR PLAYLIST
    # nueva_playlist = Playlist("Antiguas pero bonitas", "Las mejores canciones del mundo")
    # # nueva_playlist.mostrar_playlist()

    # nueva_playlist.agregar_cancion(cancion_uno)
    # nueva_playlist.mostrar_playlist()

    # #CREAR USUARIO

    # new_user = Usuario("Juan Perez", "jp@gmail.com", True)

    # #ASOCIAR LA PLAYLIST AL USUARIO

    # new_user.crear_playlist(nueva_playlist)

    # new_user.mostrar_informacion()

    # # CREAR ALBUM

    # album1 = Album("Prime",2001)

    # #agregar canciones

    # album1.agregar_cancion(cancion_dos)

    # album1.mostrar_album()
