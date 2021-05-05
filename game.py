import chess
import pygame
import random
import time
from IPython.display import display, HTML, clear_output
from chessboard import display

# board class tracks whose turn it is, possbile moves, and history
# also it is possibble to undo and redo moves and tracks repeating states
#pygame.display.set_caption("Chess Game")

def user(game_board):
    display.update(game_board.fen())
    uci = get_move("%s's move [q to quite]> " % who(game_board.turn))
    legal_uci_moves = [move.uci() for move in game_board.legal_moves]
    while uci not in legal_uci_moves:
        print("Legal moves: " + (",".join(sorted(legal_uci_moves))))
        uci = get_move("%s's move[q to quit]> " % who(game_board.turn))
    return uci

def get_move(prompt):
    uci = input(prompt)
    if uci and uci[0] == "q":
        raise KeyboardInterrupt()
    try:
        chess.Move.from_uci(uci)
    except:
        uci = None
    return uci

def random_player(game_board):
    move = random.choice(list(game_board.legal_moves))
    # if chess.BaseBoard():
    #     chess.BaseBoard.piece_at("f7")   # Working on displaying the peice that was moved wants self to be passed through but that causes error
    print("AI Move: ",move)
    return move.uci()

def who(player):
    """ function for displaying the color of a player """
    return "White" if player == chess.WHITE else "Black"

def view_game(game_board, use_display):
    """ function for displaying the board """
    # if bool(game_board.castling_rights):
    #     print("you can castle: BBH1")
    return display.update(game_board.fen())

def play_game(player1, player2, pause=0.1):
    game_board = chess.Board()
    use_display = display.start(game_board.fen())
    try:
        while not game_board.is_game_over(claim_draw=True):
            if game_board.turn == chess.WHITE:
                uci = player1(game_board)
            else:
                uci = player2(game_board)
            name = who(game_board.turn)
            game_board.push_uci(uci)
            board_stop = view_game(game_board, use_display)
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
play_game(user, random_player)


