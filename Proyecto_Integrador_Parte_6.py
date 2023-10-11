import os
import random
import readchar
from functools import *

def generar_matriz(cad):
    cadena = cad.split()
    vector = []
    for i in range(len(cadena)):
        for j in range(len(cadena[0])):
            vector.append(cadena[i][j-1])
    return vector

class Juego:
    def __init__(self, mapa, pi, pf, path):
        self.mapa = mapa
        self.posi_ini = pi
        self.posi_fin = pf
        self.path = path
    
    def mapa(self):
        return self.mapa

    def pi(self):
        return self.posi_ini
    
    def pf(self):
        return self.pf
    
    def path(self):
        return self.path


class ArchivoJuego(Juego):
    def __init__(self, mapa, pi, pf, path):
        super().__init__(mapa, pi, pf, path)
    
    def selecciona_archivo(self):
        archivo = random.choice(os.listdir(self.path))
        self.path = f"{self.path}/{archivo}"
    

    
    def leer_archivo(self):
        a = open(self.path, "rt")
        mapa = ''
        coordenadas= a.readlines(5)
        coordenadas = coordenadas[0].rstrip()
        coordenadas = list(map(int, coordenadas.split(" ")))
        self.posi_ini = (coordenadas[0], coordenadas[1])
        self.posi_fin = (coordenadas[2], coordenadas[3])
        mapa = a.readlines()
        mapa = mapa[0:]
        mapa = reduce(lambda x,y: x + y, mapa).split("\n")
        if mapa[-1] == ['']:
            del(mapa[-1])
        mapa = list(map(generar_matriz, mapa))
        
    


        self.mapa = mapa

    def imprimir_matriz(self):
        os.system("cls" if os.name == "nt" else clear)
        f = ''
        for fila in self.mapa:
            for columna in fila:
                f += columna
            print(f)
            f = ''
    
    def main_loop(self):
        px = self.posi_ini[0]
        py = self.posi_ini[1]
        self.mapa[py][px] = 'p'
        self.imprimir_matriz()
        print("\n" + "posicion: " + str(px) + ". " + str(py))

        while True:
            k = readchar.readkey()
            if k == readchar.key.UP:
                if 0 < py <= len(self.mapa) - 1:
                    if self.mapa [py - 1][px] != "#" and py > 0:
                        self.mapa[py][px] = "."
                        py -= 1
                    else:
                        pass
            elif k == readchar.key.DOWN:
                if 0 <= py < (len(self.mapa) - 1):
                    if self.mapa [py + 1][px] != "#":
                        self.mapa[py][px] = "."
                        py += 1
                    else:
                        pass
            elif k == readchar.key.LEFT:
                if 0 < px <= len(self.mapa[py]) - 1:
                    if self.mapa[py][px - 1] != "#" and px > 0:
                        self.mapa[py][px] = "."
                        px -= 1
                    else:
                        pass
            elif k == readchar.key.RIGHT:
                if 0 <= px < len(self.mapa[py]) - 1:
                    if self.mapa[py][px + 1] != "#":
                        self.mapa[py][px] = "."
                        px += 1
                    else:
                        pass

            self.mapa[py][px] = "p"
            self.imprimir_matriz()
            print("\n" + "posicion: " + str(px) + "." + str(py))

            if px == self.posi_fin[0] and py == self.posi_fin[1]:
                print("FELICITACIONES, LO LOGRASTE!!")
                break