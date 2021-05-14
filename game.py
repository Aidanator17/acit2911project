import chess
import pygame
import random
import time
from IPython.display import display, HTML, clear_output
from chessboard import display

from pynput.mouse import Listener


class Game:

    def __init__(self, player1, player2, option=False):
        self.player1 = player1
        self.player2 = player2
        self.option = option
        self.player1 = input("Enter 1 for AI or 2 for self play: ")
        if self.player1 == '1':
            self.option = False
        elif self.player1 == '2':
            self.option = True
        
        self.play_game()

        #self.player2 = random_player
    def user(self, game_board):
        """ 
        User function: updates the game board, and requests a move from the playe, and checks that move to a list of the legal moves to makes sure that it is a valid move. 
        """
        display.update(game_board.fen())
        
        #getting the move from the function get_move()
        #uci = self.get_move("%s's move [q to quite]> " % self.who(game_board.turn))
        prompt = f"{self.who(game_board.turn)}'s move [q to quite]"
        uci = self.get_move(prompt, game_board)
        legal_uci_moves = [move.uci() for move in game_board.legal_moves]
        while uci not in legal_uci_moves:
            print("Legal moves: " + (",".join(sorted(legal_uci_moves))))
            uci = self.get_move("%s's move[q to quit]> " % self.who(game_board.turn))
        self.move_txt(uci, game_board)
        return uci

    def get_move(self, prompt, game_board):
        """ get a move from the player """
        test = True
        while test == True:
            ev = display.pygame.event.get()
            pos_x, pos_y = display.pygame.mouse.get_pos()
            for event in ev:
                if event.type == display.pygame.MOUSEBUTTONUP:
                    print(f'mouse {pos_x}, {pos_y}')
                    
                    # Checking position A
                    if (pos_x > 100 ) and (pos_x < 148) and (pos_y > 100) and (pos_y < 498):
                        if (pos_y > 100) and (pos_y < 150):
                            print('a8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('a7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('a6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('a5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('a4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('a3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('a2')
                        elif (pos_y > 450):
                            print ('a1')
                    
                    # Checking position B
                    if (pos_x > 150) and (pos_x < 198):
                        if (pos_y > 100) and (pos_y < 150):
                            print('b8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('b7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('b6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('b5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('b4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('b3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('b2')
                        elif (pos_y > 450):
                            print ('b1')

                    #checking position C

                    if(pos_x > 200) and (pos_x < 250):
                        if (pos_y > 100) and (pos_y < 150):
                            print('c8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('c7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('c6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('c5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('c4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('c3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('c2')
                        elif (pos_y > 450):
                            print ('c1')
                    
                    # Checking column D

                    if (pos_x > 250) and (pos_x < 300):
                        if (pos_y > 100) and (pos_y < 150):
                            print('d8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('d7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('d6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('d5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('d4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('d3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('d2')
                        elif (pos_y > 450):
                            print ('d1')
                    
                    # Checking column E

                    if (pos_x > 300) and (pos_x < 350):
                        if (pos_y > 100) and (pos_y < 150):
                            print('e8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('e7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('e6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('e5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('e4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('e3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('e2')
                        elif (pos_y > 450):
                            print ('e1')
                        
                    # Checking column F

                    if (pos_x > 350) and (pos_x < 400):
                        if (pos_y > 100) and (pos_y < 150):
                                print('f8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('f7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('f6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('f5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('f4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('f3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('f2')
                        elif (pos_y > 450):
                            print ('f1')
                    # Checking column G

                    if (pos_x > 400) and (pos_x < 450):
                        if (pos_y > 100) and (pos_y < 150):
                            print('g8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('g7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('g6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('g5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('g4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('g3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('g2')
                        elif (pos_y > 450):
                            print ('g1')
                    # Checking column H

                    if (pos_x > 450) and (pos_x < 500):
                        if (pos_y > 100) and (pos_y < 150):
                            print('h8')
                        elif (pos_y > 150) and (pos_y < 200):
                            print('h7')
                        elif (pos_y > 200) and (pos_y < 250):
                            print('h6')
                        elif (pos_y > 250) and (pos_y < 300):
                            print('h5')
                        elif (pos_y > 300) and (pos_y < 350):
                            print('h4')
                        elif (pos_y > 350) and (pos_y < 400):
                            print('h3')
                        elif (pos_y > 400) and (pos_y < 450):
                            print('h2')
                        elif (pos_y > 450):
                            print ('h1')

                 
                    

                    
        uci = input(prompt)
        if uci and uci[0] == "q":
            raise KeyboardInterrupt()
        try:
            chess.Move.from_uci(uci)
        except:
            uci = None
        return uci

    def on_move(self, x, y):
        """ 
        function for mouse movement that will capture the x, and y position
        """
        pass
    
    def on_click(self, x, y, button, pressed):
        """ captures the mouse click """
        print('Click')
    
    def on_scroll(self, x, y, dx, dy):
        pass


    def random_player(self, game_board):
        """ 
        AI function; takes a list of legal moves and makes a random choice. based off of that move it will split it in two in order to create a nice message that will tell the player which move was just made
        """
        ai_move = random.choice(list(game_board.legal_moves))
        self.move_txt(ai_move, game_board)
        
        return ai_move.uci()

    def move_txt(self, move, game_board):
        """ 
        function for indicating which move was just made. takes the move and splits it into two and takes the starting position and passes it into the chessboard to parse which square it was from, and then based off of that square parses which peices was on there
        """ 
        move = str(move)
        start_pos, end_pos = move[:len(move)//2], move[len(move)//2:]
        turn = self.who(game_board.turn)
        square = chess.parse_square(start_pos)
        if chess.BaseBoard():
            piece = chess.BaseBoard.piece_at(chess.BaseBoard(), square)
            print(f"{turn} has move {piece} from {start_pos} to {end_pos}")
        

    def who(self, player):
        """ function for displaying the color of a player """
        return "White" if player == chess.WHITE else "Black"

    def view_game(self, game_board, use_display):
        """ function for displaying the board """
        # if bool(game_board.castling_rights):
        #     print("you can castle: BBH1")
        return display.update(game_board.fen())

    def play_game(self, pause=0.1):
        game_board = chess.Board()
        use_display = display.start(game_board.fen())
        
        
        try:
            while not game_board.is_game_over(claim_draw=True):
                if game_board.turn == chess.WHITE:
                    if self.option == True:
                        uci = self.user(game_board)
                    else:
                        uci = self.random_player(game_board)
                else:
                    uci = self.random_player(game_board)
                name = self.who(game_board.turn)
                game_board.push_uci(uci)
                board_stop = self.view_game(game_board, use_display)
                html = "<b>Move %s %s, Play '%s':</b><br/>%s" % (
                        len(game_board.move_stack), name, uci, board_stop)
                if use_display is not None:
                    if use_display:
                        clear_output(wait=True)
                    display(HTML(html))
                    if use_display:
                        time.sleep(pause)
        except KeyboardInterrupt:
            msg = "Game interrupted!"
            return (None, msg, game_board)
        result = None
        if game_board.is_check():
            msg = "check: " + self.who(not game_board.turn)
            print(msg)
        if game_board.is_checkmate():
            msg = "checkmate: " + self.who(not game_board.turn) + " wins!"
            result = not game_board.turn
            print(msg)
        elif game_board.is_stalemate():
            msg = "draw: stalemate"
            print(msg)
        elif game_board.is_fivefold_repetition():
            msg = "draw: 5-fold repetition"
            print(msg)
        elif game_board.is_insufficient_material():
            msg = "draw: insufficient material"
            print(msg)
        elif game_board.can_claim_draw():
            msg = "draw: claim"
            print(msg)
        if use_display is not None:
            print(msg)
        return (result, msg, game_board)
player1 = 0
player2 = 1

Game(player1, player2).play_game


