from random import randint
import pygame
from pygame.draw import *
from pygame.font import *

class Bacteria:
    def __init__(self, x, y, cells, genome_size, f):
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
        self.genome_size = genome_size
        self.genome = [randint(0, genome_size - 1) for i in range(genome_size)]
        self.f = f
        self.text = f.render(str(self.health), True, (255, 255, 255))
        self.cells = cells
        #self.patterns = patterns
    
    def move(self, direction, FIELD_WIDTH, FIELD_HEIGHT):
        f = self.f
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
        self.text = f.render(str(self.health), True, (255, 255, 255))
    
    def draw(self, screen):
        rect(screen, (0, 0, 255), (self.x * 20 + 1, self.y * 20 + 1, 19, 19))
        screen.blit(self.text, (self.x * 20, self.y * 20))
    
    def eat_and_suffer(self, n, directions):
        f = self.f
        cells = self.cells
        if cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].amount_of_food == 1:
            self.health += 1
            self.text = f.render(str(self.health), True, (255, 255, 255))
            #cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].amount_of_food = 0
        elif cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].is_poison == 1:
            self.health += -1
            self.text = f.render(str(self.health), True, (255, 255, 255))
            #cells[self.x + directions[n][0] - 1][self.y + directions[n][1] - 1].is_poison = 0
    
    def mutate(self):
        genome_size = self.genome_size
        self.genome[randint(0, genome_size - 1)] = randint(0, genome_size - 1)
        
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
            rect(screen, (0, 255, 0), (self.x * 20 + 1, self.y * 20 + 1, 19, 19))
        elif self.is_poison:
            rect(screen, (255, 0, 0), (self.x * 20 + 1, self.y * 20 + 1, 19, 19))