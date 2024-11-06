import pygame

bg_colour = (128, 0, 128)

screen = pygame.display.set_mode((300, 300)) 

pygame.display.set_caption("Elements") 

rec_x = 250
rec_y = 250
rec_w = 100
rec_h = 50

while True:
    color1 = (random.radint(0,255),random.radint(0,255),random.radint(0,255))
    color2 = (random.radint(0,255),random.radint(0,255),random.radint(0,255))
    color3 = (random.radint(0,255),random.radint(0,255),random.radint(0,255))
