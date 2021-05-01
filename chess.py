import chess
import arcade

#Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Chest"

class Chess(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        #sprite lists player 1 is white, player 2 is black
        self.p1_list = None
        self.p2_list = None

        #score
        self.score = 0

    def setup(self):
        """ Set up of the game. To restart game call this function """
        self.p1_list = arcade.SpriteList()
        self.p2_list = arcade.SpriteList()

        self.score = 0
        



