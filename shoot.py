#**********************INICIO DEL JUEGO************************************************
print("¡Bienvenido a Hundir la Flota!")
print_board(board)

while True:
    # Jugada del jugador
    usuario_fila = int(input("Adivina la fila: "))
    usuario_colum = int(input("Adivina la columna: "))

    # Verificar si el jugador ha acertado
    if usuario_fila == ship_row and usuario_colum == ship_col:
        print("¡Felicidades! ¡Hundiste mi barco!")
        break
    else:
        # Verificar si la jugada es válida
        if usuario_fila not in range(5) or \
            usuario_colum not in range(5):
            print("¡Oops!, ¡esa no es una ubicación en el tablero!")
        # Verificar si ya se había intentado esa ubicación
        elif board[usuario_fila][usuario_colum] == "X":
            print("Ya intentaste esa ubicación.")
        else:
            # Actualizar el tablero y marcar la jugada como intentada
            print("¡Fallaste!")
            board[usuario_fila][usuario_colum] = "X"
        # Imprimir el tablero actualizado
        print_board(board)
    
    # Jugada de la computadora
    comp_fila = random_row(board)
    comp_colum = random_col(board)

    # Verificar si la maquina ha acertado. 
    if comp_fila == ship_row and comp_colum == ship_col:
        print("¡La maquina hundió tu barco!")
        break
    else:
        # Verificar si ya se había intentado esa ubicación.
        if board[comp_fila][comp_colum] == "X":
            print("La maquina ya intentó esa ubicación.")
        else:
            # Actualizar el tablero y marcar la jugada como intentada. 
            print("La maquina falló.")
            board[comp_fila][comp_colum] = "X"
        # Imprimir el tablero actualizado. 
        print_board(board)


