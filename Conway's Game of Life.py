##
## A version of Conway's Game of Life (a cell replication game) in Pygame
## Run with python 3
## Jason Kolbly <jason@rscheme.org>
##


import time
import pygame
import math as m
import os

path = os.path.dirname(__file__)

should_it_preload = input("Do you want to load a premade object? ")
should_it_preload = should_it_preload.lower()
yes_synonyms = ["y", "yes", "sure", "okay", "fine", "affirmative", "all right", "very well", "of course", "by all means", "certainly", "absolutely", "indeed", "right", "agreed", "roger", "ok", "yeah", "yep", "yup", "okey-dokey", "yea", "aye"]
preload_boolean = False
import_boolean = False
for x in range(len(yes_synonyms)):
    if yes_synonyms[x-1] in should_it_preload:
        preload_boolean = True
if not preload_boolean:
    import_string = input("Do you want to import a file? ")
    for x in range(len(yes_synonyms)):
        if yes_synonyms[x-1] in import_string:
            import_boolean = True
    if not import_boolean:
        board_width = int(input("What should the board width be? "))
        board_height = int(input("What should the board height be? "))
        tile_size = int(input("How big is each tile? "))

board = []
board_live_counts = []

preload_options = ["glider", "glider gun", "pentomino"]
preload = ""

def save_state():
    save_name = input("What should we save it as? (Don't include an extension, it will automatically be saved with a .txt) ")
    save_name = os.path.join(path, "Life Data", save_name + ".txt")
    file = open(save_name,"w+")
    for x in range(board_height):
        file.write(str(board[x]) + "\n")
    file.close()
    print ("Game state was saved at: " + save_name)

def clear_board():
    global board
    global board_live_counts
    global board_width
    global board_height
    board = []
    board_live_counts = []
    for x in range(board_height):
        row = []
        for x in range(board_width):
            row.append(0)
        board.append(row)
        board_live_counts.append(row)

def import_file():
    global board
    global board_live_counts
    global board_width
    global board_height
    global tile_size
    
    file_name = input("What is the file name? (don't include the extension) ")
    file_name = os.path.join(path, "Life Data", file_name + ".txt")
    file = open(file_name, "r")
    lines = file.readlines()
    for x in range(len(lines)):
        lines[x].replace("[","")
        lines[x].replace("]","")
        row = lines[x].strip().split(",")
        for y in range(len(row)):
            row[y] = row[y].strip(" ")
            row[y] = row[y].strip("[")
            row[y] = row[y].strip("]")
            
            row[y] = int(row[y])
        board.append(row)
        board_live_counts.append(row)
    
##    for i in range(len(lines)):
##        print (lines[i])
##    print ("BREAK")
##    for i in range(len(board_live_counts)):
##        print (board_live_counts[i])
    file.close()

    board_height = len(board)
    for x in range(len(board)):
        board_width = len(board[x])
    tile_size = int(700/board_height)
    
    initiate()
    
def load_option():
    global preload
    global board_height
    global board_width
    global tile_size
    while not any(preload_option in preload for preload_option in preload_options):
        preload = input("What do you want to preload? It can be: " +  str(preload_options) + " ")
        preload = preload.lower()
    if "glider gun" in preload:
        board_width = 50
        board_height = 37
        tile_size = 13
        initiate()
        #clear_board()

        # Leftmost square
        board[5][1] = 1
        board[5][2] = 1
        board[6][1] = 1
        board[6][2] = 1

        # The middle 'C'
        board[3][14] = 1
        board[3][13] = 1
        board[4][12] = 1
        board[5][11] = 1
        board[6][11] = 1
        board[7][11] = 1
        board[8][12] = 1
        board[9][13] = 1
        board[9][14] = 1

        # The middle dot
        board[6][15] = 1

        # The middle arrow thingy
        board[4][16] = 1
        board[5][17] = 1
        board[6][18] = 1
        board[6][17] = 1
        board[7][17] = 1
        board[8][16] = 1

        # The thing that looks kinda like a frog
        board[5][21] = 1
        board[5][22] = 1
        board[4][21] = 1
        board[4][22] = 1
        board[3][21] = 1
        board[3][22] = 1
        board[2][23] = 1
        board[6][23] = 1
        board[6][25] = 1
        board[7][25] = 1
        board[2][25] = 1
        board[1][25] = 1

        # The right square
        board[3][35] = 1
        board[3][36] = 1
        board[4][35] = 1
        board[4][36] = 1
        
        # Leftmost square
        #board[1][5] = 1
        #board[2][5] = 1
        #board[1][6] = 1
        #board[2][6] = 1

        # The middle 'C'
        #board[14][3] = 1
        #board[13][3] = 1
        #board[12][4] = 1
        #board[11][5] = 1
        #board[11][6] = 1
        #board[11][7] = 1
        #board[12][8] = 1
        #board[13][9] = 1
        #board[14][9] = 1

        # The middle dot
        #board[15][6] = 1

        # The middle arrow thingy
        #board[16][4] = 1
        #board[17][5] = 1
        #board[18][6] = 1
        #board[17][6] = 1
        #board[17][7] = 1
        #board[16][8] = 1

        # The thing that looks kinda like a frog
        #board[21][5] = 1
        #board[22][5] = 1
        #board[21][4] = 1
        #board[22][4] = 1
        #board[21][3] = 1
        #board[22][3] = 1
        #board[23][2] = 1
        #board[23][6] = 1
        #board[25][6] = 1
        #board[25][7] = 1
        #board[25][2] = 1
        #board[25][1] = 1

        # The right square
        #board[35][3] = 1
        #board[36][3] = 1
        #board[35][4] = 1
        #board[36][4] = 1
    elif "glider" in preload:
        board_width = 20
        board_height = 20
        tile_size = 20
        initiate()
        
        board[0][1] = 1
        board[1][2] = 1
        board[2][2] = 1
        board[2][1] = 1
        board[2][0] = 1
    elif "pentomino" in preload:
        board_width = 100
        board_height = 100
        tile_size = 7
        initiate()

        board[49][49] = 1
        board[49][50] = 1
        board[50][49] = 1
        board[51][49] = 1
        board[50][48] = 1

