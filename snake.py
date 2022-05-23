import pygame, sys
import random

class SNAKE():

    def __init__(self, snake_x, snake_y, snake_size):
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.snake_size = snake_size
        self.snake_body = [[self.snake_x, self.snake_y], [self.snake_x - self.snake_size, self.snake_y], [self.snake_x - self.snake_size * 2, self.snake_y]]
        self.snake_head = [self.snake_x, self.snake_y]
        self.snake_tail = [self.snake_x - self.snake_size * 2, self.snake_y]

        self.snake_body_hor = pygame.image.load("Enter your path here/res/textures/snake_body_hor.png").convert_alpha()
        self.snake_body_ver = pygame.image.load("Enter your path here/res/textures/snake_body_ver.png").convert_alpha()
        self.snake_body_hor = pygame.transform.scale(self.snake_body_hor, (19,19))
        self.snake_body_ver = pygame.transform.scale(self.snake_body_ver, (19,19))

        self.snake_head_up = pygame.image.load("Enter your path here/res/textures/snake_head_up.png").convert_alpha()
        self.snake_head_down = pygame.image.load("Enter your path here/res/textures/snake_head_down.png").convert_alpha()
        self.snake_head_left = pygame.image.load("Enter your path here/res/textures/snake_head_left.png").convert_alpha()
        self.snake_head_right = pygame.image.load("Enter your path here/res/textures/snake_head_right.png").convert_alpha()
        self.snake_head_up = pygame.transform.scale(self.snake_head_up, (self.snake_size,self.snake_size))
        self.snake_head_down = pygame.transform.scale(self.snake_head_down, (self.snake_size,self.snake_size))
        self.snake_head_left = pygame.transform.scale(self.snake_head_left, (self.snake_size,self.snake_size))
        self.snake_head_right = pygame.transform.scale(self.snake_head_right, (self.snake_size,self.snake_size))

        self.direction = "RIGHT"
    
    def snake_extend(self):
        self.snake_body.insert(0, list(self.snake_head))

    def move_snake(self,key1, key2, key3, key4):
        self.userInput = pygame.key.get_pressed()

        if self.userInput[key1] and self.direction != "DOWN":
            self.direction = "UP"
        elif self.userInput[key2] and self.direction != "UP":
            self.direction = "DOWN"
        elif self.userInput[key3] and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif self.userInput[key4] and self.direction != "LEFT":
            self.direction = "RIGHT"
        
        if self.direction == "UP":
            self.snake_head[1] -= self.snake_size
        elif self.direction == "DOWN":
            self.snake_head[1] += self.snake_size
        elif self.direction == "LEFT":
            self.snake_head[0] -= self.snake_size
        elif self.direction == "RIGHT":
            self.snake_head[0] += self.snake_size
    
    def drawsnake(self):
        if self.direction == "UP":
            for pos in self.snake_body[1:]:
                screen.blit(self.snake_body_ver, (pos[0], pos[1]))
            
        elif self.direction == "DOWN":
            for pos in self.snake_body[1:]:
                screen.blit(self.snake_body_ver, (pos[0], pos[1]))
        
        elif self.direction == "LEFT":
            for pos in self.snake_body[1:]:
                screen.blit(self.snake_body_hor, (pos[0], pos[1]))

        elif self.direction == "RIGHT":
            for pos in self.snake_body[1:]:
                screen.blit(self.snake_body_hor, (pos[0], pos[1]))
        
        if self.direction == "UP":
            screen.blit(self.snake_head_up, (self.snake_head[0], self.snake_head[1]))
        elif self.direction == "DOWN":
            screen.blit(self.snake_head_down, (self.snake_head[0], self.snake_head[1]))
        elif self.direction == "LEFT":
            screen.blit(self.snake_head_left, (self.snake_head[0], self.snake_head[1]))
        elif self.direction == "RIGHT":
            screen.blit(self.snake_head_right, (self.snake_head[0], self.snake_head[1]))

