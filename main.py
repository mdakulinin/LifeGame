from random import choice
import pygame
from pygame.draw import *
from random import randint
from pygame.font import *

FPS = 1

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 800

FIELD_WIDTH = 1200//20
FIELD_HEIGHT = 800//20

directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

mutation_num = [0 for x in range(16)]

pygame.font.init()
f = Font(None, 16)

class Bacteria:
    def __init__(self, x, y, genome=0):
        '''
        self.x - коррдината бактерии по x (1 - (FIELD_WIDTH - 1))
        self.y - коррдината бактерии по x (1 - (FIELD_HEIGHT-1))
        self.health - здоровье, тратится при перемещении
        self.genome - геном бактерии, массив из 16 чисел от 0 до 15;
        0-63 - перемещение (0 - в левый верхний угол, далее по часовой стрелке)
        64-127 - съесть еду из клетки в соответствующей клетке (0 - левый верхний угол, далее по часовой стрелке)
        '''
        self.x = x
        self.y = y
        self.health = 128
        self.genome = [randint(0, 127) for i in range(128)]
        self.text = f.render(str(self.health), True, WHITE)
        #self.patterns = patterns
    
    def move(self, direction):
        if direction == 0 and self.x != 0 and self.y != 0:
            self.x += -1
            self.y += -1
        elif direction == 1 and self.y != 0:
            self.y += -1
        elif direction == 2 and self.y != 0 and self.x != FIELD_WIDTH - 1:
            self.x += 1
            self.y += -1
        elif direction == 3 and self.x != FIELD_WIDTH - 1:
            self.x += 1
        elif direction == 4 and self.x != FIELD_WIDTH - 1 and self.y != FIELD_HEIGHT - 1:
            self.x += 1
            self.y += 1
        elif direction == 5 and self.y != FIELD_HEIGHT - 1:
            self.y += 1
        elif direction == 6 and self.x != 0 and self.y != FIELD_HEIGHT - 1:
            self.x += -1
            self.y += 1
        elif direction == 7 and self.x != 0:
            self.x += -1
        self.health -= 1
        self.text = f.render(str(self.health), True, WHITE)
    
    def draw(self, screen):
        rect(screen, BLUE, (self.x * 20 + 1, self.y * 20 + 1, 19, 19))
        screen.blit(self.text, (self.x * 20, self.y * 20))
    
    def eat_and_suffer(self, n):
        if cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].amount_of_food == 1:
            self.health += 1
            self.text = f.render(str(self.health), True, WHITE)
            #cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].amount_of_food = 0
        elif cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].is_poison == 1:
            self.health += -1
            self.text = f.render(str(self.health), True, WHITE)
            #cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].is_poison = 0
    
    def mutate(self):
        self.genome[randint(0, 127)] = randint(0, 127)
        
    def is_dead(self):
        if self.health <= 0:
            return True
        return False
        
        
class Cell:
    '''
    Клетка поля.
    Имеет аттрибуты:
    x, y - координаты;
    amount_of_food - количество еды на клетке.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.amount_of_food = randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1)
        if self.amount_of_food == 0:
            self.is_poison = randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1)
        else:
            self.is_poison = 0
    
    def draw(self, screen):
        if self.amount_of_food:
            rect(screen, GREEN, (self.x * 20 + 1, self.y * 20 + 1, 19, 19))
        elif self.is_poison:
            rect(screen, RED, (self.x * 20 + 1, self.y * 20 + 1, 19, 19))
            

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
bacteria = []
cells = [[Cell(x, y) for y in range(FIELD_HEIGHT)] for x in range(FIELD_WIDTH)]

clock = pygame.time.Clock()
finished = False
for i in range(16):
    bacteria.append(Bacteria(randint(1, FIELD_WIDTH - 1), randint(1, FIELD_HEIGHT - 1)))
time = 0
while not finished:
    screen.fill(WHITE)
    for cell_list in cells:
        for cell in cell_list:
            cell.draw(screen)
    for bac in bacteria:
        if not bac.is_dead():
            bac.draw(screen)
        if bac.genome[time % 128] < 64:
            bac.move(bac.genome[time % 128] % 8)
        else:
            bac.eat_and_suffer((bac.genome[time % 128] - 64) % 8)
    for i in range(20, 1200, 20):
        line(screen, BLACK, (i, 0), (i, 800))
    for i in range(20, 800, 20):
        line(screen, BLACK, (0, i), (1200, i))     
    for i in range(len(bacteria)):
        if bacteria[i].is_dead():
            bacteria[i].mutate()
            bacteria[i].health = 50
            mutation_num[i] += 1
            
        
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            None
        elif event.type == pygame.MOUSEBUTTONUP:
            None
        elif event.type == pygame.MOUSEMOTION:
            None
    time += 1
    if time % 1000 == 0:
        print('mutations: ', mutation_num)
    if time % 10000 == 0:
        print('best genome: ', bacteria[mutation_num.index(min(mutation_num))].genome)
pygame.quit()
