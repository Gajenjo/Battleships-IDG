import pandas as pd
import numpy as np


def own_board (size,boat1=4,boat2=3,boat3=2,boat4=1,boat="\u26F4"):
    '''
    Función que dado un tamaño N
    devuelve la visual de un tablero (Pandas Dataframe)
    con X barcos de Y tipo

    Los barcos por defecto son:
    - 4 barcos de tamaño 1
    - 3 barcos de tamaño 2
    - 2 barcos de tamaño 3
    - 1 barco de tamaño 4

    El barco por defecto es "\u26F4"
    '''
    nboard = size
    board = np.full((nboard,nboard)," ")
    n_boats1 = 0
    n_boats2 = 0
    n_boats3 = 0
    n_boats4 = 0
    while True:
        barco = boat
        rng1 = np.random.randint(0, nboard)
        rng2 = np.random.randint(0, nboard)
        orientation = np.random.randint(1,3)
        if orientation == 1:
            barco_2 = np.full((1, 2),barco)
            barco_3 = np.full((1, 3),barco)
            barco_4 = np.full((1, 4),barco)
            size_until_border = board[rng1:rng1+1, rng2-1:-1]
            while (board[rng1,rng2] != barco)&(n_boats1<boat1):
                board[rng1,rng2]=barco
                n_boats1+=1
            while (board[rng1,rng2] != barco) & (len(barco_2[0])<=len(size_until_border[0])) & (barco not in size_until_border)&(n_boats2<boat2):
                board[rng1:rng1+1, rng2:len(barco_2[0])+rng2]= barco_2
                n_boats2+=1         
            while (board[rng1,rng2] != barco) & (len(barco_3[0])<=len(size_until_border[0])) & (barco not in size_until_border)&(n_boats3<boat3):
                board[rng1:rng1+1, rng2:len(barco_3[0])+rng2]= barco_3
                n_boats3+=1
            while (board[rng1,rng2] != barco) & (len(barco_4[0])<=len(size_until_border[0])) & (barco not in size_until_border)&(n_boats4<boat4):
                board[rng1:rng1+1, rng2:len(barco_4[0])+rng2]= barco_4
                n_boats4+=1
        elif orientation == 2:
            barco_2 = np.full((2, 1),barco)
            barco_3 = np.full((3, 1),barco)
            barco_4 = np.full((4, 1),barco)
            size_until_border = board[rng1-1:-1, rng2:rng2+1]
            while (board[rng1,rng2] != barco)&(n_boats1<boat1):
                board[rng1,rng2]=barco
                n_boats1+=1
            while (board[rng1,rng2] != barco) & (len(barco_2)<=len(size_until_border)) & (barco not in size_until_border)&(n_boats2<boat2):
                    board[rng1:rng1+len(barco_2), rng2:rng2+1]= barco_2
                    n_boats2+=1         
            while (board[rng1,rng2] != barco) & (len(barco_3)<=len(size_until_border)) & (barco not in size_until_border)&(n_boats3<boat3):
                board[rng1:rng1+len(barco_3), rng2:rng2+1]= barco_3
                n_boats3+=1
            while (board[rng1,rng2] != barco) & (len(barco_4)<=len(size_until_border)) & (barco not in size_until_border)&(n_boats4<boat4):
                board[rng1:rng1+len(barco_4), rng2:rng2+1]= barco_4
                n_boats4+=1

        if (n_boats1 == boat1)&(n_boats2 == boat2)&(n_boats3 == boat3)&(n_boats4 == boat4):
            break
    return (print(pd.DataFrame(board)))

def enemy_board(size,boat1=4,boat2=3,boat3=2,boat4=1,boat="\u26F4"):
    '''
    Función hermana de own_board

    Función que dado un tamaño n
    devuelve un tablero (Pandas Dataframe) SIN VISUAL
    con X barcos de Y tipo

    Los barcos por defecto son:
    - 4 barcos de tamaño 1
    - 3 barcos de tamaño 2
    - 2 barcos de tamaño 3
    - 1 barco de tamaño 4

    El barco por defecto es "\u26F4"
    '''
    nboard = size
    board = np.full((nboard,nboard)," ")
    n_boats1 = 0
    n_boats2 = 0
    n_boats3 = 0
    n_boats4 = 0
    while True:
        barco = "\u26F4"
        rng1 = np.random.randint(0, nboard)
        rng2 = np.random.randint(0, nboard)
        orientation = np.random.randint(1,3)
        if orientation == 1:
            barco_2 = np.full((1, 2),barco)
            barco_3 = np.full((1, 3),barco)
            barco_4 = np.full((1, 4),barco)
            size_until_border = board[rng1:rng1+1, rng2-1:-1]
            while (board[rng1,rng2] != barco)&(n_boats1<boat1):
                board[rng1,rng2]=barco
                n_boats1+=1
            while (board[rng1,rng2] != barco) & (len(barco_2[0])<=len(size_until_border[0])) & (barco not in size_until_border)&(n_boats2<boat2):
                board[rng1:rng1+1, rng2:len(barco_2[0])+rng2]= barco_2
                n_boats2+=1         
            while (board[rng1,rng2] != barco) & (len(barco_3[0])<=len(size_until_border[0])) & (barco not in size_until_border)&(n_boats3<boat3):
                board[rng1:rng1+1, rng2:len(barco_3[0])+rng2]= barco_3
                n_boats3+=1
            while (board[rng1,rng2] != barco) & (len(barco_4[0])<=len(size_until_border[0])) & (barco not in size_until_border)&(n_boats4<boat4):
                board[rng1:rng1+1, rng2:len(barco_4[0])+rng2]= barco_4
                n_boats4+=1
        elif orientation == 2:
            barco_2 = np.full((2, 1),barco)
            barco_3 = np.full((3, 1),barco)
            barco_4 = np.full((4, 1),barco)
            size_until_border = board[rng1-1:-1, rng2:rng2+1]
            while (board[rng1,rng2] != barco)&(n_boats1<boat1):
                board[rng1,rng2]=barco
                n_boats1+=1
            while (board[rng1,rng2] != barco) & (len(barco_2)<=len(size_until_border)) & (barco not in size_until_border)&(n_boats2<boat2):
                    board[rng1:rng1+len(barco_2), rng2:rng2+1]= barco_2
                    n_boats2+=1         
            while (board[rng1,rng2] != barco) & (len(barco_3)<=len(size_until_border)) & (barco not in size_until_border)&(n_boats3<boat3):
                board[rng1:rng1+len(barco_3), rng2:rng2+1]= barco_3
                n_boats3+=1
            while (board[rng1,rng2] != barco) & (len(barco_4)<=len(size_until_border)) & (barco not in size_until_border)&(n_boats4<boat4):
                board[rng1:rng1+len(barco_4), rng2:rng2+1]= barco_4
                n_boats4+=1

        if (n_boats1 == boat1)&(n_boats2 == boat2)&(n_boats3 == boat3)&(n_boats4 == boat4):
            break
    return board