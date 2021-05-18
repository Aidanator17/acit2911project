import chess
import pygame
import random
import time
from IPython.display import display, HTML, clear_output
from module import display
from database import dbpush #playernumber, playercolor, AIcolor, Movelist, Winner("Player" or "AI"), datePlayed, time(seconds)
from sqlalchemy import Table, Column, String, MetaData, create_engine, ARRAY
import uuid
from datetime import datetime

from pynput.mouse import Listener


class Game:

    def __init__(self, player1, player2, option=False):
        self.player1 = player1
        self.player2 = player2
        self.option = option
        self.moves = []
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
        prompt = f"{self.who(game_board.turn)}'s move [q to quit]"
        uci = self.get_move(prompt)
        legal_uci_moves = [move.uci() for move in game_board.legal_moves]
        while uci not in legal_uci_moves:
            print("Legal moves: " + (",".join(sorted(legal_uci_moves))))
            uci = self.get_move("%s's move[q to quit]> " % self.who(game_board.turn))
        self.move_txt(uci, game_board)
        return uci

    def dbGame(self, game_board, starttime):
        d1 = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        gametime = float(time.time()) - starttime
        if self.who(not game_board.turn) == self.playerc:
            winner = 'player'
        else:
            winner = 'AI'
        if self.playerc == 'Black':
            aic = 'White'
        else:
            aic = 'Black'
        dbpush('Peter',self.playerc,aic,self.moves,winner,d1,round(gametime,1))
    
    def translate_piece(self, opiece):
        piece = str(opiece)
        if piece.lower() == 'k':
            return "king"
        if piece.lower() == 'q':
            return "queen"
        if piece.lower() == 'p':
            return "pawn"
        if piece.lower() == 'r':
            return "rook"
        if piece.lower() == 'b':
            return "bishop"
        if piece.lower() == 'n':
            return "knight"
        else:
            return "unknown"

    def get_move(self, prompt):
        """ get a move from the player """
        selections = []
        while len(selections) < 2:
            ev = display.pygame.event.get()
            pos_x, pos_y = display.pygame.mouse.get_pos()
            for event in ev:
                if event.type == display.pygame.MOUSEBUTTONUP:
                    print(f'mouse {pos_x}, {pos_y}')
                    
                    # Checking position A
                    if (pos_x > 100 ) and (pos_x < 148) and (pos_y > 100) and (pos_y < 498):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('a8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('a7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('a6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('a5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('a4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('a3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('a2')
                        elif (pos_y > 450):
                            selections.append ('a1')
                    
                    # Checking position B
                    if (pos_x > 150) and (pos_x < 198):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('b8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('b7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('b6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('b5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('b4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('b3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('b2')
                        elif (pos_y > 450):
                            selections.append ('b1')

                    #checking position C

                    if(pos_x > 200) and (pos_x < 250):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('c8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('c7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('c6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('c5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('c4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('c3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('c2')
                        elif (pos_y > 450):
                            selections.append ('c1')
                    
                    # Checking column D

                    if (pos_x > 250) and (pos_x < 300):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('d8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('d7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('d6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('d5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('d4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('d3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('d2')
                        elif (pos_y > 450):
                            selections.append ('d1')
                    
                    # Checking column E

                    if (pos_x > 300) and (pos_x < 350):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('e8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('e7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('e6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('e5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('e4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('e3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('e2')
                        elif (pos_y > 450):
                            selections.append ('e1')
                        
                    # Checking column F

                    if (pos_x > 350) and (pos_x < 400):
                        if (pos_y > 100) and (pos_y < 150):
                                selections.append('f8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('f7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('f6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('f5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('f4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('f3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('f2')
                        elif (pos_y > 450):
                            selections.append ('f1')
                    # Checking column G

                    if (pos_x > 400) and (pos_x < 450):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('g8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('g7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('g6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('g5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('g4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('g3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('g2')
                        elif (pos_y > 450):
                            selections.append ('g1')
                    # Checking column H

                    if (pos_x > 450) and (pos_x < 500):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('h8')
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('h7')
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('h6')
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('h5')
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('h4')
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('h3')
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('h2')
                        elif (pos_y > 450):
                            selections.append ('h1')

                 
                    

                    
        #uci = input(prompt)
        t_uci = selections[0] + selections[1]
        print(t_uci)
        #if uci and uci[0] == "q":
         #   raise KeyboardInterrupt()
        try:
            chess.Move.from_uci(t_uci)
        except:
            t_uci = None
        return t_uci

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
            if self.option == True:
                if turn == self.playerc:
                    tmove = f"Player ({turn}) moved {self.translate_piece(piece)} from {start_pos} to {end_pos}"
                    print(tmove)
                    self.moves.append(tmove)
                else:
                    tmove = f"{turn} moved {self.translate_piece(piece)} from {start_pos} to {end_pos}"
                    print(tmove)
                    self.moves.append(tmove)
            else:
                print(f"{turn} moved {self.translate_piece(piece)} from {start_pos} to {end_pos}")
            time.sleep(1)

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
        starttime = float(time.time())
        self.playerc = 'White'
        
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
            if self.option == True:
                self.dbGame(game_board,starttime)
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


