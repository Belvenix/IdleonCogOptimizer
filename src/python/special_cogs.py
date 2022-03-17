from typing import List, Tuple, Union

from .cogs import Cog

class BoostedCog(Cog):
    def __init__(self, build: int = 0, flaggy: int = 0, exp: int = 0, b_mult: int = 1, f_mult: int = 1, e_mult: int = 1) -> None:
        super().__init__(build, flaggy, exp)
        self.b_mult = b_mult
        self.f_mult = f_mult
        self.e_mult = e_mult


    def boosted(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern with given values"""
        return self._boosted_cogs_relative_coordinates(), (self.b_mult, self.f_mult, self.e_mult)
    
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern."""
        return []

class Adjay(BoostedCog):
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            0   0   0   0   0
            0   0   1   0   0
            0   1   x   1   0
            0   0   1   0   0
            0   0   0   0   0
            
        """
        return [
            ( 0,   -1),
            (-1,    0),
            ( 1,    0),
            ( 0,    1)
            ]

    def __str__(self) -> str:
        return '+'

class Diggle(BoostedCog):
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            0   0   0   0   0
            0   1   0   1   0
            0   0   x   0   0
            0   1   0   1   0
            0   0   0   0   0
            
        """
        return [
            (-1,   -1),
            (-1,    1),
            ( 1,   -1),
            ( 1,    1)
            ]

    def __str__(self) -> str:
        return 'x'

class Uppy(BoostedCog):
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            0   1   1   1   0
            0   1   1   1   0
            0   0   x   0   0
            0   0   0   0   0
            0   0   0   0   0

        """
        return [
            (-1,   -2),
            ( 0,   -2),
            ( 1,   -2),
            (-1,   -1),
            ( 0,   -1),
            ( 1,   -1)
            ]
    
    def __str__(self) -> str:
        return '^'

class Downer(BoostedCog):
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            0   0   0   0   0
            0   0   0   0   0
            0   0   x   0   0
            0   1   1   1   0
            0   1   1   1   0

        """
        return [
            (-1,    2),
            ( 0,    2),
            ( 1,    2),
            (-1,    1),
            ( 0,    1),
            ( 1,    1)
            ]

    def __str__(self) -> str:
        return 'v'

class Leff(BoostedCog):
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            0   0   0   0   0
            1   1   0   0   0
            1   1   x   0   0
            1   1   0   0   0
            0   0   0   0   0

        """
        return [
            (-2,   -1),
            (-2,    0),
            (-2,    1),
            (-1,   -1),
            (-1,    0),
            (-1,    1)
            ]
    def __str__(self) -> str:
        return '<'

class Rite(BoostedCog):
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            0   0   0   0   0
            0   0   0   1   1
            0   0   x   1   1
            0   0   0   1   1
            0   0   0   0   0

        """
        return [
            ( 2,   -1),
            ( 2,    0),
            ( 2,    1),
            ( 1,   -1),
            ( 1,    0),
            ( 1,    1)
            ]
    def __str__(self) -> str:
        return '>'

class Rowow(BoostedCog):
    def __init__(self, build: int = 0, flaggy: int = 0, exp: int = 0, b_mult: int = 1, f_mult: int = 1, e_mult: int = 1, board_width: int = 12) -> None:
        super().__init__(build, flaggy, exp, b_mult, f_mult, e_mult)
        self.board_width = board_width

    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            0   0   0   0   0
            0   0   0   0   0
            <   1   x   1   >
            0   0   0   0   0
            0   0   0   0   0

        """
        return [(i, 0) for i in range(-(self.board_width - 1), self.board_width) if i != 0]
    def __str__(self) -> str:
        return '='

class Collumm(BoostedCog):
    def __init__(self, build: int = 0, flaggy: int = 0, exp: int = 0, b_mult: int = 1, f_mult: int = 1, e_mult: int = 1, board_height: int = 8) -> None:
        super().__init__(build, flaggy, exp, b_mult, f_mult, e_mult)
        self.board_height = board_height

    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.

            0   0   ^   0   0
            0   0   1   0   0
            0   0   x   0   0
            0   0   1   0   0
            0   0   v   0   0

        """
        return [(0, i) for i in range(-(self.board_height - 1), self.board_height) if i != 0]
    def __str__(self) -> str:
        return '|'

class Omni(BoostedCog):
    def _boosted_cogs_relative_coordinates(self) -> List[Tuple[Union[int, slice], Union[int, slice]]]:
        """ Boost efficiency in pattern.
        
            1   0   0   0   1
            0   0   0   0   0
            0   0   x   0   0
            0   0   0   0   0
            1   0   0   0   1
            
        """
        return [
            (-2,   -2),
            (-2,    2),
            ( 2,   -2),
            ( 2,    2)
            ]
    def __str__(self) -> str:
        return '#'
