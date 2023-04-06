import pygame, sys
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        # create a rectangle
        # draw the rectangle

pygame.init()

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill((50,50,50))

    pygame.display.update()
    clock.tick(60)