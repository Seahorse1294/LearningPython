import pygame, sys

# Initiate
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

# Font
base_font = pygame.font.Font(None,72)
user_text = ''


input_rect = pygame.Rect(200,200,140,60)
colour_active = pygame.Color('lightskyblue')
colour_passive = pygame.Color('gray15')
colour = colour_passive

active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                colour = colour_active
            else:
                active = False
                colour = colour_passive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    screen.fill((0,0,150))
    pygame.draw.rect(screen,colour,input_rect,2)
    text_surface = base_font.render(user_text,True,(250,240,255))
    screen.blit(text_surface,(input_rect.left+5,input_rect.top+5))

    input_rect.w = max(text_surface.get_width()+10,150)
    pygame.display.flip()

    clock.tick(60)