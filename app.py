import pygame
import random

######################################
#                                    #
#                Snake               #
#                                    #
######################################

class Snake:
    def __init__(self, x, y):
        self.body = [[x, y], [x - 10, y], [x - 20, y]]
        self.direction = "RIGHT"
        self.new_direction = "RIGHT"
        self.color = (0, 255, 0)
        
    def update(self):
        if self.new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif self.new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif self.new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif self.new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

        if self.direction == "RIGHT":
            self.body.insert(0, [self.body[0][0] + 10, self.body[0][1]])
        elif self.direction == "LEFT":
            self.body.insert(0, [self.body[0][0] - 10, self.body[0][1]])
        elif self.direction == "UP":
            self.body.insert(0, [self.body[0][0], self.body[0][1] - 10])
        elif self.direction == "DOWN":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + 10])
        self.body.pop()
        
    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(
                block[0], block[1], 10, 10))
    
    def is_collision(self):
        if self.body[0][0] < 0 or self.body[0][0] > 390:
            return True
        elif self.body[0][1] < 0 or self.body[0][1] > 390:
            return True
        elif any(self.body[0] == block for block in self.body[1:]):
            return True
        elif self.body[0] in [obstacle.pos for obstacle in obstacles]:
            return True
        else:
            return False

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

######################################
#                                    #
#         Foods / Obstacles          #
#                                    #
######################################

class Food:
    def __init__(self):
        self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        self.color = (255, 0, 0)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.pos[0], self.pos[1], 10, 10))

    def move(self):
        self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        while self.pos in taken_pos:
            self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        
class Obstacle:
    def __init__(self):
        self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        while self.pos in taken_pos:
            self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        self.color = (0, 0, 0)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.pos[0], self.pos[1], 10, 10))

######################################
#                                    #
#            Bonus / Malus           #
#                                    #
######################################

class Bonus1:
    def __init__(self):
        self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        while self.pos in taken_pos:
            self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        self.color = (255,20,147)
        self.lifespan = 100
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.pos[0], self.pos[1], 10, 10))
        
    def activate(self):
        global speed
        if speed > 10:
            speed -= 5

class Bonus2:
    def __init__(self):
        self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        while self.pos in taken_pos:
            self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        self.color = (255,215,0)
        self.lifespan = 150
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.pos[0], self.pos[1], 10, 10))
        
    def activate(self):
        global life
        life += 1

class Malus1:
    def __init__(self):
        self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        while self.pos in taken_pos:
            self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        self.color = (162,164,21)
        self.lifespan = 400
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.pos[0], self.pos[1], 10, 10))
        
    def activate(self):
        global speed
        speed += 5

class Malus2:
    def __init__(self):
        self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        while self.pos in taken_pos:
            self.pos = [random.randrange(1, 40) * 10, random.randrange(1, 40) * 10]
        self.color = (25,25,112)
        self.lifespan = 400
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.pos[0], self.pos[1], 10, 10))
        
    def activate(self):
        for i in range(5):
            obstacles.append(Obstacle())

######################################
#                                    #
#         Starting the Game          #
#                                    #
######################################

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake")

snake = Snake(100, 50)
life = 1
food = Food()
obstacles = []
modifiers = []
taken_pos = []

clock = pygame.time.Clock()
speed = 10

score = 0
font = pygame.font.SysFont('arial', 20)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.new_direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                snake.new_direction = "LEFT"
            elif event.key == pygame.K_UP:
                snake.new_direction = "UP"
            elif event.key == pygame.K_DOWN:
                snake.new_direction = "DOWN"

    snake.update()

    if snake.body[0] == food.pos:
        food.move()
        snake.grow()
        obstacles.append(Obstacle())
        score += 10
        speed += 2.5

    for modifier in modifiers:
        if modifier.pos == snake.body[0]:
            modifier.activate()
            modifiers.remove(modifier)
            break

    if random.randint(1,500) == 1:
        modifiers.append(Bonus1())
    if random.randint(1,3000) == 1:
        modifiers.append(Bonus2())
    if random.randint(1,250) == 1:
        modifiers.append(Malus1())
    if random.randint(1,150) == 1:
        modifiers.append(Malus2())
    
    for modifier in modifiers:
        modifier.lifespan -= 1
        if modifier.lifespan == 0:
            modifiers.remove(modifier)

    # Compute taken_pos
    taken_pos.append(food.pos)
    taken_pos.append([obstacle.pos for obstacle in obstacles])
    taken_pos.append(snake.body)

    # Vérifie si le serpent a touché les bords de l'écran ou s'est mordu la queue
    if snake.is_collision():
        life -= 1
        if life == 0:
            pygame.quit()
            quit()

    # Efface l'écran avec la couleur de fond
    screen.fill((255,255,255))

    # Affiche le serpent et la nourriture
    snake.draw(screen)
    food.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)
    for modifier in modifiers:
        modifier.draw(screen)

    # Ajoute le score à l'écran
    font = pygame.font.SysFont('arial', 20)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Met à jour l'affichage
    pygame.display.flip()

    # Pause le jeu pour contrôler sa vitesse
    clock.tick(speed)
