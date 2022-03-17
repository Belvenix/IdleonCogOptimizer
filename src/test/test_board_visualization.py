from ..python.board import Board
from ..python.cogs import Cog, Player
from ..python.special_cogs import *
import numpy as np

def test_correct_visualization_empty():
    board = Board(height=4, width=6, locked=False)
    board.print_board()
    expected =  '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n'
    print(repr(board._visualization_board))
    assert board._visualization_board == expected

def test_correct_visualization_multiple_cogs_locked():
    board = Board(height=4, width=6)
    board.place(0, 1, Cog())
    board.place(3, 1, Cog())
    board.print_board()
    expected =  '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n'
    print(repr(board._visualization_board))
    assert board._visualization_board == expected

def test_correct_visualization_multiple_cogs_unlocked():
    board = Board(height=4, width=6, locked=False)
    board.place(0, 1, Cog())
    board.place(3, 1, Cog())
    board.print_board()
    expected =  '.\t.\t.\t.\t.\t.\n' + \
                'c\t.\t.\tc\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n'
    print(repr(board._visualization_board))
    assert board._visualization_board == expected

def test_correct_visualization_multiple_cog_types():
    board = Board(height=4, width=6, locked=False)
    board.place(0, 1, Cog())
    board.place(3, 1, Adjay())
    board.place(0, 2, Diggle())
    board.place(0, 3, Uppy())
    board.place(1, 0, Downer())
    board.place(2, 1, Leff())
    board.place(3, 4, Rite())
    board.place(1, 2, Rowow())
    board.place(2, 5, Collumm())
    board.place(3, 2, Omni())
    board.print_board()
    expected =  '.\tv\t.\t.\t.\t.\n' +\
                'c\t.\t<\t+\t.\t.\n' +\
                'x\t=\t.\t#\t.\t.\n' +\
                '^\t.\t.\t.\t.\t.\n'
    print(repr(board._visualization_board))
    assert board._visualization_board == expected

def test_correct_visualization_partially_unlocked():
    board = Board(height=4, width=6)
    mask = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ])
    board.unlock(mask)
    board.place(0, 1, Cog())
    board.place(2, 1, Cog())
    board.place(3, 2, Cog())
    board.print_board()
    expected =  '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\tc\t.\t.\t.\n' + \
                '.\t.\t.\tc\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n'
    print(repr(board._visualization_board))
    assert board._visualization_board == expected

def test_correct_visualization_player_unlocked():
    board = Board(height=4, width=6, locked=False)
    board.place(0, 2, Player("test"))
    board.print_board()
    expected =  '.\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n' + \
                'p\t.\t.\t.\t.\t.\n' + \
                '.\t.\t.\t.\t.\t.\n'
    print(repr(board._visualization_board))
    assert board._visualization_board == expected

