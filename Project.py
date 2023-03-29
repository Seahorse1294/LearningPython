import pygame, sys

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Create Display Surface
screen = pygame.display.set_mode((800,600))
second_surface = pygame.Surface([800,50])
second_surface.fill((0,100,150))
character = pygame.Surface((25,60))

kitten = pygame.image.load('kitten.jpg')
kitten_rect = kitten.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((180,100,125))
    screen.blit(kitten,kitten_rect)
    screen.blit(second_surface,(0,550))
    screen.blit(character,(200,600-60-50))
    pygame.transform.rotozoom(kitten_rect,50)
    
    pygame.display.flip()
    clock.tick(60)