def initiate():
    global screen
    global white
    global black
    global paused
    global board_width
    global board_height

    pygame.init()
    size = [board_width*tile_size,board_height*tile_size]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PAUSED")

    icon_name = os.path.join(path, "Life Data", "icon.png")
    #icon = pygame.image.load(icon_name)
    #pygame.display.set_icon(icon)

    paused = True

    white = (255,255,255)
    black = (0,0,0)

    if not import_boolean:
        clear_board()
    
    for x in range(board_width):
        pygame.draw.line(screen, white, [x*tile_size-tile_size, 0], [x*tile_size-tile_size, board_height*tile_size])
        
    for y in range(board_height):
        pygame.draw.line(screen, white, [0, y*tile_size-tile_size], [board_width*tile_size, y*tile_size-tile_size])


try:
    initiate()
except NameError:
    pass

if preload_boolean:
    load_option()

if import_boolean:
    import_file()

#for x in range(len(board)):
#    print (board[x])

pygame.display.flip()

def draw_background():
    global board_width
    global board_height
    screen.fill(black)
    for x in range(board_width):
        pygame.draw.line(screen, white, [x*tile_size, 0], [x*tile_size, board_height*tile_size])
    for y in range(board_height):
        pygame.draw.line(screen, white, [0, y*tile_size], [board_width*tile_size, y*tile_size])

def turn():
    global board_width
    global board_height
    for x in range(len(board)):
        board_live_counts[x] = [0] * (len(board_live_counts[x]))
    for x in range(len(board)):
        for y in range(len(board[x])):
            if x > 0:
                if board[x-1][y] == 1:
                    board_live_counts[x][y] += 1
            if x < len(board)-1:
                if board[x+1][y] == 1:
                    board_live_counts[x][y] += 1
            if y > 0:
                if board[x][y-1] == 1:
                    board_live_counts[x][y] += 1
            if y < len(board[x])-1:
                if board[x][y+1] == 1:
                    board_live_counts[x][y] += 1
            if y < len(board[x])-1 and x < len(board)-1:
                if board[x+1][y+1] == 1:
                    board_live_counts[x][y] += 1
            if y > 0 and x < len(board)-1:
                if board[x+1][y-1] == 1:
                    board_live_counts[x][y] += 1
            if y < len(board[x])-1 and x > 0:
                if board[x-1][y+1] == 1:
                    board_live_counts[x][y] += 1
            if y > 0 and x > 0:
                if board[x-1][y-1] == 1:
                    board_live_counts[x][y] += 1
        #print (board_live_counts[x])
        #print (len(board_live_counts[x]))
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 1:
                if board_live_counts[x][y] < 2:
                    board[x][y] = 0
                    #print (str(x) + "," + str(y) + " is less than 2")
                elif board_live_counts[x][y] <= 3:
                    board[x][y] = 1
                    #print (str(x) + "," + str(y) + " is less than 4")
                else:
                    board[x][y] = 0
                    #print (str(x) + "," + str(y) + " is more than 3")
            else:
                #print (str(x) + "," + str(y) + " is dead")
                if board_live_counts[x][y] == 3:
                    board[x][y] = 1
                    #print (str(x) + "," + str(y) + " is 3")
    #for x in range(100):
        #print ("")
    #for x in range(len(board)):
    #    print (board[x])
    time.sleep(0.1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused == True:
                    paused = False
                    pygame.display.set_caption("This is Conway's game of life!")
                else:
                    pygame.display.set_caption("PAUSED")
                    paused = True
            if event.key == pygame.K_s:
                save_state()
            if event.key == pygame.K_w:
                print ("w")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if mouse_position[0] > 0 and mouse_position[1] > 0 and mouse_position[0] < tile_size*board_width and mouse_position[1] < tile_size*board_height:
                pressed_location = [int(m.floor(mouse_position[0]/tile_size)),int(m.floor(mouse_position[1]/tile_size))]
                #print (str(pressed_location))
                if board[pressed_location[1]][pressed_location[0]] != 1:
                        board[pressed_location[1]][pressed_location[0]] = 1
                else:
                        board[pressed_location[1]][pressed_location[0]] = 0

    if paused == False:
        turn()
    
    draw_background()
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 1:
                pygame.draw.rect(screen, white, [y*tile_size,x*tile_size,tile_size,tile_size])    
    pygame.display.update()
    #for x in range(len(board)):
    #    print (board[x])
