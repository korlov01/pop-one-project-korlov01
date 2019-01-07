import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, _, _, _, _],
            [_, _, _, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases
    assert at((2, 2)) == M
    assert at((3, 3)) == R

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    #eventually add some board2 and at least 3 tests with it
    set_board(board2)
    assert at((0, 3)) == _
    assert at((1, 2)) == _
    assert at((3, 3)) == R

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board
    set_board(board2)
    assert board2 == get_board()

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
        string_to_location('T68')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs
    with pytest.raises(ValueError):
        string_to_location('$:^')
    assert string_to_location('A2') == (0, 1)
    assert string_to_location('D4') == (3, 3)

def test_location_to_string():
    with pytest.raises(ValueError):
    # Replace with tests
        location_to_string((6,6))
        location_to_string((2,6))
    assert location_to_string((0,0)) == 'A1'
    assert location_to_string((4,4)) == 'E5'

def test_at():
    # Replace with tests
    set_board(board1)
    with pytest.raises(ValueError):
        at((7, 8))
        at((1, 35))
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((2, 2)) == M
    

def test_all_locations():
    # Replace with tests
    allocations = []
    for i in range (0,5):
        for j in range (0,5):
            allocations.append((i,j))
    assert test_all_locations() == allocations


def test_adjacent_location():
    # Replace with tests
    with pytest.raises(ValueError):
        adjacent_location((1,0),up)
        adjacent_location((4,2),down)
        adjacent_location((0,0),left)
        adjacent_location((0,4),right)
    assert adjacent_location((0,0),right) == (0,1)
    assert adjacent_location((1,2),down) == (2,2)
    assert adjacent_location((4,3),left) == (4,2)
    assert adjacent_location((3,3),up) == (2,3)
    
def test_is_legal_move_by_musketeer():
    # Replace with tests
    with pytest.raises(ValueError):
        at(location) != 'M'
    set_board(board1)
    assert is_legal_move_by_musketeer((0,3),down) == False
    assert is_legal_move_by_musketeer((1,3),left) == True
    assert is_legal_move_by_musketeer((2,2),right) == True
    
def test_is_legal_move_by_enemy():
    # Replace with tests
    with pytest.raises(ValueError):
        at(location) != 'R'
    set_board(board1)
    assert is_legal_move_by_enemy((1,2),right) == False
    assert is_legal_move_by_enemy((1,2),left) == True
    assert is_legal_move_by_enemy((3,1),up) == False

def test_is_legal_move():
    # Replace with tests

def test_can_move_piece_at():
    # Replace with tests

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    # Replace with tests

def test_is_legal_location():
    # Replace with tests

def test_is_within_board():
    # Replace with tests

def test_all_possible_moves_for():
    # Replace with tests
    
def test_make_move():
    # Replace with tests
    
def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    # Replace with tests


