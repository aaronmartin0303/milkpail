import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

# Window parameters
DISPLAYSURF = pygame.display.set_mode((800, 400))
pygame.display.set_caption('SKU Code Training')
# Color definitions in RGB
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
BLUE = (25, 25, 230)
DARKGRAY = (64, 64, 64)
YELLOW = (230, 230, 0)
RED = (230, 0, 0)
LIME = (0, 240, 0)
LIGHTGRAY = (200, 200, 200)
WHITE = (255, 255, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 142)
textSurfaceObj = fontObj.render('>', True, YELLOW, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (40, 35)
# Drawing on surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.rect(DISPLAYSURF, BLUE, (0, 0, 395, 100))
pygame.draw.rect(DISPLAYSURF, BLACK, (395, 0, 405, 400))
pygame.draw.rect(DISPLAYSURF, GRAY, (405, 5, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (505, 5, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (605, 5, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (405, 105, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (505, 105, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (605, 105, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (405, 205, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (505, 205, 90, 90)) 
pygame.draw.rect(DISPLAYSURF, GRAY, (605, 205, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (405, 305, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (505, 305, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (605, 305, 90, 90))
pygame.draw.rect(DISPLAYSURF, GRAY, (705, 205, 90, 190))
pygame.draw.rect(DISPLAYSURF, GRAY, (705, 5, 90, 190)) 
#main game loop

while True:
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

