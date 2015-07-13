import pygame
import math
pygame.init()
width, height = 600,500
screen = pygame.display.set_mode((width,height))

imageW = 34
imageH = 48

dot = pygame.image.load("dot.png");
x=100
y=100

screen.fill(0)
screen.blit(dot,(x,y));
pygame.display.flip();
pygame.image.save(screen,'stuff.png')