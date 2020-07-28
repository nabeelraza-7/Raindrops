# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:50:08 2020

@author: Nabeel
"""
import random
import pygame

bg = (127, 127, 127)
PURPLE = (255,0,255)
BLACK = (0,0,0)
rect_width = 3
rect_height = 10
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rain")
screen.fill(BLACK)
# fps = 60
# clock = pygame.time.Clock()
class rain:
    def __init__(self, screen):
        self.screen = screen
        rect_width = random.randint(1,2)
        rect_height = random.randint(10,15)
        self.x = random.randint(0+rect_width, width)
        self.y = random.randint(-700, -50)
        
        self.rect = [self.x, self.y, rect_width, rect_height]
        
    def update(self):
        self.rect[1] += random.randint(2,5)
        if self.rect[1] >= 600:
            self.rect[1] = random.randint(-150, -100)
        
    def reposition(self):
        self.rect.y = 0
    
    def __repr__(self):
        """Only for debugging to see how it prints."""
        return f'Rain({self.rect[0]}, {self.rect[1]})'
        
drops = []
for i in range(800):
    
    x = rain(screen)
    pygame.draw.rect(screen, PURPLE, tuple(x.rect), 0)
    drops.append(x)
flag = False
running = True
while running:
    # clock.tick(fps)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            flag = True
        if keys[pygame.K_ESCAPE]:
            flag = False
    if flag:   
        for x in drops:
            x.update()
        for x in drops:
            pygame.draw.rect(screen, PURPLE, x.rect, 0)
    pygame.display.flip()
pygame.quit()