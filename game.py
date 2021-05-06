import chess
import pygame
import random
import time
from IPython.display import display, HTML, clear_output
from chessboard import display

# board class tracks whose turn it is, possbile moves, and history
# also it is possibble to undo and redo moves and tracks repeating states
#pygame.display.set_caption("Chess Game")

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
        display.update(game_board.fen())
        uci = self.get_move("%s's move [q to quite]> " % self.who(game_board.turn))
        legal_uci_moves = [move.uci() for move in game_board.legal_moves]
        while uci not in legal_uci_moves:
            print("Legal moves: " + (",".join(sorted(legal_uci_moves))))
            uci = self.get_move("%s's move[q to quit]> " % self.who(game_board.turn))
        return uci

    def get_move(self, prompt):
        uci = input(prompt)
        if uci and uci[0] == "q":
            raise KeyboardInterrupt()
        try:
            chess.Move.from_uci(uci)
        except:
            uci = None
        return uci

    def random_player(self, game_board):
        ai_move = random.choice(list(game_board.legal_moves))
        move = str(ai_move)
        start_pos, end_pos = move[::2], move[1::2]
        print(start_pos, end_pos)
        #print(move)
        #square = chess.parse_square('e4')
        #print(square)
        if chess.BaseBoard():
            piece = chess.BaseBoard.piece_at(chess.BaseBoard(),1)   # Working on displaying the peice that was moved wants self to be passed through but that causes error
            print(piece)
        return ai_move.uci()
        

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
            msg = "check: " + who(not game_board.turn)
            print(msg)
        if game_board.is_checkmate():
            msg = "checkmate: " + who(not game_board.turn) + " wins!"
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


