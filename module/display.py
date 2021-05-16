import os
import sys
import pygame
from pygame.locals import *

from . import board

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'images')

background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'park2.png'))

os.environ['SDL_VIDEO_CENTERED'] = '1' # Centre display window.

FPS = 30
FPSCLOCK = pygame.time.Clock()

DISPLAYSURF = None

BASICFONT = None

gameboard = None

colors = {
    'Brown':  (101, 67, 33),
    'White':(234, 223, 200),
    'Black':(54, 34, 4),
}

BGCOLOR = colors['Brown']

WINDOWWIDTH, WINDOWHEIGHT = 600, 600



BASICFONTSIZE = 30


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() #terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back
    
    return False


def start(fen=''):
    global gameboard
    pygame.init()

    # Setting up the GUI window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Chess')
    BASICFONT = pygame.font.SysFont('calibri', BASICFONTSIZE)
    checkForQuit()

    # DISPLAYSURF.fill(BGCOLOR)

    # Setting the background image here
    DISPLAYSURF.blit(background_image, [0, 0])
    gameboard = board.Board(colors, BGCOLOR, DISPLAYSURF)
    gameboard.displayBoard()

    if (fen):
        gameboard.updatePieces(fen)
    else:
        gameboard.drawPieces()
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def update(fen):
    checkForQuit()
    gameboard.displayBoard()
    gameboard.updatePieces(fen)    
    pygame.display.update()
    FPSCLOCK.tick(FPS)
