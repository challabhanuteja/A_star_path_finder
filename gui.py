import pygame
pygame.init()
display_width = 800
display_height= 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

a = [[0]*10 for n in range(10)]
w=80

def draw():
    while(True):
        x,y=0,0
        for row in a:
            for col in row:
                pygame.draw.rect(gameDisplay,y,w,w)
                x+=w
    pygame.display.update()
    clock.tick(75)
draw()
pygame.quit()
quit()
