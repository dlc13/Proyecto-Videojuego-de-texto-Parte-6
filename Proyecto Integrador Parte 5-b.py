from Proyecto_Integrador_Parte_6 import *

def main():
    x = ArchivoJuego("", 0, 0, "maps")
    x.selecciona_archivo()
    x.leer_archivo()
    x.main_loop()

if __name__ == "__main__":
    main()