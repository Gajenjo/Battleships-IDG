import pandas as pd
import numpy as np

from constants import size,boat,miss, boat_damaged
from board import own_board,enemy_board,blank_board

#**********************INICIO DEL JUEGO************************************************


def shoot (miss=miss,board_enemy=enemy_board(),board_own=own_board(),board_blank=blank_board(),boat_damaged = boat_damaged):

    print(board_enemy) #BORRAR SOLO PARA PRUEBAS
    while True:
        # Jugada del jugador
        usuario_fila = int(input("Adivina la fila: "))
        usuario_colum = int(input("Adivina la columna: "))

        # Jugada de la computadora
        comp_fila = np.random.randint(0,size)
        comp_colum = np.random.randint(0,size)

        # Verificar si el jugador ha acertado
        if usuario_fila > size or \
                usuario_colum > size:
                print("¡Oops!, ¡esa no es una ubicación en el tablero!")
                continue
        elif board_enemy[usuario_fila,usuario_colum] == boat:
            board_enemy[usuario_fila,usuario_colum] = boat_damaged
            board_blank[usuario_fila][usuario_colum] = boat_damaged
            # print(pd.DataFrame(board_enemy))
            print("¡Felicidades! ¡tocaste mi barco!")
            Jugador=pd.DataFrame(board_own)
            Maquina=pd.DataFrame(board_blank) 
            espacio=pd.DataFrame(np.full((10,1),"|"))
            resultado=pd.concat([Jugador,espacio,Maquina],axis=1)
            print(resultado)

            continue
            # board_enemy[comp_fila][comp_colum] = boat_damaged #********************
        elif boat not in board_enemy:
            print("Felicidades, ¡has ganado!")
            break

            
        else:
            # Verificar si la jugada es válida
            if board_enemy[usuario_fila][usuario_colum] == miss or\
                board_enemy[usuario_fila][usuario_colum] == boat_damaged: #cambiar a boat_damage
                print("Ya intentaste esa ubicación.")
            else:
                # Actualizar el tablero y marcar la jugada como intentada
                print("¡Fallaste!")
                board_enemy[usuario_fila][usuario_colum] = miss
                board_blank[usuario_fila][usuario_colum] = miss
        


        # Verificar si la maquina ha acertado. 
        if board_own[comp_fila,comp_colum] == boat:
            print("¡La maquina tocó tu barco!") #####************
            board_own[comp_fila][comp_colum] = boat_damaged #********************
            Jugador=pd.DataFrame(board_own)
            Maquina=pd.DataFrame(board_blank) 
            espacio=pd.DataFrame(np.full((10,1),"|"))
            resultado=pd.concat([Jugador,espacio,Maquina],axis=1)
            print(resultado)
            continue
        else:
            # Verificar si ya se había intentado esa ubicación.
            if board_own[comp_fila][comp_colum] == miss: #añadir fallo or barco destruido
                print("La maquina ya intentó esa ubicación.")
            elif boat not in board_own:
                print("Perdiste")
            else:
                # Actualizar el tablero y marcar la jugada como intentada. 
                print("La maquina falló.")
                board_own[comp_fila][comp_colum] = miss
                
        # Imprimir el tablero actualizado. 
        Jugador=pd.DataFrame(board_own)
        Maquina=pd.DataFrame(board_blank) 
        espacio=pd.DataFrame(np.full((10,1),"|"))
        resultado=pd.concat([Jugador,espacio,Maquina],axis=1)
        print(resultado)


