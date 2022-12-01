from random import choice
import pygame
from pygame.draw import *
from random import randint
from pygame.font import *
from shell import *
from classes import *

FPS = 10

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 800

FIELD_WIDTH = 1200//20
FIELD_HEIGHT = 800//20

directions = ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))
CELLS_NUMBER = 16

mutation_num = [0 for x in range(CELLS_NUMBER)]
            
def GAME(GENOME_SIZE):
    global f, f1
    pygame.font.init()
    f = Font(None, 16)
    f1 = Font(None, 24)
    
    global FPS
    pygame.init()
    screen = pygame.display.set_mode((WIDTH + 250, HEIGHT))
    screen.fill(WHITE)
    bacteria = []
    cells = [[Cell(x, y) for y in range(FIELD_HEIGHT)] for x in range(FIELD_WIDTH)]
    
    clock = pygame.time.Clock()
    finished = False
    for i in range(CELLS_NUMBER):
        bacteria.append(Bacteria(randint(1, FIELD_WIDTH - 1), randint(1, FIELD_HEIGHT - 1), cells, GENOME_SIZE, f))
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
                bac.move(bac.genome[time % GENOME_SIZE] % 8, FIELD_WIDTH, FIELD_HEIGHT)
            else:
                bac.eat_and_suffer((bac.genome[time % GENOME_SIZE] - GENOME_SIZE // 2) % 8, directions)
        for i in range(20, 1220, 20):
            line(screen, BLACK, (i, 0), (i, 800))
        for i in range(20, 800, 20):
            line(screen, BLACK, (0, i), (1200, i))     
        for i in range(len(bacteria)):
            if bacteria[i].is_dead():
                bacteria[i].mutate()
                bacteria[i].health = 16
                mutation_num[i] += 1
        text_time = f1.render(f'time = {time} ({FPS})', True, BLACK) 
        text_K_UP = f1.render('SPEED UP - ЛКМ', True, BLACK)
        text_K_DOWN = f1.render('SPEED DOWN - ПКМ', True, BLACK)
        screen.blit(text_time, (WIDTH + 10, 10))
        screen.blit(text_K_UP, (WIDTH + 10, 40))
        screen.blit(text_K_DOWN, (WIDTH + 10, 70))
            
        pygame.display.update()
    
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  #  левая кнопка мыши
                    FPS *= 2
                if event.button == 3:  # правая кнопка мыши
                    FPS = FPS // 2
            elif event.type == pygame.KEYDOWN and event.key in [pygame.K_RIGHTBRACKET, pygame.K_LEFTBRACKET]:
                if event.key == pygame.K_RIGHTBRACKET:  #  левая кнопка мыши
                    FPS = min(10240, FPS * 2)
                if event.key == pygame.K_LEFTBRACKET:  # правая кнопка мыши
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

    pygame.display.quit()    
    pygame.quit()
