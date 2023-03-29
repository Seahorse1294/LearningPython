import pygame,sys

# Initialisation
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
kitten = pygame.image.load('kitten.jpg')
kitten_rect = kitten.get_rect(center=(400,300))
angle = 0


def rotate(surface,angle):
    rotated_surface = pygame.transform.rotozoom(surface,angle,0.95)
    rotated_rect = rotated_surface.get_rect(center = (400,300))
    return rotated_surface, rotated_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    angle += 5
    screen.fill((50,75,75))
    kitten_rotated, kitten_rotated_rect = rotate(kitten,angle)


    screen.blit(kitten_rotated, kitten_rotated_rect)

    pygame.display.flip()
    clock.tick(60)