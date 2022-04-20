import pygame
import sys
import os
pygame.init()

# Display constts
width,height=600,650

#colors
bgcolor = (0,0,0)
accentclr = (48,245,34)
txtclr = (255,255,255)

#text
heading = pygame.font.SysFont('Source Code Pro',50)
winnertext = pygame.font.SysFont('Source Code Pro',70)
timertext = pygame.font.SysFont('Source Code Pro',30)
turntext = pygame.font.SysFont('Source Code Pro',30)

#images
crossimg=pygame.transform.scale( pygame.image.load(r"assets\cross.png"),(76,76))
zeroimg = pygame.transform.scale(pygame.image.load(r"assets\xero.png"),(76,76))

#display and clock 
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic-Tac-Toe")
clock=pygame.time.Clock()
fps=10




#draw elements function
def draw( bgobjs,bgtiles,bgtcolors,cross,zero,whoseturn):
    win.fill(bgcolor)
    
    #heading
    headingbg=pygame.Rect(0,0,width,50)
    pygame.draw.rect(win,accentclr,headingbg)
    headingtext = heading.render("Tic - Tac - Toe",1,bgcolor)
    win.blit(headingtext,(width//2-headingtext.get_width()//2,10))
    
    #grid
    
    for i in range(len(bgtiles)):
        for j in range(len(bgtiles[i])):
            pygame.draw.rect(win,bgtcolors[i][j],bgtiles[i][j])
            # pygame.draw.rect(win,bgcolor,bgobjs[i][j])
    #cross and zero 
    for i in range(4):
        for j in range(4):
            obj=bgobjs[i][j]
            tup =(i,j)
            if tup in cross:
                win.blit(crossimg,(obj.x,obj.y))
            elif tup in zero:
                win.blit(zeroimg,(obj.x,obj.y))
            else:
                pygame.draw.rect(win,bgcolor,obj)
                
    #turn text
    turndisp = turntext.render(whoseturn,1,accentclr)
    win.blit(turndisp,(width//2-turndisp.get_width()//2,620))
    
    pygame.display.update()

#function to detect win:
def detectwin(l):
    poss=[]
    for i in range(4):
        tmp=[(i,j) for j in range(3)]
        poss.append(tmp)
        tmp=[(i,j) for j in range(1,4)]
        poss.append(tmp)
        
    for j in range(4):
        tmp=[(i,j) for i in range(3)]
        poss.append(tmp)
        tmp=[(i,j) for i in range(1,4)]
        poss.append(tmp)
    poss.extend([[(0,0),(1,1),(2,2)],[(1,1),(2,2),(3,3)],[(0,3),(1,2),(2,1)],[(1,2),(2,1),(3,0)]])
    poss.extend([[(0,2),(1,1),(2,0)],[(3,1),(2,2),(1,3)],[(1,0),(2,1),(3,2)],[(0,1),(1,2),(2,3)]])
    for el in poss:
        if el[0] in l and el[1] in l and el[2] in l:
            return True
    return False

def drawwin(text):
    disptext = winnertext.render(text,1,txtclr)
    win.blit(disptext,(width//2-disptext.get_width()//2,70))
    timer = timertext.render("Game resets in : 3 seconds",1,accentclr)
    win.blit(timer,(width//2-timer.get_width()//2,120))
    pygame.display.update()
    pygame.time.delay(3000)
    # for i in range(3,0,-1):
    #     timer = timertext.render("Game resets in : "+str(i)+" seconds",1,txtclr)
    #     print(i)
    #     win.blit(timer,(width//2-timer.get_width()//2,200))
    #     pygame.display.update()
    #     pygame.time.delay(1000)
        
    
    
def main():
    
    #grid elements:
    bgtiles=[]
    bgtcolors=[]
    bgobjs=[]
    inix,iniy=100,200
    for i in range(4):
        tmplist=[]
        tmplist2=[]
        tmplist3=[]
        for j in range(4):
            tmp=pygame.Rect(inix+j*100,iniy+i*100,100,100)
            tmplist.append(tmp)
            tmp=pygame.Rect(inix+12+j*100,iniy+12+i*100,76,76)
            tmplist2.append(tmp)
            tmplist3.append(txtclr)
        bgtiles.append(tmplist)
        bgobjs.append(tmplist2)
        bgtcolors.append(tmplist3)
   
    #state variables
    cross=[]
    zero=[]
    aci,acj=0,0
    turn=True
    
    run=True
    
    #game loop
    while run:
        clock.tick(fps)
        
        #fetching events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            if aci>0:
                aci-=1
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            if aci<3:
                aci+=1
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            if acj>0:
                acj-=1
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            if acj<3:
                acj+=1
                
        
        for i in range(4):
            for j in range(4):
                if i==aci and j==acj:
                    bgtcolors[i][j]=accentclr
                else:
                    bgtcolors[i][j]=txtclr
        
        if keys_pressed[pygame.K_f] or keys_pressed[pygame.K_RCTRL]:
            tup=(aci,acj)
            if tup not in cross and tup not in zero:
                if turn:
                    cross.append(tup) 
                else:
                    zero.append(tup)
                turn=not turn
                
        if turn:
            whoseturn="Cross' turn"
        else:
            whoseturn="Zero's turn"
        draw( bgobjs,bgtiles,bgtcolors,cross,zero,whoseturn)   
        if detectwin(cross):
            drawwin("CROSS WINS!!")
            main()
        if detectwin(zero):
            drawwin("ZERO WINS!!")
            main()
        if len(cross) + len(zero)==16:
            drawwin("NOBODY WON")
            main()

if __name__=="__main__":
    main()