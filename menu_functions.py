import sys 
import os
import pygame
from pygame.draw import *
from pygame.font import *
from menu_classes import *

color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100)
black = (0, 0, 0)

pygame.font.init()

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
text44 = smolfont.render('новая клетка с 16 очками здоровья.', True, color)
cross = smallfont.render('X', True, color)
cross1 = smallfont.render('X', True, color_light)
title = font.render('Game of Life', True, color)
prompt = font1.render('Выберите длину генома', True, color)


'''
Вспомогательные функции:
Size — определить размер всех квадратиков;
Outline — определить ширину обводки всех квадратиков;
pos — определить положение i-го квадратика.
'''

def Size(amount, width):
    size = round(width/(2.5*amount + 1.5))
    return size

def Outline(amount, width):
    outline = round((1 - 0.8**(1/2))*(width/(2.5*amount + 1.5)))
    if round((1 - 0.8**(1/2))*(width/(2.5*amount + 1.5))) == 0:
        outline = 0.5
    return outline
    
def pos(i, size):
    pos = 1.5*size*(i+1) + size*i
    return pos

'''
drawRules — нарисовать экран с правилами.
'''
def drawRules(screen):    
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
        
'''
drawSelect — нарисовать экран с выбором размера генома.
'''
def drawSelect(screen):
    width = screen.get_width() 
    height = screen.get_height()     
    amount = 10
    w = width/2
    h = height/2
    
    Rect = []
    size = Size(amount, width)
    outline = Outline(amount, width)
    for i in range(amount):
        Rect.append(Checkbox(pos(i, size), size, outline, i))
        
    finished = False
    while not finished:
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for i in range(amount):
                    if Rect[i].pos <= mouse[0] <= Rect[i].pos + size and h+60 <= mouse[1] <= h+60 + size:
                        genome_size = 2**(i+3)
                        finished = True
                    
        screen.fill((255, 255, 255)) 
        mouse = pygame.mouse.get_pos()          
        
        for i in range(amount):
            Rect[i].drawRect(screen, h)
            Rect[i].Text(screen, h, amount)
        
        rect(screen,color_dark,[width/2-600,height/2-350,1200,170])
        screen.blit(prompt,(width/2-500,height/2 - 315))
        
        for i in range(amount):
            if Rect[i].pos <= mouse[0] <= Rect[i].pos + size and h+60 <= mouse[1] <= h+60 + size:        
                Rect[i].drawCross(screen, h)
                
        pygame.display.update()
        
    return genome_size

'''
drawMenu — нарисовать главный экран.
'''
def drawMenu(screen):
    width = screen.get_width() 
    height = screen.get_height()     
    finished = False
    while not finished:     
        for ev in pygame.event.get():                    
            if ev.type == pygame.QUIT: 
                pygame.quit() 
               
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if width/2-182 <= mouse[0] <= width/2+182 and height/2-70 <= mouse[1] <= height/2+15:  
                    genome_size = drawSelect(screen)
                    
                    finished = True
                elif width/2-182 <= mouse[0] <= width/2+182 and height/2+150 <= mouse[1] <= height/2+235:
                    pygame.display.quit()
                    pygame.quit()
                elif width/2-182 <= mouse[0] <= width/2+182 and height/2+40 <= mouse[1] <= height/2+125:
                    drawRules(screen)
                            
        screen.fill((255, 255, 255)) 
        mouse = pygame.mouse.get_pos() 
    
        rect(screen,color_dark,[width/2-182,height/2-70,364,85])
        rect(screen,color_dark,[width/2-182,height/2+150,364,85])
        rect(screen,color_dark,[width/2-182,height/2+40,364,85])
        rect(screen,color_dark,[width/2-600,height/2-350,1200,170])
    
        if width/2-182 <= mouse[0] <= width/2+182 and height/2-70 <= mouse[1] <= height/2+15: 
            rect(screen,color_light,[width/2-182,height/2-70,364,85]) 
        elif width/2-182 <= mouse[0] <= width/2+182 and height/2+40 <= mouse[1] <= height/2+125:
            rect(screen,color_light,[width/2-182,height/2+40,364,85])
        elif width/2-182 <= mouse[0] <= width/2+182 and height/2+150 <= mouse[1] <= height/2+235:
            rect(screen,color_light,[width/2-182,height/2+150,364,85])

        screen.blit(start,(width/2-80,height/2 -60))
        screen.blit(rules,(width/2-125,height/2+ 50))
        screen.blit(quit,(width/2-95,height/2+ 160))
        screen.blit(title,(width/2-400,height/2 - 330))
      
        pygame.display.update()
        
    pygame.display.quit()
    pygame.quit()
    return genome_size