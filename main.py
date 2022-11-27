from random import choice
import pygame
from pygame.draw import *
from random import randint
from pygame.font import *
from shell import *

FPS = 10

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = 0xFFFFFF
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 800

FIELD_WIDTH = 1200//20
FIELD_HEIGHT = 800//20

directions = ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))

GENOME_SIZE = 16
CELLS_NUMBER = 16

mutation_num = [0 for x in range(CELLS_NUMBER)]

pygame.font.init()
f = Font(None, 16)
f1 = Font(None, 24)

parser = Parser()
namespace = parser.parse_args(sys.argv[1:])
if namespace.genome_size:
    genome_size = int(namespace.genome_size[0])
else: 
    genome_size = 16   

class Bacteria:
    def __init__(self, x, y, genome=0):
        '''
        self.x - коррдината бактерии по x (1 - (FIELD_WIDTH - 1))
        self.y - коррдината бактерии по x (1 - (FIELD_HEIGHT-1))
        self.health - здоровье, тратится при перемещении
        self.genome - геном бактерии, массив из 128 чисел от 0 до 128, команды;
        0-63 - перемещение (остаток от деления на 8, 0 - в левый верхний угол, далее по часовой стрелке)
        64-127 - съесть еду из клетки в соответствующей клетке (остаток от деления на 8, 0 - левый верхний угол, далее по часовой стрелке)
        '''
        self.x = x
        self.y = y
        self.health = 16
        self.genome = [randint(0, GENOME_SIZE - 1) for i in range(GENOME_SIZE)]
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
        self.genome[randint(0, GENOME_SIZE - 1)] = randint(0, GENOME_SIZE - 1)
        
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
screen = pygame.display.set_mode((WIDTH + 250, HEIGHT))
screen.fill(WHITE)
bacteria = []
cells = [[Cell(x, y) for y in range(FIELD_HEIGHT)] for x in range(FIELD_WIDTH)]

clock = pygame.time.Clock()
finished = False
for i in range(CELLS_NUMBER):
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
        if bac.genome[time % GENOME_SIZE] < GENOME_SIZE // 2:
            bac.move(bac.genome[time % GENOME_SIZE] % 8)
        else:
            bac.eat_and_suffer((bac.genome[time % GENOME_SIZE] - GENOME_SIZE // 2) % 8)
    for i in range(20, 1220, 20):
        line(screen, BLACK, (i, 0), (i, 800))
    for i in range(20, 800, 20):
        line(screen, BLACK, (0, i), (1200, i))     
    for i in range(len(bacteria)):
        if bacteria[i].is_dead():
            bacteria[i].mutate()
            bacteria[i].health = 16
            mutation_num[i] += 1
    text_time = f1.render('time = ' + str(time), True, BLACK) 
    text_K_UP = f1.render('SPEED UP - ЛКМ', True, BLACK)
    text_K_DOWN = f1.render('SPEED DOWN - ПКМ', True, BLACK)
    screen.blit(text_time, (WIDTH + 10, 10))
    screen.blit(text_K_UP, (WIDTH + 10, 40))
    screen.blit(text_K_DOWN, (WIDTH + 10, 70))
        
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #  левая кнопка мыши
                FPS *= 2
            if event.button == 3:  # правая кнопка мыши
                FPS = FPS // 2        
        elif event.type == pygame.MOUSEBUTTONUP:
            None
        elif event.type == pygame.MOUSEMOTION:
            None
    time += 1
    if time % 10 == 0:
        print('mutations: ', mutation_num)
    if time % 100 == 0:
        print('best genome: ', bacteria[mutation_num.index(min(mutation_num))].genome)
    
pygame.quit()
