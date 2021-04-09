import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
clock=pygame.time.Clock()
surface =pygame.display.set_mode((300,400))
pygame
current_y = 100
dy = 0
gravity = 0.1

color=(255,0,0)

#dy =-2

def drawBall(drawY, drawX, color=(0,255,0)):
 pygame.draw.circle(surface, (0, 255, 0), (drawX, int(current_y)), 12)

def quitGame():
	pygame.quit()
	sys.exit()
while True:
    surface.fill((0,0,0))
    dy -= gravity
    current_y -= dy
    drawBall(current_y,150)
    

    print(current_y)
    if current_y>376 or current_y<10:
        print("**************************")
        dy *= -1
        color =(0,0,255)
	
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
                            
    clock.tick(30)
    pygame.display.update()
