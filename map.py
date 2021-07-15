import pygame
from pygame.locals import *


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
shade = (40,40,40)
green = (0, 255, 0)
blue = (0, 0, 255)

start=(0,0)
size = (0,0)



screen= pygame.display.set_mode((display_width,display_height))

def generate_towns(n):
    print(n)

pygame.init()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         change += 10
        #         print(change)
        #         pygame.draw.ellipse(screen, blue, (20, display_height/2, change, 40))
    
    
    screen.fill(shade)
    pygame.display.set_caption("Optimal Path Finder")
    pygame.draw.ellipse(screen, red, (20, display_height/2, 40, 40))    
    pygame.draw.ellipse(screen, red, (140, display_height/2-80, 40,40))    
    pygame.display.update()
    

pygame.quit()