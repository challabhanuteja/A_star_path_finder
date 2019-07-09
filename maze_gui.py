import pygame
import numpy as np
def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
n = 10
a = [[0]*n for i in range(n)]
start=[0,0]
end=[9,0]
#a[][0]=-1
def new_a_star(a,start,end,dc,lc):
    h = [[0]*n for i in range(n)]
    f = [[0]*n for i in range(n)]
    ex,ey=end
    for i in range(n): #calculating heuristic values for all the nodes because the list is static
        for j in range(n):
            h[i][j] = (abs(ex-i)+abs(ey-j))*10
    sx,sy=start
    open,closed=[h[sx][sy]],[]
    #finding the eklements of open List
    first = 0
    r=0
    while(len(open)!=0 and r<10):
        r+=1
        if first==0:
            closed.append(open[0])
            open.remove(h[sx][sy])
            first=1
        x1 = sx-1
        if(x1<0): #to solve the problems happen at edges of the matrix
            x1=0
        x2= sx+2
        if(x2>n):#to solve the problems happen at edges of the matrix
            x2=n
        y1 = sy-1
        if(y1<0):#to solve the problems happen at edges of the matrix
            y1=0
        y2= sy+2
        if(y2>n):#to solve the problems happen at edges of the matrix
            y2=n
        g=[]
        q=0
        for i in range(x1,x2):
                for j in range(y1,y2):
                    if a[i][j]==-1 :
                        continue
                    if i==x2//2 and j==y2//2:
                        g.append(0)
                    elif (i+j)%2!=0:
                        g.append(lc)
                    else:
                        g.append(dc)
                    open.append(h[i][j] + g[q])
                    f[i][j] = g[q]+h[i][j]
                    q+=1

        #finding the minimum element in open list
        minimum = min(open)
        closed.append(minimum)
        sx,sy = index_2d(f,minimum)
        open.remove(minimum)

        # print(closed)
        # print(sx,sy)
        # print(g)
        # print(np.matrix(h))
        # print(np.matrix(f))
    return closed,f

pygame.init()

white = (255,255,255)
red = (255,0,0)
green =(0,255,0)
blue = (0,0,255)
black = (0,0,0)
grey = (128,128,128)
window_width=800
window_height=800
gameDisplay = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('A* path finder')
pygame.display.update() #or pygame.display.flip()
clock = pygame.time.Clock()


w=window_width/n
h=window_height/n
gameDisplay.fill(white)
x,y=0,0
for row in a:
    for col in row:
        pygame.draw.rect(gameDisplay,black,[x,y,w,h],2)
        if col==-1:
            gameDisplay.fill(grey,[x,y,w,h])

        x+=w
    x=0
    y=y+h
gameDisplay.fill(blue,[start[0]*w,start[1]*h,w,h])
gameDisplay.fill(blue,[end[0]*w,end[1]*h,w,h])
pygame.display.update()


def game_loop():
    completed = False
    gameExit = False
    closed1,f1=    new_a_star(a,start,end,14,10)
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        for i in closed1:
            x,y= index_2d(f1,i)
            gameDisplay.fill(green,[x*h,y*w,w,h])
            clock.tick(1)
            pygame.display.update()
        completed=True
        if completed ==True:
            break

game_loop()
