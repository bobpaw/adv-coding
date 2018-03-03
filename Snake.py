##
## A basic version of the snake game
## Run in Python 3 with Pygame
## Author: Jason Kolbly <jason@rscheme.org>
##

import pygame
from random import randint

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

tile_size = 20
total_tiles = 30
delay = 100

pellet = [randint(0,total_tiles-1),randint(0,total_tiles-1)]
events = []

pygame.init()
size = (tile_size*total_tiles, tile_size*total_tiles)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snek")

playing = True

class player():
    def __init__(self, x, y, x_vel=1, y_vel=0):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.length = 1
        self.history = []
    def move(self, new_x, new_y):
        global pellet
        global playing
        global delay
        
        self.history.append([self.x,self.y])
        if [new_x,new_y] in self.history:
            playing = False
            return False
        else:
            if new_x >= 0 and new_x < total_tiles:
                self.x = new_x
            elif new_x < 0:
                self.x = total_tiles-1
            else:
                self.x = 0
            if new_y >= 0 and new_y < total_tiles:
                self.y = new_y
            elif new_y < 0:
                self.y = total_tiles-1
            else:
                self.y = 0
        if (self.x == pellet[0] and self.y == pellet[1]) or pellet in self.history:
            self.length += 1
            pellet = [randint(0,total_tiles-1),randint(0,total_tiles-1)]
            if delay > 20:
                delay -= 2
        while len(self.history) > self.length:
            self.history.pop(0)

player = player(10,10)

def draw():
    screen.fill(black)
    pygame.draw.rect(screen, red, [pellet[0]*tile_size, pellet[1]*tile_size, tile_size, tile_size])
    pygame.draw.rect(screen, green, [player.x*tile_size, player.y*tile_size, tile_size, tile_size])
    for location in player.history:
        pygame.draw.rect(screen, blue, [location[0]*tile_size, location[1]*tile_size, tile_size, tile_size])
        
    for x in range(total_tiles):
        pygame.draw.line(screen, white, [x*tile_size, 0], [x*tile_size, tile_size*total_tiles])
        pygame.draw.line(screen, white, [0, x*tile_size], [total_tiles*tile_size, x*tile_size])
    pygame.display.update()

def test_event(event_list):
    for e in events:
        if e.type in event_list and e.type != pygame.KEYDOWN:
            return True
        elif e.type == pygame.KEYDOWN:
            if e.key in event_list:
                return True
    return False

while playing:
    events = []
    for event in pygame.event.get():
        events.append(event)
    if test_event([pygame.QUIT,pygame.K_q]):
        pygame.quit()
        quit()
    if test_event([pygame.K_w,pygame.K_UP]) and player.y_vel == 0:
        player.x_vel = 0
        player.y_vel = -1
    elif test_event([pygame.K_d,pygame.K_RIGHT]) and player.x_vel == 0:
        player.x_vel = 1
        player.y_vel = 0
    elif test_event([pygame.K_s,pygame.K_DOWN]) and player.y_vel == 0:
        player.x_vel = 0
        player.y_vel = 1
    elif test_event([pygame.K_a,pygame.K_LEFT]) and player.x_vel == 0:
        player.x_vel = -1
        player.y_vel = 0
    player.move(player.x+player.x_vel,player.y+player.y_vel)
    draw()
    pygame.time.wait(int(delay))
pygame.quit()
print ("You got a score of: " + str(player.length-1))
pygame.time.wait(3000)
quit()
