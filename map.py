import pygame
from pygame.locals import *
import main as algorithms
pygame.font.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
shade = (40,40,40)
green = (0, 255, 0)
path = (230,230,250)
blue = (0, 0, 255)

font = pygame.font.SysFont(None, 24)
kisumu_label = font.render('KISUMU', True, white)
nakuru_label = font.render('NAKURU', True, white)
nairobi_label = font.render('NAIROBI', True, white)
thika_label = font.render('THIKA', True, white)
mombasa_label = font.render('MOMBASA', True, white)



def setup(start, end):
    #get an array of all attempts done. 
    bfs = algorithms.BreadthFirst(start, end)
    dfs = algorithms.DepthFirst(start, end)
    aStar = algorithms.aStar(start, end)

    return bfs, dfs, aStar

attempts = setup("Kisumu", "Mombasa")
bfs = attempts[0]
dfs = attempts[1]
aStar = attempts[2]
bfs_attempts = bfs[0]
dfs_attempts = dfs[0]
aStar_attempts = aStar[0]

bfs_optimal = bfs[1].split(" --> ")
dfs_optimal = dfs[1].split(" --> ")
aStar_optimal = aStar[1].split(" --> ")
print("DFS: ", aStar_optimal)
screen= pygame.display.set_mode((display_width,display_height))

def highlight(town, parent):
    if town == "Kisumu":
        pygame.draw.ellipse(screen, green, (20, display_height/2, 40, 40))
        pygame.draw.ellipse(screen, red, (240, display_height/2-80, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2, display_height/2+40, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 120, display_height/2-30, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 350, display_height/2+80, 40,40))

        if parent == "Nakuru":
            pygame.draw.line(screen, green, (40, 320), (260, 240))
            pygame.draw.line(screen, red, (260, 240), (420, 360))
            pygame.draw.line(screen, red, (420, 360), (540, 290))
            pygame.draw.line(screen, red, (420, 360), (770, 400))

    elif town == "Nakuru":
        pygame.draw.ellipse(screen, red, (20, display_height/2, 40, 40))
        pygame.draw.ellipse(screen, green, (240, display_height/2-80, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2, display_height/2+40, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 120, display_height/2-30, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 350, display_height/2+80, 40,40))

        if parent == "Kisumu":
            pygame.draw.line(screen, green, (40, 320), (260, 240))
            pygame.draw.line(screen, red, (260, 240), (420, 360))
            pygame.draw.line(screen, red, (420, 360), (540, 290))
            pygame.draw.line(screen, red, (420, 360), (770, 400))
        elif parent == "Nairobi": 
            pygame.draw.line(screen, red, (40, 320), (260, 240))
            pygame.draw.line(screen, green, (260, 240), (420, 360))
            pygame.draw.line(screen, red, (420, 360), (540, 290))
            pygame.draw.line(screen, red, (420, 360), (770, 400))

    elif town == "Nairobi":
        pygame.draw.ellipse(screen, red, (20, display_height/2, 40, 40))
        pygame.draw.ellipse(screen, red, (240, display_height/2-80, 40,40))
        pygame.draw.ellipse(screen, green, (display_width/2, display_height/2+40, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 120, display_height/2-30, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 350, display_height/2+80, 40,40))

        if parent == "Nakuru":
            pygame.draw.line(screen, red, (40, 320), (260, 240))
            pygame.draw.line(screen, green, (260, 240), (420, 360))
            pygame.draw.line(screen, red, (420, 360), (540, 290))
            pygame.draw.line(screen, red, (420, 360), (770, 400))
        elif parent == "Thika": 
            pygame.draw.line(screen, red, (40, 320), (260, 240))
            pygame.draw.line(screen, red, (260, 240), (420, 360))
            pygame.draw.line(screen, green, (420, 360), (540, 290))
            pygame.draw.line(screen, red, (420, 360), (770, 400))
        elif parent == "Mombasa":
            pygame.draw.line(screen, red, (40, 320), (260, 240))
            pygame.draw.line(screen, red, (260, 240), (420, 360))
            pygame.draw.line(screen, red, (420, 360), (540, 290))
            pygame.draw.line(screen, green, (420, 360), (770, 400))

    elif town == "Thika":
        pygame.draw.ellipse(screen, red, (20, display_height/2, 40, 40))
        pygame.draw.ellipse(screen, red, (240, display_height/2-80, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2, display_height/2+40, 40,40))
        pygame.draw.ellipse(screen, green, (display_width/2 + 120, display_height/2-30, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 350, display_height/2+80, 40,40))

        if parent == "Nairobi": 
            pygame.draw.line(screen, red, (40, 320), (260, 240))
            pygame.draw.line(screen, red, (260, 240), (420, 360))
            pygame.draw.line(screen, green, (420, 360), (540, 290))
            pygame.draw.line(screen, red, (420, 360), (770, 400))

    elif town == "Mombasa":
        pygame.draw.ellipse(screen, red, (20, display_height/2, 40, 40))
        pygame.draw.ellipse(screen, red, (240, display_height/2-80, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2, display_height/2+40, 40,40))
        pygame.draw.ellipse(screen, red, (display_width/2 + 120, display_height/2-30, 40,40))
        pygame.draw.ellipse(screen, green, (display_width/2 + 350, display_height/2+80, 40,40))

        if parent == "Nairobi": 
            pygame.draw.line(screen, red, (40, 320), (260, 240))
            pygame.draw.line(screen, red, (260, 240), (420, 360))
            pygame.draw.line(screen, red, (420, 360), (540, 290))
            pygame.draw.line(screen, green, (420, 360), (770, 400))

