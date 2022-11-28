import sys 
import os
import pygame
from pygame.draw import *
from random import randint
from pygame.font import *
from menu_functions import *

     
pygame.init() 
res = (1450,800) 
screen = pygame.display.set_mode(res)

width = screen.get_width() 
height = screen.get_height() 

drawMenu(screen)
