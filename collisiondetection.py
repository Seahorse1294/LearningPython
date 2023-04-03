import pygame, sys

pygame.init()

clock = pygame.time.Clock()
screen_width, screen_height = 800,600
screen = pygame.display.set_mode((screen_width,screen_height))

moving_rect = pygame.Rect(350,250,100,100)
xspeed,yspeed = 5,4

other_rect = pygame.Rect(300,450,200,100)
other_speed = 2

def bouncing_rect():
    global xspeed, yspeed, other_speed

    moving_rect.x += xspeed
    moving_rect.y += yspeed
    other_rect.y += other_speed

    #collision with screen borders
    if moving_rect.right > screen_width and xspeed > 0:
        xspeed *= -1
    if moving_rect.left <= 0 and xspeed < 0:
        xspeed *= -1
    if moving_rect.bottom > screen_height and yspeed > 0:
        yspeed *= -1
    if moving_rect.top <= 0 and yspeed < 0:
        yspeed *= -1
    if other_rect.bottom > screen_height or other_rect.top <= 0:
        other_speed *= -1

    # collision with rect
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and yspeed > 0:
            yspeed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and yspeed < 0:
            yspeed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and xspeed < 0 :
            xspeed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance and xspeed > 0:
            xspeed *= -1

    pygame.draw.rect(screen,(255,0,0),other_rect)
    pygame.draw.rect(screen,(255,255,255),moving_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))

    bouncing_rect()

    pygame.display.flip()
    clock.tick(60)