def optimal(arr): #highlights the optimal path
    for i in range(len(arr)):
        if arr[i] == "Kisumu":
            pygame.draw.ellipse(screen, path, (20, display_height/2, 42, 42), width = 2)
            if i == len(arr)-1:
                break
            elif arr[i+1] == "Nakuru":
                pygame.draw.line(screen, path, (44, 324), (264, 244))
        elif arr[i] == "Nakuru":
            pygame.draw.ellipse(screen, path, (240, display_height/2-80, 42,42), width = 2)
            if i == len(arr)-1:
                break            
            elif arr[i+1] == "Kisumu":
                pygame.draw.line(screen, path, (44, 328), (264, 248))
            elif arr[i+1] == "Nairobi":
                pygame.draw.line(screen, path, (264, 248), (424, 368))
        elif arr[i] == "Nairobi":
            pygame.draw.ellipse(screen, path, (display_width/2, display_height/2+40, 42,42), width = 2)
            if i == len(arr)-1:
                break            
            elif arr[i+1] == "Thika":
                pygame.draw.line(screen, path, (424, 368), (544, 298))
            elif arr[i+1] == "Nakuru":
                pygame.draw.line(screen, path, (264, 248), (424, 368))
            elif arr[i+1] == "Mombasa":
                pygame.draw.line(screen, path, (424, 368), (774, 408))
        elif arr[i] == "Thika":
            pygame.draw.ellipse(screen, path, (display_width/2 + 120, display_height/2-30, 42,42), width = 2)
            if i == len(arr)-1:
                break            
            elif arr[i+1] == "Nairobi":
                pygame.draw.line(screen, path, (424, 368), (544, 298))      
        elif arr[i] == "Mombasa":
            pygame.draw.ellipse(screen, path, (display_width/2 + 350, display_height/2+80, 42,42), width = 2)
            if i == len(arr)-1:
                break            
            elif arr[i+1] == "Nairobi":
                pygame.draw.line(screen, path, (424, 368), (774, 408))

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
    pygame.draw.line(screen, red, (40, 320), (260, 240)) #Kisumu -> Nakuru
    pygame.draw.line(screen, red, (260, 240), (420, 360))
    pygame.draw.line(screen, red, (420, 360), (540, 290))
    pygame.draw.line(screen, red, (420, 360), (770, 400))

    #Label the towns
    screen.blit(kisumu_label, (20, display_height/2 + 50))
    screen.blit(nakuru_label, (220, display_height/2 - 20))
    screen.blit(nairobi_label, (display_width/2, display_height/2 + 90))
    screen.blit(thika_label, (display_width/2 + 120, display_height/2 +20))
    screen.blit(mombasa_label, (display_width/2 + 300, display_height/2 + 130))         

    optimal_path = "Optimal Path = " + " --> ".join(aStar_optimal)
    for track in aStar_attempts: #Change this to see different paths
        for town in track:
            if town[1] == True:
                highlight(town[0], town[2])
                pygame.time.wait(750)
        optimal(dfs_optimal)
        
        screen.blit(font.render(optimal_path, True, white), (display_width/2 - 250, display_height/2 + 200))
        pygame.display.update()        
    

pygame.quit()