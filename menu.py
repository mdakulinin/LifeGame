from random import choice
import pygame
import os
from pygame.draw import *
from random import randint
from pygame.font import *

import sys 
     
pygame.init() 
res = (1450,800) 
screen = pygame.display.set_mode(res)


'''
во!
'''

width = screen.get_width() 
height = screen.get_height() 
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100)
black = (0, 0, 0)
  
smallfont = pygame.font.SysFont('Corbel',70)
smolfont = pygame.font.SysFont('Corbel',38)
font = pygame.font.SysFont('Corbel',150)
numb = pygame.font.SysFont('None',90)
font1 = pygame.font.SysFont('Corbel',100)

start = smallfont.render('Старт', True , color)
rules = smallfont.render('Правила', True , color)
quit = smallfont.render('Выйти', True , color)
text1 = smolfont.render('1. Синим цветом отображаются клетки, которые двигаются в', True, color)
text11 = smolfont.render('зависимости от их генома, который определяется рандомно.', True, color)
text2 = smolfont.render('2. Красным цветом отображается яд, зеленым – еда. Клетки могут либо', True, color)
text22 = smolfont.render('взаимодействовать с ними, либо нет, когда наступают на них.', True, color)
text3 = smolfont.render('3. У клеток есть здоровье, которое падает со временем, если она', True, color)
text33 = smolfont.render('отравлена или если не ела; здоровье растет, если клетка поела.', True, color)
text5 = smolfont.render('5. У клетки есть шанс мутировать, что поменяет поведение клетки.', True, color)
text55 = smolfont.render('', True, color)
text4 = smolfont.render('4. При достижении 0 здоровья клетка умирает, и на ее месте появляется', True, color)
text44 = smolfont.render('новая клетка с 50 очками здоровья.', True, color)
cross = smallfont.render('X', True, color)
cross1 = smallfont.render('X', True, color_light)
title = font.render('Game of Life', True, color)
prompt = font1.render('Выберите длину генома', True, color)
g8 = numb.render('8', True, black)
g16 = numb.render('16', True, black)
g32 = numb.render('32', True, black)
g64 = numb.render('64', True, black)
g128 = numb.render('128', True, black)

def drawMenu():
    finished = False
    while not finished:     
        for ev in pygame.event.get():                    
            if ev.type == pygame.QUIT: 
                pygame.quit() 
               
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if width/2-182 <= mouse[0] <= width/2+182 and height/2-70 <= mouse[1] <= height/2+15:  
                    genome_size = drawSelect()
                    os.system("python main.py -g " + str(genome_size))
                    finished = True
                elif width/2-182 <= mouse[0] <= width/2+182 and height/2+150 <= mouse[1] <= height/2+235:
                    pygame.display.quit()
                    pygame.quit()
                elif width/2-182 <= mouse[0] <= width/2+182 and height/2+40 <= mouse[1] <= height/2+125:
                    drawRules()
                            
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

        screen.blit(start,(width/2-80,height/2 -60))
        screen.blit(rules,(width/2-125,height/2+ 50))
        screen.blit(quit,(width/2-95,height/2+ 160))
        screen.blit(title,(width/2-400,height/2 - 330))
      
        pygame.display.update()
        
    pygame.display.quit()
    pygame.quit()

def drawRules():
    finished = False
    s = 100
    while not finished:
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 1392 <= mouse[0] <= 1433 and 9 <= mouse[1] <= 66:
                    finished = True
            
        screen.fill(color_dark)
        mouse = pygame.mouse.get_pos() 
        
        rect(screen, color, (s-5, 85, 1190, 480), 3)
        
        screen.blit(text1,(110, 100))
        screen.blit(text11,(148, 150))
        screen.blit(text2,(110, 200))
        screen.blit(text22,(149, 250))
        screen.blit(text3,(110, 300))
        screen.blit(text33,(150, 350))
        screen.blit(text4,(110, 400))
        screen.blit(text44,(150, 450))
        screen.blit(text5,(110, 500))
        screen.blit(text55,(150, 550))
        screen.blit(cross,(1395, 10))
        
        if 1392 <= mouse[0] <= 1433 and 9 <= mouse[1] <= 66:
            screen.blit(cross1,(1395, 10))

        pygame.display.update()
        
def drawSelect():
    w = width/2
    h = height/2    
    def drawRect(x, y):
        rect(screen, black, (x, y, 100, 100), 8)
    def drawCross(x, y):
        pygame.draw.line(screen, black, [x+8, y+8], [x+92, y+92], 7)
        pygame.draw.line(screen, black, [x+8, y+92], [x+92, y+8], 7)
    finished = False
    while not finished:
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if w-550 <= mouse[0] <= w-450 and h+60 <= mouse[1] <= h+160:
                    genome_size = 8
                    finished = True
                if w-300 <= mouse[0] <= w-200 and h+60 <= mouse[1] <= h+160:
                    genome_size = 16
                    finished = True
                if w-50 <= mouse[0] <= w+50 and h+60 <= mouse[1] <= h+160:
                    genome_size = 32
                    finished = True
                if w+200 <= mouse[0] <= w+300 and h+60 <= mouse[1] <= h+160:
                    genome_size = 64
                    finished = True
                if w+450 <= mouse[0] <= w+550 and h+60 <= mouse[1] <= h+160:                
                    genome_size = 128
                    finished = True
                    
        screen.fill((255, 255, 255)) 
        mouse = pygame.mouse.get_pos()          
                
        drawRect(w-550, h+60)
        drawRect(w-300, h+60)
        drawRect(w-50, h+60)
        drawRect(w+200, h+60)
        drawRect(w+450, h+60)
        
        screen.blit(g8,(w-515, h))
        screen.blit(g16,(w-286, h))
        screen.blit(g32,(w-36, h))
        screen.blit(g64,(w+218, h))
        screen.blit(g128,(w+445, h))
        
        pygame.draw.rect(screen,color_dark,[width/2-600,height/2-350,1200,170])
        screen.blit(prompt,(width/2-500,height/2 - 315))
        
        if w-550 <= mouse[0] <= w-450 and h+60 <= mouse[1] <= h+160:
            drawCross(w-550, h+60)
        if w-300 <= mouse[0] <= w-200 and h+60 <= mouse[1] <= h+160:
            drawCross(w-300, h+60)
        if w-50 <= mouse[0] <= w+50 and h+60 <= mouse[1] <= h+160:
            drawCross(w-50, h+60)
        if w+200 <= mouse[0] <= w+300 and h+60 <= mouse[1] <= h+160:
            drawCross(w+200, h+60)
        if w+450 <= mouse[0] <= w+550 and h+60 <= mouse[1] <= h+160:
            drawCross(w+450, h+60)
        
        pygame.display.update()
        
    return genome_size
        
drawMenu()
