import pygame
from pygame.locals import *
from random import random

#Breite und Hoehe des Fensters (kann beliebig verstellt werden)
width = 1680
height = 1050
width4 = width/4
height4 = height/4

def updateall():
    draw_stars()
    pygame.display.update()

def draw_stars():
    window.fill((0,0,0))
    mousepos = pygame.mouse.get_pos()
    for star in stars:
        x = (star[0]+mousepos[0])*star[2]+width4
        y = (star[1]+mousepos[1])*star[2]+height4
        window.fill((255*star[2],255*star[2],255*star[2]),(x,y,1,1))

pygame.init()
window = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()#Fuer die FPS-Angabe

stars = []

for i in range(200):
    stars.append([int(random()*2*width-width),int(random()*2*height-height),random()])

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
    clock.tick()
    print clock.get_fps()#<-- Ausgabe der FPS-Rate
    updateall()
