import pygame
import time
from o import O
import random

last_execution = time.time()
jodarcolor = (230,220,210)

createobject = True
colors = ["#c00000","#fe0000","#ff3300","#ffff01","#92d14f","#00af50","#92d14f","#01b0f1","#0071c1","#7030a0"]
# classlist = [O(random.choice(colors))]
objectlist = []
pygame.init()
windowlist = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]


screen_w = 360
screen_h = 660
screen = pygame.display.set_mode((screen_w, screen_h))
run = True

while run:
    if createobject:
        clr = random.choice(colors)
        object1 = O(clr)
        createobject = False
    screen.fill("black")
    for objectfromlist in objectlist:
        yy = 0
        for row in objectfromlist.gets():
            xx = 0
            for e in row:
                if(e == 1):
                    pygame.draw.rect(screen,objectfromlist.color,[(objectfromlist.getx() + xx),(objectfromlist.gety() + yy),30,30])
                
                xx += 30
            yy += 30 
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
                object1.move_d(630,objectlist)
            
            if event.key == pygame.K_UP:
                object1.mchanged()




    # draw object
    
    yy = 0
    for row in object1.gets():
        xx = 0
        for e in row:
            if(e == 1):
                pygame.draw.rect(screen,object1.color,[(object1.getx() + xx),(object1.gety() + yy),30,30])
                
            xx += 30
        yy += 30 
    
    if time.time() - last_execution >= 1:
        object1.move_d(630,objectlist)
        last_execution = time.time()
    # draw jodran
    pygame.draw.rect(screen,jodarcolor,[0,0,30,660])
    pygame.draw.rect(screen,jodarcolor,[0,0,360,30])
    pygame.draw.rect(screen,jodarcolor,[330,0,30,660])
    pygame.draw.rect(screen,jodarcolor,[0,630,360,30])  
    pygame.display.flip()
    # check if the object have to stop and add it to the list of object
    for e in objectlist:
        
        if e.itis == "o" and object1.itis == "o":
            ob1X = object1.getx() + 30
            ob1Y = object1.gety() + 90
            ob2X = e.getx() + 30
            ob2Y = e.gety() + 30
            if (ob1Y == ob2Y) and ((ob1X ==  ob2X) or (ob1X == ob2X + 30) or (ob1X +30 == ob2X)):
                objectlist.append(object1)
                createobject = True
                
            
    if object1.moving == False:
        objectlist.append(object1)
        createobject = True
        
    # removethethings
    numofel = 0
    for obb in objectlist:    
        obbY = obb.gety()
        i = 0
        
        for row in obb.gets():
            obbX = obb.getx()
            j = 0
            for clm in row:
                if clm == 1:
                    ii = int(obbY/30)
                    jj = int(obbX/30)
                    # print("objcetx: ",obbX," objecty: ",obbY)
                    windowlist[ii - 1][jj - 1] = [numofel,i,j]
                j +=1
                obbX +=30
            i += 1
            obbY += 30

        numofel +=1

    
        
        
        
        

    iii = 0
    
    for row in windowlist:
        if 0 not in row:
            jjj = 0
            for cl in row:
                rmfromobject = objectlist[cl[0]]
                rmfromobject.s[cl[1]][cl[2]] = 0
                windowlist[iii][jjj] = 0
                
                jjj +=1
        iii +1
    windowlist = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]  
    for ob in objectlist:
        if all(1 not in row for row in ob.gets()):
            objectlist.remove(ob)
            

pygame.quit()