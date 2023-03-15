import pandas as pd
import numpy as np

from constants import size,boat,miss
from board import own_board,enemy_board

#**********************INICIO DEL JUEGO************************************************
def shoot (own_board=own_board,enemy_board=enemy_board,size=size,boat=boat,miss=miss):
    print("¡Bienvenido a Hundir la Flota!")
    print(own_board())
    while True:
        # Jugada del jugador
        usuario_fila = int(input("Adivina la fila: "))
        usuario_colum = int(input("Adivina la columna: "))

        # Verificar si el jugador ha acertado
        if enemy_board[usuario_fila,usuario_colum] == boat:
            print("¡Felicidades! ¡Hundiste mi barco!")
            break
        else:
            # Verificar si la jugada es válida
            if usuario_fila not in range(enemy_board) or \
                usuario_colum not in range(enemy_board):
                print("¡Oops!, ¡esa no es una ubicación en el tablero!")
            # Verificar si ya se había intentado esa ubicación
            elif enemy_board[usuario_fila][usuario_colum] == miss: #añadir fallo or barco destruido
                print("Ya intentaste esa ubicación.")
            else:
                # Actualizar el tablero y marcar la jugada como intentada
                print("¡Fallaste!")
                enemy_board[usuario_fila][usuario_colum] = miss
            # Imprimir el tablero actualizado
            print(enemy_board)
        
        # Jugada de la computadora
        comp_fila = np.random.randint(0,size)
        comp_colum = np.random.randint(0,size)

        # Verificar si la maquina ha acertado. 
        if own_board[comp_fila,comp_colum] == boat:
            print("¡La maquina hundió tu barco!")
            break
        else:
            # Verificar si ya se había intentado esa ubicación.
            if own_board[comp_fila][comp_colum] == miss: #añadir fallo or barco destruido
                print("La maquina ya intentó esa ubicación.")
            else:
                # Actualizar el tablero y marcar la jugada como intentada. 
                print("La maquina falló.")
                own_board[comp_fila][comp_colum] = miss
            # Imprimir el tablero actualizado. 
            print(own_board)


