import os
import sys
import pygame
from pygame.locals import *
import time
from . import board

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'images')

background_image = pygame.image.load(os.path.join(IMAGE_DIR, 'park2.png'))
#os.environ['SDL_VIDEODRIVER'] = 'dummy'

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

MOVE_CAPTION = []

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
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
    pygame.font.init()

    # Setting up the GUI window.
    pygame.display.set_caption('Chess')
    BASICFONT = pygame.font.SysFont('calibri', BASICFONTSIZE)
    font = pygame.font.SysFont('calibri', 60)
    msg = False

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
def message(turn, piece, start_pos, end_pos):
    font = pygame.font.SysFont('papyrus', 38, bold=True)
    message = font.render(f"{turn} has move {piece} from {start_pos} to {end_pos}", True, (199, 133, 66))
    # print(pygame.font.get_fonts())

    # clock = pygame.time.Clock()
    msg_surf = message.copy()
    # alpha = 255
    # timer = 10
    # while alpha > 200:
    #     if timer > 0:
    #         timer -= 1
    #     else:
    #         if alpha > 200:
                # print(f'timer {timer}, alpha {alpha}')
                # alpha = max(200, alpha)
    msg_surf = message.copy()
    #msg_surf.fill((140, 93, 46)

        #DISPLAYSURF.fill((30, 30, 30))
        #while timer > 0:

    DISPLAYSURF.blit(msg_surf, (WINDOWWIDTH/2 - msg_surf.get_width()/2, WINDOWHEIGHT/2 - msg_surf.get_height()))
        #clock.tick(30)
        #time = 20
    pygame.display.update()

    # DISPLAYSURF(message, (100, 100))

def invalid_move(inv_msg):
    """ Message for invalid move """
    font = pygame.font.SysFont('papyrus', 38, bold=True)
    message = font.render(inv_msg, True, (199, 133, 66))
    
    DISPLAYSURF.blit(message, (WINDOWWIDTH/2 - message.get_width()/2, WINDOWHEIGHT//2))
    pygame.display.update()

def indication(cord):
    """ function to draw rectangle to indicate selected piece """
    x = cord[0]
    y = cord[1]
    

    print(x, y)
        # pygame.draw.rect(DISPLAYSURF, pygame.Color(255, 255, 255, 128), pygame.Rect(x, y, 50, 50))
    ind_surf = pygame.Surface((50, 50))
    ind_surf.set_alpha(128)
    ind_surf.fill((76, 230, 0))
    DISPLAYSURF.blit(ind_surf, (x, y))
    pygame.display.update()
    return None

def update(fen):
    checkForQuit()
    DISPLAYSURF.blit(background_image, [0, 0])
    gameboard.displayBoard()
    gameboard.updatePieces(fen) 
    pygame.display.update()
    FPSCLOCK.tick(FPS)


