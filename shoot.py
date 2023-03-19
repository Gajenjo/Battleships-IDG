import pandas as pd
import numpy as np

import pygame
pygame.init()
import time
from colorama import Fore, Style


from constants import size,boat,miss, boat_damaged
from board import own_board,enemy_board,blank_board

#*************************************INICIO DEL JUEGO************************************************#

# Cargar sonido de explosión
sonido_explosion = pygame.mixer.Sound('explosion-01.wav')

# Reproducir sonido de explosión
sonido_explosion.play()

# Esperar a que el sonido termine de reproducirse
pygame.time.wait(int(sonido_explosion.get_length() * 1000))


# Función del juego 

def shoot (miss=miss,board_enemy=enemy_board(),board_own=own_board(),board_blank=blank_board(),boat_damaged = boat_damaged):

# Comienzo del juego

    print(Fore.BLUE + "¡BIENVENIDO AL JUEGO HUNDIR LA FLOTA!\n" + Style.RESET_ALL)
    time.sleep(1)

    print(Fore.GREEN + "Instrucciones\n" + Style.RESET_ALL)
    time.sleep(1)

    print("El objetivo del juego es hundir todos los barcos de tu oponente antes de que él hunda los tuyos.\n")
    time.sleep(2)

    print("Para jugar, introduce las coordenadas de la casilla donde quieres lanzar un misil.\n\n"
    " - Si aciertas en una casilla donde hay un barco, lo dañarás y se marcará en tu tablero. \n"
    " - Si fallas, se marcará en tu tablero y será el turno de tu oponente.\n")
    time.sleep(3)

    print(Fore.YELLOW + "PARA SALIR DEL JUEGO, INTRODUCE 'salir'.\n" + Style.RESET_ALL)
    time.sleep(1)
   

    #print(board_enemy) #BORRAR SOLO PARA PRUEBAS*********************************

    turno = "jugador"


    while True:

        if turno == "jugador":
            
            # Jugada del jugador
            usuario_fila = input("Adivina la fila (debe estar entre 1 y 10, o escribe 'salir' para salir del juego): ")
        
            if usuario_fila.lower() == "salir":
                print(Fore.YELLOW + "Gracias por jugar. ¡Hasta la próxima!")
                break
        
            usuario_fila = int(usuario_fila)
            usuario_colum = int(input("Adivina la columna (debe estar entre 1 y 10): "))
            

            # Verificar si el jugador señala el tablero. 
            if usuario_fila > size or \
                    usuario_colum > size:
                    print("¡Oops!, ¡esa no es una ubicación en el tablero!")
                    continue
            
            #Jugador acierta el disparo
            elif board_enemy[usuario_fila,usuario_colum] == boat:
                board_enemy[usuario_fila,usuario_colum] = boat_damaged
                board_blank[usuario_fila][usuario_colum] = boat_damaged
                # print(pd.DataFrame(board_enemy)) 
                print(Fore.GREEN + "¡Felicidades! ¡tocaste mi barco!" + Style.RESET_ALL)
                sonido_explosion.play()
                Jugador=pd.DataFrame(board_own)
                Maquina=pd.DataFrame(board_blank) 
                espacio=pd.DataFrame(np.full((10,1),"|"))
                resultado=pd.concat([Jugador,espacio,Maquina],axis=1)
                print(resultado)

                continue

            elif boat not in board_enemy:
                print("Felicidades, ¡has ganado!")
                break

                
            else:
                # Verificar si la jugada es válida
                if board_enemy[usuario_fila][usuario_colum] == miss or\
                    board_enemy[usuario_fila][usuario_colum] == boat_damaged: 
                    print(Fore.YELLOW + "Ya intentaste esa ubicación." + Style.RESET_ALL)
                else:
                    # Actualizar el tablero y marcar la jugada como intentada
                    print(Fore.RED + "¡Fallaste!" + Style.RESET_ALL)
                    board_enemy[usuario_fila][usuario_colum] = miss
                    board_blank[usuario_fila][usuario_colum] = miss
                    turno = "maquina"

        if turno == "maquina":


            # Jugada de la computadora
            comp_fila = np.random.randint(0,size)
            comp_colum = np.random.randint(0,size)

            # Verificar si la maquina ha acertado. 
            if board_own[comp_fila,comp_colum] == boat:
                print(Fore.RED + "¡La maquina tocó tu barco!" + Style.RESET_ALL) 
                sonido_explosion.play()
                board_own[comp_fila][comp_colum] = boat_damaged 
                Jugador=pd.DataFrame(board_own)
                Maquina=pd.DataFrame(board_blank) 
                espacio=pd.DataFrame(np.full((10,1),"|"))
                resultado=pd.concat([Jugador,espacio,Maquina],axis=1)
                print(resultado)
                continue
            else:
                # Verificar si ya se había intentado esa ubicación.
                if board_own[comp_fila][comp_colum] == miss: 
                    print("La maquina ya intentó esa ubicación.")
                elif boat not in board_own:
                    print("Perdiste")
                else:
                    # Actualizar el tablero y marcar la jugada como intentada. 
                    print(Fore.GREEN + "La maquina falló." + Style.RESET_ALL)
                    board_own[comp_fila][comp_colum] = miss
                    turno = "jugador"
                    
            # Imprimir el tablero actualizado. 
            Jugador=pd.DataFrame(board_own)
            Maquina=pd.DataFrame(board_blank) 
            espacio=pd.DataFrame(np.full((10,1),"|"))
            resultado=pd.concat([Jugador,espacio,Maquina],axis=1)
            print(resultado)
