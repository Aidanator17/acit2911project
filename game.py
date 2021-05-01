import chess
import pygame
from chessboard import display

game_board = chess.Board()
pygame.display.set_caption("Chess Game")

def main():
    run = True
    main_font = pygame.font.SysFont("comicsans", 50)

while True:
    display.start(game_board.fen())
