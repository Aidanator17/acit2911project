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
        """ Initializing variables, and checking cases """
        try:
            int(player1)
            self.player1 = player1
        except:
            print("Player can only be an integer (player_id)")
            raise TypeError()

        try:
            int(player2)
            self.player2 = player2
        except:
            print("Player can only be an integer (player_id)")
            raise TypeError() 


        self.option = option
        self.mode=""

        #self.player2 = random_player
    def user(self, game_board):
        """ 
        User function: updates the game board, and requests a move from the playe, and checks that move to a list of the legal moves to makes sure that it is a valid move. 
        """
        display.update(game_board.fen())
        
        prompt = f"{self.who(game_board.turn)}'s move [q to quite]"
        uci = self.get_move(prompt)
        legal_uci_moves = [move.uci() for move in game_board.legal_moves]
        while uci not in legal_uci_moves:
            print("Legal moves: " + (",".join(sorted(legal_uci_moves))))
            inv_move = "Invalid Move"
            display.invalid_move(inv_move)
            time.sleep(2)
            display.update(game_board.fen())
            uci = self.get_move("%s's move[q to quit]> " % self.who(game_board.turn))
            display.update(game_board.fen())
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
        name = input('Please enter your name: ')
        dbpush(name,self.playerc,aic,self.moves,winner,d1,round(gametime,1))
    
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
        cord = []
        ind = True
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
                            cord.append(100)
                            cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('a7')
                            cord.append(100)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('a6')
                            cord.append(100)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('a5')
                            cord.append(100)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('a4')
                            cord.append(100)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('a3')
                            cord.append(100)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('a2')
                            cord.append(100)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('a1')
                            cord.append(100)
                            cord.append(450)
                    
                    # Checking position B
                    if (pos_x > 150) and (pos_x < 198):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('b8')
                            cord.append(150)
                            cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('b7')
                            cord.append(150)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('b6')
                            cord.append(150)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('b5')
                            cord.append(150)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('b4')
                            cord.append(150)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('b3')
                            cord.append(150)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('b2')
                            cord.append(150)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('b1')
                            cord.append(150)
                            cord.append(450)

                    #checking position C

                    if(pos_x > 200) and (pos_x < 250):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('c8')
                            cord.append(200)
                            cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('c7')
                            cord.append(200)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('c6')
                            cord.append(200)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('c5')
                            cord.append(200)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('c4')
                            cord.append(200)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('c3')
                            cord.append(200)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('c2')
                            cord.append(200)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('c1')
                            cord.append(200)
                            cord.append(450)
                    
                    # Checking column D

                    if (pos_x > 250) and (pos_x < 300):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('d8')
                            cord.append(250)
                            cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('d7')
                            cord.append(250)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('d6')
                            cord.append(250)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('d5')
                            cord.append(250)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('d4')
                            cord.append(250)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('d3')
                            cord.append(250)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('d2')
                            cord.append(250)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('d1')
                            cord.append(250)
                            cord.append(450)
                    
                    # Checking column E

                    if (pos_x > 300) and (pos_x < 350):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('e8')
                            cord.append(300)
                            cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('e7')
                            cord.append(300)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('e6')
                            cord.append(300)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('e5')
                            cord.append(300)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('e4')
                            cord.append(300)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('e3')
                            cord.append(300)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('e2')
                            cord.append(300)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('e1')
                            cord.append(300)
                            cord.append(450)
                        
                    # Checking column F

                    if (pos_x > 350) and (pos_x < 400):
                        if (pos_y > 100) and (pos_y < 150):
                                selections.append('f8')
                                cord.append(350)
                                cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('f7')
                            cord.append(350)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('f6')
                            cord.append(350)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('f5')
                            cord.append(350)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('f4')
                            cord.append(350)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('f3')
                            cord.append(350)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('f2')
                            cord.append(350)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('f1')
                            cord.append(350)
                            cord.append(450)
                    # Checking column G

                    if (pos_x > 400) and (pos_x < 450):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('g8')
                            cord.append(400)
                            cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('g7')
                            cord.append(400)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('g6')
                            cord.append(400)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('g5')
                            cord.append(400)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('g4')
                            cord.append(400)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('g3')
                            cord.append(400)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('g2')
                            cord.append(400)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('g1')
                            cord.append(400)
                            cord.append(450)
                    # Checking column H

                    if (pos_x > 450) and (pos_x < 500):
                        if (pos_y > 100) and (pos_y < 150):
                            selections.append('h8')
                            cord.append(450)
                            cord.append(100)
                        elif (pos_y > 150) and (pos_y < 200):
                            selections.append('h7')
                            cord.append(450)
                            cord.append(150)
                        elif (pos_y > 200) and (pos_y < 250):
                            selections.append('h6')
                            cord.append(450)
                            cord.append(200)
                        elif (pos_y > 250) and (pos_y < 300):
                            selections.append('h5')
                            cord.append(450)
                            cord.append(250)
                        elif (pos_y > 300) and (pos_y < 350):
                            selections.append('h4')
                            cord.append(450)
                            cord.append(300)
                        elif (pos_y > 350) and (pos_y < 400):
                            selections.append('h3')
                            cord.append(450)
                            cord.append(350)
                        elif (pos_y > 400) and (pos_y < 450):
                            selections.append('h2')
                            cord.append(450)
                            cord.append(400)
                        elif (pos_y > 450):
                            selections.append ('h1')
                            cord.append(450)
                            cord.append(450)
            
            if len(selections) == 1:
                if ind == True:
                    print('cause')
                    display.indication(cord)
                    ind = False
                    

                    
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
            display.message(turn, piece, start_pos, end_pos)
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
        """ Main function """
        #checking if the user wishes to watch a game against two AIs or wishes to play
        self.player1 = input("Enter 1 for AI or 2 for self play: ")
        self.playerc = 'Black'
        if self.player1 == '1':
            self.mode = "A"
            self.option = False
        elif self.player1 == '2':
            self.mode = "B"
            self.option = True
            self.moves = []
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
                display.update(game_board.fen())
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
if __name__ == "__main__":
    player1 = 0
    player2 = 1
    game_1=Game(player1, player2)
    game_1.play_game()

    