class FRUIT:

    def __init__(self, fruit_size):
        self.fruit_size = fruit_size
        self.fruit_pos = [random.randrange(1, (width//fruit_size)) * fruit_size,
                          random.randrange(1, (height//fruit_size)) * fruit_size]
        self.fruit_spawn = True
        self.fruit_image = pygame.image.load("Enter your path here/res/textures/apple.png").convert_alpha()
        self.fruit_image = pygame.transform.scale(self.fruit_image, (fruit_size, fruit_size))

    def spawn_fruit(self):
        if not fruit.fruit_spawn:
            self.fruit_pos = [random.randrange(1, (width//self.fruit_size)) * self.fruit_size,
                            random.randrange(1, (height//self.fruit_size)) * self.fruit_size]
            self.fruit_spawn = True

    def drawfruit(self):
        screen.blit(self.fruit_image, (self.fruit_pos[0], self.fruit_pos[1]))

class SCORE:
    def __init__(self):
        self.score = 0
    
    def scoring(self):
        if snake.snake_head[0] == fruit.fruit_pos[0] and snake.snake_head[1] == fruit.fruit_pos[1]:
            self.score += 1
            fruit.fruit_spawn = False
        else:
            snake.snake_body.pop()

    def drawscore(self, score_x, score_y, color):
        self.score_text = score_font.render(f"score: {str(self.score)}", True, color)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topleft = (score_x, score_y)
        screen.blit(self.score_text, self.score_rect)

class RESET:
    def __init__(self):
        self.paused = False
    
    def game_over(self, x, y, color):

        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.paused = False
                    snake.snake_body = [[snake.snake_x, snake.snake_y], [snake.snake_x - snake.snake_size, snake.snake_y], [snake.snake_x - snake.snake_size * 2, snake.snake_y]]
                    snake.snake_head = [snake.snake_x, snake.snake_y]
                    score.score = 0
                    snake.direction = "RIGHT"
                    

            self.game_over_font = font.render("GAME OVER", True ,color)
            self.pause_score_subfont = subfont.render(f"score: {str(score.score)}", True, (255,255,255))
            self.pause_score_subfont_rect = self.pause_score_subfont.get_rect(center = (400,400))
            self.game_over_rect = self.game_over_font.get_rect()
            self.game_over_rect.center = (x, y)
            screen.blit(self.game_over_font, self.game_over_rect)
            screen.blit(self.pause_score_subfont, self.pause_score_subfont_rect)

            pygame.display.update()
    
    def kill_func(self):

        if snake.snake_head[0] >= width:
            reset.paused = True
        elif snake.snake_head[0] <= -snake.snake_size:
            reset.paused = True
        elif snake.snake_head[1] >= height:
            reset.paused = True
        elif snake.snake_head[1] <= -snake.snake_size:
            reset.paused = True

        for block in snake.snake_body[1:]:
            if snake.snake_head[0] == block[0] and snake.snake_head[1] == block[1]:
                self.paused = True


def pause():
    global paused

    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False    

        pause_font = font.render("PAUSED", True, (255,255,255))
        pause_subfont = subfont.render("Press ESCAPE to continue", True, (255,255,255))
        pause_score_subfont = subfont.render(f"score: {str(score.score)}", True, (255,255,255))
        pause_score_subfont_rect = pause_score_subfont.get_rect(center = (400,400))
        pause_subrect = pause_subfont.get_rect()
        pause_subrect.center = (400,500)
        pause_rect = pause_font.get_rect()
        pause_rect.center = (400,300)
        screen.blit(pause_font, pause_rect)
        screen.blit(pause_subfont, pause_subrect)
        screen.blit(pause_score_subfont, pause_score_subfont_rect)

        pygame.display.update()

def background_render():
    global width, height
    background = pygame.image.load("Enter your path here/res/textures/backgrund.png").convert_alpha()
    background = pygame.transform.scale(background, (width, height))
    screen.blit(background, (0,0))

               
pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake = SNAKE(400,300,20)
fruit = FRUIT(20)
score = SCORE()
reset = RESET()

paused = True

score_font = pygame.font.Font(None, 24)
font = pygame.font.Font(None, 64)
subfont = pygame.font.Font(None, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = True
                pause()
    
    background_render()
    pygame.display.set_caption("SNAKE GAME")

    snake.move_snake(   
                    pygame.K_UP, 
                    pygame.K_DOWN,
                    pygame.K_LEFT,
                    pygame.K_RIGHT
                )
    snake.snake_extend()
    score.scoring()
    fruit.spawn_fruit()
    snake.drawsnake()
    fruit.drawfruit()
    
    score.drawscore(0, 0, (255,255,255))

    reset.kill_func()
    reset.game_over(400, 300, (255,255,255))

    clock.tick(12)
    pygame.display.update()
