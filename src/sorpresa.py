import numpy as np
import pygame 
import time
from pygame import mixer

# import board
import board_2

# Sound Effect from <a href="https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=39536">Pixabay</a>

# Init game and boards size
pygame.display.init()
mixer.init()
window_size=(800,600)
screen = pygame.display.set_mode(size=window_size)

# Load images
new_size = 350
background=pygame.image.load("Ultimate Battleship\-BS-_Hero_Image_-_Desktop.jpg")
background= pygame.transform.scale(background,window_size)
logo=pygame.image.load("Ultimate Battleship\\battleship-hero-logo.jpg")
logo=pygame.transform.scale(logo,(600,90))
boat=pygame.image.load("Ultimate Battleship\\3117907.png")
boat=pygame.transform.scale(boat,(new_size/10,new_size/10))
explosion=pygame.image.load("Ultimate Battleship\explosion.png")
explosion=pygame.transform.scale(explosion,(new_size/10,new_size/10))

# Init boards
board_array = board_2.own_board() # tablero creado a partir de un array
board_enemy_array= board_2.blank_board() # tablero creado a partir de un array
board_enemy_array_true= board_2.enemy_board() # tablero creado a partir de un array
board_surface = pygame.surfarray.make_surface(board_array)
board_surface = pygame.transform.scale(board_surface,(new_size,new_size)) # Reescalado del tablero para poder trabajar con él
board_surface_2=pygame.surfarray.make_surface(board_enemy_array)
board_surface_2 = pygame.transform.scale(board_surface_2,(new_size,new_size))
board_surface_enemy=pygame.surfarray.make_surface(board_enemy_array_true)
board_surface_enemy = pygame.transform.scale(board_surface_enemy,(new_size,new_size))
board_size = board_surface.get_size()
board_size_2 = board_surface_2.get_size()
board_size_3 = board_surface_enemy.get_size()
board_pos = (25, 100)  # posición del tablero en la ventana
board_pos_2 = (board_pos[0]+board_size[0]+50,board_pos[1])
board_pos_3 = board_pos_2
border_color = (0, 0, 0) # color del borde
border_rect_1=pygame.Rect(board_pos[0]-1,board_pos[1]-1,board_size[0]+2,board_size[1]+2) # Creacion borde tablero
border_rect_2=pygame.Rect(board_pos_2[0]-1,board_pos_2[1]-1,board_size_2[0]+2,board_size_2[1]+2)
screen.blit(background,(0,0)) # Fondo imagen
screen.blit(logo,(100,5)) # Fondo logo
pygame.draw.rect(screen,border_color,border_rect_1) # Borde tablero en pantalla
pygame.draw.rect(screen,border_color,border_rect_2)
screen.blit(board_surface,board_pos) # primer tablero en pantalla
screen.blit(board_surface_2,board_pos_2) # segundo tablero en pantalla

# game colours
bg_color = (33, 176, 243)  # color de fondo del tablero
ship_color = (32, 176, 243)  # color de las celdas que contienen barcos
miss_color = (66, 136, 168)  # color de las celdas sin barcos y ya disparadas
hit_color = (155, 0, 0)  # color de las celdas con barcos y ya disparadas
cell_size = new_size/10  # tamaño de cada celda del tablero manteniendo la coherencia


# Own board blit
for i in range(board_array.shape[0]):
    for j in range(board_array.shape[1]):
        rect = pygame.Rect(board_pos[0]+i*cell_size, board_pos[1]+j*cell_size, cell_size, cell_size)
        if board_array[i, j] == 0:
            pygame.draw.rect(screen, bg_color, rect)
        elif board_array[i, j] == 1:
            pygame.draw.rect(screen, ship_color, rect)
            screen.blit(boat,(rect[0],rect[1]))

# Enemy board blit
for i in range(board_enemy_array_true.shape[0]):
    for j in range(board_enemy_array_true.shape[1]):
        rect = pygame.Rect(board_pos_3[0]+i*cell_size, board_pos_3[1]+j*cell_size, cell_size, cell_size)
        if board_enemy_array_true[i, j] == 0:
            pygame.draw.rect(screen, bg_color, rect)
        elif board_enemy_array_true[i, j] == 1:
            pygame.draw.rect(screen, ship_color, rect)

# Music and sounds load
pygame.display.flip()
music_on = pygame.display.get_active()
try_sound = "Ultimate Battleship\one_beep-99630.mp3"
miss_sound = "Ultimate Battleship\\vibrating-thud-39536.mp3"
hit_sound = "Ultimate Battleship\\retro-video-game-death-95730.mp3"
background_music= "Ultimate Battleship\Track02_BS01.mp3"

if music_on == True:
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)


turn="player_turn"

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            board_x = mouse_pos[0]
            board_y = mouse_pos[1]

            cell_x = board_x//cell_size
            cell_y = board_y//cell_size

            # Player turn
            if turn == "player_turn":
                if (425 <= board_x < 775) & (100 <= board_y < 450):
                    cell_color = screen.get_at((board_x, board_y))
                    cell_color = cell_color[:-1]
                    if cell_color == ship_color:
                        hit_s_sound = pygame.mixer.Sound(hit_sound).play().set_volume(0.1)
                        pygame.draw.rect(screen, hit_color, ((cell_x * cell_size)+5,(cell_y * cell_size)-5, cell_size, cell_size))
                        screen.blit(explosion,((cell_x * cell_size)+5,(cell_y * cell_size)-5, cell_size, cell_size))
                        pygame.display.update()

                    elif cell_color == bg_color:
                        miss_s_sound = pygame.mixer.Sound(miss_sound).play().set_volume(0.1)
                        pygame.draw.rect(screen, miss_color, ((cell_x * cell_size)+5,(cell_y * cell_size)-5, cell_size, cell_size))
                        pygame.display.update()
                        turn = "computer_turn"
                        
                        
            
            # Computer turn
            if turn == "computer_turn":
                enemy_x = np.random.randint(0,board_enemy_array_true.shape[1])
                enemy_y = np.random.randint(0,board_enemy_array_true.shape[1])
                enemy_x= int((enemy_x*cell_size)+board_pos[0])
                enemy_y= int((enemy_y*cell_size)+board_pos[1])
                pc_cell_color = screen.get_at((enemy_x+1, enemy_y+1))                
                pc_cell_color = pc_cell_color[:-1]
                if pc_cell_color == ship_color:
                    time.sleep(1)
                    hit_s_sound = pygame.mixer.Sound(hit_sound).play().set_volume(0.1)
                    pygame.draw.rect(screen, hit_color, ((enemy_x),(enemy_y), cell_size, cell_size))
                    screen.blit(explosion,((enemy_x),(enemy_y), cell_size, cell_size))
                    pygame.display.update()                    
                elif pc_cell_color == bg_color:
                    time.sleep(1)
                    miss_s_sound = pygame.mixer.Sound(miss_sound).play().set_volume(0.1)
                    pygame.draw.rect(screen, miss_color, ((enemy_x),(enemy_y), cell_size, cell_size))
                    pygame.display.update()
                    turn = "player_turn"
    # if ship_color not in screen:
    #     break