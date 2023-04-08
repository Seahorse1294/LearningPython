import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.randomise()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
    
    def randomise(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(-1,0)
    
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x*cell_size)
            y_pos = int(block.y*cell_size)
            snake_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(135,16,110),snake_rect)
    
    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+ self.direction)
        self.body = body_copy[:]
    
    def add_block(self):
        body_copy = self.body[:]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        

    def update(self):
        self.snake.move()
        self.eat()
        self.check_fail()
    
    def draw(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def eat(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
    def check_fail(self):
        if self.snake.body[0].x < 0 or self.snake.body[0].x > cell_number or self.snake.body[0].y < 0 or self.snake.body[0].y > cell_number:
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()
pygame.init()

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,120)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not main_game.snake.direction == Vector2(0,1):
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and not main_game.snake.direction == Vector2(0,-1):
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT and not main_game.snake.direction == Vector2(1,0):
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT and not main_game.snake.direction == Vector2(-1,0):
                main_game.snake.direction = Vector2(1,0)

    screen.fill((50,50,50))
    main_game.draw()
    pygame.display.update()
    clock.tick(60)