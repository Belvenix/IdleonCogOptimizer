import numpy as np

from ..python.board import Board
from ..python.cogs import Cog, Player
from ..python.special_cogs import *

def test_initialize():
    board = Board()
    assert board.board.shape == (8, 12), "Default board shape should be (8, 12)!"
    assert board.get_totals() == (0,0,0), "Total values should be equal to 0!"
    assert len(board.storage) == 0, "Cog storage should be empty, when initialized!"
    assert np.array_equal(board.mask, np.zeros((8,12))), "Default mask shape should be (8, 12) and all values should equal to 0!"

def test_validate_success_default_board_correct_coordinates_unlocked():
    board = Board()
    unlocked_places = np.zeros((8,12))
    unlocked_places[4,4] = 1
    board.unlock(unlocked_places)
    assert board.validate(4, 4), "Board(4,4) should be valid and unlocked!"

def test_validate_fail_default_board_correct_coordinates_locked():
    board = Board()
    assert not board.validate(4, 4), "Board(4,4) should be valid, but locked!"

def test_validate_fail_default_board_incorrect_coordinates_unlocked():
    board = Board(locked=False)
    assert not board.validate(9, 9), "Board(9,9) should be invalid, but unlocked!"

def test_validate_success_changed_board_correct_coordinates_unlocked():
    board = Board(20, 40, locked=False)
    assert not board.validate(15, 30), "Board(15,30) should be valid and unlocked!"

def test_validate_success_changed_board_correct_coordinates_unlocked():
    board = Board(40, 20, locked=False)
    assert not board.validate(30, 15), "Board(30,15) should be valid and unlocked!"

def test_calculation_no_boosting_single():
    board = Board(locked=False)
    board.place(4, 4, Cog(50, 40, 30))
    expected = (50, 40, 30)
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_no_boosting_multiple():
    board = Board(locked=False)
    board.place(4, 4, Cog(50, 40, 30))
    board.place(4, 5, Cog(30, 20, 10))
    expected = (50 + 30, 40 + 20, 30 + 10)
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_no_boosting_player():
    board = Board(locked=False)
    board.place(4, 4, Player('Test', 100, 100, 100))
    expected = (100, 100, 0)
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_with_boosting_adjay_multiple():
    board = Board(locked=False)
    board.place(5, 5, Cog(300, 200, 100))
    board.place(3, 5, Cog(30, 20, 10))
    board.place(4, 6, Cog(50, 50, 50))
    board.place(4, 4, Cog(10, 30, 20))
    board.place(3, 4, Cog(4,3,2))
    board.place(4, 5, Adjay(10, 20, 30, b_mult=1.5, f_mult=2, e_mult=2.5))
    expected = (
        300 * 1.5   + 30 * 1.5  + 50 * 1.5  + 10 * 1.5  + 4     + 10,
        200 * 2     + 20 * 2    + 50 * 2    + 30 * 2    + 3     + 20,
        100 * 1     + 10 * 1    + 50 * 1    + 20 * 1    + 2     + 30
    )
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_with_boosting_diggle_multiple():
    board = Board(locked=False)
    board.place(3, 4, Cog(100, 300, 200))
    board.place(3, 5, Cog(30, 20, 10))
    board.place(4, 5, Diggle(25, 33, 17, b_mult=2, f_mult=2.5, e_mult=1.5))
    expected = (
        100 * 2     + 30 * 1    + 25 * 1,
        300 * 2.5   + 20 * 1    + 33 * 1,
        200 * 1     + 10 * 1    + 17 * 1
    )
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_with_boosting_uppy_multiple():
    board = Board(locked=False)
    board.place(4, 7, Cog(100, 300, 200))
    board.place(4, 3, Cog(30, 20, 10))
    board.place(4, 5, Uppy(11, 24, 7, b_mult=2.5, f_mult=1.5, e_mult=2))
    expected = (
        100 * 1     + 30 * 2.5  + 11 * 1,
        300 * 1     + 20 * 1.5  + 24 * 1,
        200 * 1     + 10 * 1    + 7 * 1
    )
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_with_boosting_downer_multiple():
    board = Board(locked=False)
    board.place(5, 6, Cog(100, 300, 200))
    board.place(4, 4, Cog(30, 20, 10))
    board.place(4, 5, Downer(12, 25, 8, b_mult=2.5, f_mult=1.5, e_mult=2))
    board.calculate_board()
    assert board.get_totals() == (292, 495, 218)

