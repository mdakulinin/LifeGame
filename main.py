from random import choice
import pygame
from pygame.draw import *
from random import randint

FPS = 10

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = 0xFFFFFF

WIDTH = 1200
HEIGHT = 800

FIELD_WIDTH = 1200//20
FIELD_HEIGHT = 800//20

class Bacteria:
    def __init__(self, x, y, cell_type):
        self.x = x
        self.y = y
        self.cell_type = cell_type
        self.health = 100
        #self.genome 
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
            self.x -= 1
    
    def draw(self, screen):
        rect(screen, RED, (self.x * 20 + 1, self.y * 20 + 1, 19, 19))
            
    def neighbours(self):
        None
    
    def eat_food(self):
        None
        
    def eat_cell(self):
        None
    
    def mutate(self):
        None
    
    def reproduce(self):
        None
        
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
        self.amount_of_food = randint(0, 10)
            

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
bacteria = []

clock = pygame.time.Clock()
finished = False
for i in range(10):
    bacteria.append(Bacteria(randint(1, 59), randint(1, 40), "photo"))
while not finished:
    screen.fill(WHITE)
    for bac in bacteria:
        bac.move(randint(0, 7))
        bac.draw(screen)    
    for i in range(20, 1200, 20):
        line(screen, BLACK, (i, 0), (i, 800))
    for i in range(20, 800, 20):
        line(screen, BLACK, (0, i), (1200, i))    
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
pygame.quit()
