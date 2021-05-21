import pytest
from game import Game


@pytest.fixture
def game_1():
    player_one = 1
    player_two = 0
    gm = Game(player_one, player_two)
    return gm


def test_constructor(game_1):
    assert hasattr(game_1, "player1")
    assert hasattr(game_1, "player2")
    assert hasattr(game_1, "option")
    assert hasattr(game_1, "mode")


def test_constructor_values():
    with pytest.raises(TypeError):
        Game("player_1", 0)

    with pytest.raises(TypeError):
        Game(1, "player_2")
    

def test_modes(game_1):
    if game_1.mode == "A":
        assert game_1.player1 == "1"
    elif game_1.mode == "B":
        assert game_1.player1 == "2"

    assert game_1.player2 == 0


def test_option(game_1):
    if game_1.mode == "A":
        assert game_1.option == False
    elif game_1.mode == "B":
        assert game_1.option == False


def test_user(game_1):
    assert hasattr(game_1, "user")
    


def test_get_move(game_1):
    assert hasattr(game_1, "get_move")
   


def test_random_player(game_1):
    assert hasattr(game_1, "random_player")
   

def test_move_txt(game_1):
    assert hasattr(game_1, "move_txt")


def test_who(game_1):
    assert hasattr(game_1, "who")
   


def test_view_game(game_1):
    assert hasattr(game_1, "view_game")
   



# def test_play_game(game_1):
#     assert hasattr(game_1, "play_game")