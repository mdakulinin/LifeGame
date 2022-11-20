from random import choice
import pygame
from pygame.draw import *
from random import randint
from pygame.font import *

import sys 
  
  
# initializing the constructor 
pygame.init() 
   
res = (1400,800) 
screen = pygame.display.set_mode(res) 
   
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
width = screen.get_width() 
height = screen.get_height() 
  
smallfont = pygame.font.SysFont('Corbel',70)
font = pygame.font.SysFont('Corbel',150)
  
start = smallfont.render('Start', True , color)
rules = smallfont.render('Rules', True , color)
quit = smallfont.render('Quit', True , color)
text = smallfont.render('haha bt', True, (0, 0, 0))
title = font.render('Game of Life', True, color)  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
               
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-182 <= mouse[0] <= width/2+182 and height/2-70 <= mouse[1] <= height/2+15:  
                break;
            elif width/2-182 <= mouse[0] <= width/2+182 and height/2+150 <= mouse[1] <= height/2+235:
                pygame.quit()
            elif width/2-182 <= mouse[0] <= width/2+182 and height/2+40 <= mouse[1] <= height/2+125:
                while True: 
                    screen.fill((255, 255, 255))
                    screen.blit(text,(20, 8))
                    pygame.display.update() 
                            
    screen.fill((255, 255, 255)) 
      
    mouse = pygame.mouse.get_pos() 
      
    pygame.draw.rect(screen,color_dark,[width/2-182,height/2-70,364,85])
    pygame.draw.rect(screen,color_dark,[width/2-182,height/2+150,364,85])
    pygame.draw.rect(screen,color_dark,[width/2-182,height/2+40,364,85])
    pygame.draw.rect(screen,color_dark,[width/2-600,height/2-350,1200,170])
    
    if width/2-182 <= mouse[0] <= width/2+182 and height/2-70 <= mouse[1] <= height/2+15: 
        pygame.draw.rect(screen,color_light,[width/2-182,height/2-70,364,85]) 
    elif width/2-182 <= mouse[0] <= width/2+182 and height/2+40 <= mouse[1] <= height/2+125:
        pygame.draw.rect(screen,color_light,[width/2-182,height/2+40,364,85])
    elif width/2-182 <= mouse[0] <= width/2+182 and height/2+150 <= mouse[1] <= height/2+235:
        pygame.draw.rect(screen,color_light,[width/2-182,height/2+150,364,85])

    screen.blit(start,(width/2-70,height/2 -60))
    screen.blit(rules,(width/2-74,height/2+ 50))
    screen.blit(quit,(width/2-68,height/2+ 160))
    screen.blit(title,(width/2-400,height/2 - 330))
      
    pygame.display.update() 