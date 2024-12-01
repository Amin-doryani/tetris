import pygame
import time
from o import O


last_execution = time.time()
jodarcolor = (230,220,210)
object1 = O()
pygame.init()
screen_w = 360
screen_h = 660
screen = pygame.display.set_mode((screen_w, screen_h))
run = True

while run:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # move the object
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                object1.move_l(30)
            if event.key == pygame.K_RIGHT:
                object1.move_r(330)
            
            if event.key == pygame.K_DOWN:
                object1.move_d(630)





    # draw joderan
    
    yy = 0
    for row in object1.gets():
        xx = 0
        for e in row:
            if(e == 1):
                pygame.draw.rect(screen,"red",[(object1.getx() + xx),(object1.gety() + yy),30,30])
                
            xx += 30
        yy += 30 
    if time.time() - last_execution >= 1:
        object1.move_d(630)
        last_execution = time.time()
        
    pygame.draw.rect(screen,jodarcolor,[0,0,30,660])
    pygame.draw.rect(screen,jodarcolor,[0,0,360,30])
    pygame.draw.rect(screen,jodarcolor,[330,0,30,660])
    pygame.draw.rect(screen,jodarcolor,[0,630,360,30])  
    pygame.display.flip()

pygame.quit()