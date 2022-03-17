from typing import Tuple
from .cogs import Cog, EmptyCog, Player
from .special_cogs import BoostedCog
import numpy as np

class Board:
    def __init__(self, height: int = 8, width: int = 12, locked: bool = True) -> None:
        self._visualization_board = ''
        self.board = np.array([[EmptyCog() for w in range(width)] for h in range(height)])
        if locked:
            self.mask = np.zeros_like(self.board)
        else:
            self.mask = np.ones_like(self.board)
        self.storage = []
        self.total_build = 0
        self.total_flaggy = 0
        self.total_exp = 0

    def unlock(self, mask: np.array):
        assert mask.shape == self.board.shape, "Mask shape is different than board shape!"
        self.mask = mask
        
    def empty(self) -> bool:
        for cog in self.board.flatten():
            if not isinstance(cog, EmptyCog):
                return False
        return True

    def place(self, x:int, y:int, cog: Cog = EmptyCog()) -> None:
        if self.validate(x, y):
            assert isinstance(cog, Cog), "You can't place non-cogs on board!"
            if not isinstance(self.board[y, x], EmptyCog):
                self.storage.append(self.board[y, x])
            self.board[y,x] = cog
        
    def clear(self):
        self.reset_board_values()
        for x in range(self.board.shape[1]):
            for y in range(self.board.shape[0]):
                self.place(x, y, EmptyCog())

    def reset_board_values(self):
        self.total_build = 0
        self.total_flaggy = 0
        self.total_exp = 0

    def validate(self, x, y) -> bool:
        return (x >= 0 and y >= 0 and x < self.board.shape[1] and y < self.board.shape[0]) and (self.mask[y, x])

    def get_totals(self) -> Tuple[int, int, int]:
        return self.total_build, self.total_flaggy, self.total_exp

    def calculate_board(self):
        self.reset_loop()
        self.multiply_loop()
        self.sum_loop()

    def reset_loop(self):
        self.reset_board_values()
        for c in self.board.flatten():
            c.reset()

    def multiply_loop(self):
        for x in range(self.board.shape[1]):
            for y in range(self.board.shape[0]):
                if self.validate(x, y):
                    c = self.board[y, x]
                    if isinstance(c, BoostedCog):
                        boosted_coordinates, boosted_values = c.boosted()
                        for bc in boosted_coordinates:
                            dx, dy = bc[0], bc[1]
                            
                            if self.validate(x+dx, y+dy):
                                boosted_cog = self.board[y+dy, x+dx]
                                boosted_cog.apply_boost(*boosted_values)
                                self.board[y+dy, x+dx] = boosted_cog
                                
    def sum_loop(self):
        for x in range(self.board.shape[1]):
            for y in range(self.board.shape[0]):
                if self.validate(x, y):
                    c = self.board[y, x]
                    self.total_build +=c.get_values()[0]
                    self.total_flaggy += c.get_values()[1]
                    self.total_exp += c.get_values()[2]

    def show(self):
        self.print_rates()
        self.print_board()
        self.print_storage()
        self.print_players_info()

    def print_rates(self):
        print("Total build rate: " + str(self.total_build) + '\n' +
            "Total flaggy rate: " + str(self.total_flaggy) + '\n' +
            "Total extra exp: " + str(self.total_exp))

    def print_board(self):
        board_print = ''
        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[1]):
                board_print += str(self.board[y, x]) + '\t'
            board_print = board_print[:-1] + '\n'
        self._visualization_board = board_print
        print(self._visualization_board)
        
    def print_storage(self):
        storage_print = 'In storage: '
        for s in self.storage:
            storage_print += str(s) + ', '
        print(storage_print)

    def print_players_info(self):
        print('Player stats:')
        for c in self.board.flatten():
            if isinstance(c, Player):
                print(c.info())