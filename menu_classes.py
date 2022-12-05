import sys 
import os
import pygame
from pygame.draw import *
from menu_functions import *

'''
класс Checkbox — класс множества квадратиков с надписями, позволяющими выбрать размер генома.
pos — позиция квадратика;
size — размер квадратика;
outline — ширина обводки;
index — порядковый номер квадратика;
'''

class Checkbox:
    def __init__ (self,  pos, size, outline, index):
        self.pos = pos
        self.size = size
        self.outline = outline
        self.index = index
        
    '''
    drawRect — нарисовать квадратик.
    drawCross — нарисовать крест в квадрате.
    Text — написать текст над квадратом.
    '''
    
    def drawRect(self, screen, height):
        rect(screen, (0,0,0), (self.pos, height+60, self.size, self.size), self.outline)
        
    def drawCross(self, screen, height):
        o = self.outline
        s = self.size
        pos = self.pos
        h = height + 60
        
        line(screen, (0,0,0), [pos + o, h + o], [pos + s - o, h + s - o], o)
        line(screen, (0,0,0), [pos + o, h + s - o], [pos + s - o, h + o], o)        
    
    def Text(self, screen, height,amount):
        f1 = round((self.size + 10)*0.8)
        f2 = round((self.size + 10)*80/133)
        h = height - 45*(f1/90) + 50
        
        numb = pygame.font.SysFont('None',f1)
        if self.index >= 7:
            numb = pygame.font.SysFont('None',f2)
            h = height - (45/1.33)*(f1/90) + 50
            
        g = numb.render(str(2**(self.index+3)), True, (0,0,0))
        
        if self.index == 0:
            screen.blit(g, (self.pos + self.size/2.8, h))
        elif self.index <= 3:
            screen.blit(g, (self.pos + self.size/5, h))
        else:    
            screen.blit(g, (self.pos, h)) 
        

        
        