def test_calculation_with_boosting_leff_multiple():
    board = Board(locked=False)
    board.place(6, 4, Cog(200, 100, 300))
    board.place(2, 6, Cog(50, 40, 60))
    board.place(4, 5, Leff(12, 23, 1, b_mult=1.5, f_mult=1.25, e_mult=2))
    board.calculate_board()
    assert board.get_totals() == (287, 173, 361)

def test_calculation_with_boosting_rite_multiple():
    board = Board(locked=False)
    board.place(6, 5, Cog(200, 100, 300))
    board.place(2, 5, Cog(30, 20, 10))
    board.place(4, 5, Rite(12, 25, 8, b_mult=2, f_mult=3, e_mult=4))
    board.calculate_board()
    assert board.get_totals() == (442, 345, 318)

def test_calculation_with_boosting_rowow_multiple():
    board = Board(locked=False)
    board.place(0, 5, Cog(100, 300, 200))
    board.place(4, 0, Cog(30, 20, 10))
    board.place(4, 5, Rowow(13, 24, 1, b_mult=2.5, f_mult=1.5, e_mult=2))
    expected = (
        100 * 2.5   + 30 * 1    + 13 * 1,
        300 * 1.5   + 20 * 1    + 24 * 1,
        200 * 1     + 10 * 1    + 1 * 1
    )
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_with_boosting_collum_multiple():
    board = Board(locked=False)
    board.place(0, 5, Cog(200, 100, 300))
    board.place(4, 0, Cog(50, 40, 60))
    board.place(4, 5, Collumm(14, 24, 1, b_mult=1.5, f_mult=1.25, e_mult=2))
    expected = (
        200 * 1 + 50 * 1.5  + 14 * 1,
        100 * 1 + 40 * 1.25 + 24 * 1,
        300 * 1 + 60 * 1    + 1 * 1
    )
    board.calculate_board()
    assert board.get_totals() == expected

def test_calculation_with_boosting_omni_multiple():
    board = Board(locked=False)
    board.place(6, 7, Cog(80, 80, 80))
    board.place(3, 6, Cog(100, 100, 100))
    board.place(4, 5, Omni(12, 25, 8, b_mult=2, f_mult=3, e_mult=4))
    expected = (
        80 * 2  + 100 * 1   + 12 * 1,
        80 * 3  + 100 * 1   + 25 * 1,
        80 * 1  + 100 * 1   + 8 * 1
    )
    board.calculate_board()
    assert board.get_totals() == expected

def test_put_cog_in_storage():
    board = Board(locked=False)
    board.place(4, 4, Cog(80, 80, 80))
    board.place(4, 4, Cog(100, 100, 100))
    assert len(board.storage) == 1
    assert board.storage[0].get_values() == (80, 80, 80)

def test_dont_put_empty_cog_in_storage():
    board = Board(locked=False)
    board.place(4, 4)
    board.place(4, 4, Cog(80, 80, 80))
    board.place(4, 5, Cog(100, 100, 100))
    assert len(board.storage) == 0

def test_reset_puts_all_zeros():
    board = Board(locked=False)
    board.place(4, 4, Cog(50, 40, 30))
    board.place(4, 5, Cog(30, 20, 10))
    board.calculate_board()
    board.reset_board_values()
    assert board.get_totals() == (0, 0, 0)

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