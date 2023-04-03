import pygame, sys


pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill((30,30,160))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill((50,50,50))
    screen.blit(test_surface,(300,250))
    pygame.display.update()
    clock.tick(60)