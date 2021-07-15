import pygame
from pygame.locals import *

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
shade = (40,40,40)
green = (0, 255, 0)
blue = (0, 0, 255)

screen= pygame.display.set_mode((display_width,display_height))

pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(shade)
    #Draw all the 5 towns
    pygame.display.set_caption("Optimal Path Finder")
    pygame.draw.ellipse(screen, red, (20, display_height/2, 40, 40))    
    pygame.draw.ellipse(screen, red, (240, display_height/2-80, 40,40))
    pygame.draw.ellipse(screen, red, (display_width/2, display_height/2+40, 40,40))
    pygame.draw.ellipse(screen, red, (display_width/2 + 120, display_height/2-30, 40,40))
    pygame.draw.ellipse(screen, red, (display_width/2 + 350, display_height/2+80, 40,40))

    # Draw the roads between the towns
    pygame.draw.line(screen, green, (40, 320), (260, 240))
    pygame.draw.line(screen, green, (260, 240), (420, 360))
    pygame.draw.line(screen, green, (420, 360), (540, 290))
    pygame.draw.line(screen, green, (420, 360), (770, 400))

    pygame.display.update()
    

pygame.quit()