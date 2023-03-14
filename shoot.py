import board
import pandas as pd
import numpy as np
#**********************INICIO DEL JUEGO************************************************
print("¡Bienvenido a Hundir la Flota!")

while True:
    # Jugada del jugador
    usuario_fila = int(input("Adivina la fila: "))
    usuario_colum = int(input("Adivina la columna: "))

    # Verificar si el jugador ha acertado
    if tablero[usuario_fila,usuario_colum] == barco:
    # if (usuario_fila == ship_row and usuario_colum == ship_col):
        print("¡Felicidades! ¡Hundiste mi barco!")
        break
    else:
        # Verificar si la jugada es válida
        if usuario_fila not in range(tablero) or \
            usuario_colum not in range(tablero):
            print("¡Oops!, ¡esa no es una ubicación en el tablero!")
        # Verificar si ya se había intentado esa ubicación
        elif tablero[usuario_fila][usuario_colum] == Fallo: #añadir fallo or barco destruido
            print("Ya intentaste esa ubicación.")
        else:
            # Actualizar el tablero y marcar la jugada como intentada
            print("¡Fallaste!")
            tablero[usuario_fila][usuario_colum] = Fallo
        # Imprimir el tablero actualizado
        print(tablero)
    
    # Jugada de la computadora
    comp_fila = np.random.randint(0,tamaño)
    comp_colum = np.random.randint(0,tamaño)

    # Verificar si la maquina ha acertado. 
    if tablero[comp_fila,comp_colum] == barco:
        print("¡La maquina hundió tu barco!")
        break
    else:
        # Verificar si ya se había intentado esa ubicación.
        if tablero[comp_fila][comp_colum] == Fallo: #añadir fallo or barco destruido
            print("La maquina ya intentó esa ubicación.")
        else:
            # Actualizar el tablero y marcar la jugada como intentada. 
            print("La maquina falló.")
            tablero[comp_fila][comp_colum] = "X"
        # Imprimir el tablero actualizado. 
        print(tablero)


