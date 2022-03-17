from typing import List, Tuple, Union

import numpy as np


class Cog:
    def __init__(self, build:int = 0, flaggy:int = 0, exp:int = 0) -> None:
        self.x = None
        self.y = None
        self._base_build = build
        self._base_flaggy = flaggy
        self._base_exp = exp
        self.build = build
        self.flaggy = flaggy
        self.exp = exp

    def reset(self) -> None:
        self.build = self._base_build
        self.flaggy = self._base_flaggy
        self.exp = self._base_exp

    def apply_boost(self, b_mult: float = 1, f_mult: float = 1, e_mult: float = 1) -> None:
        assert b_mult >= 1 and f_mult >= 1 and e_mult >= 1, "Multipliers should be greater or equal one!"
        self.build *= b_mult
        self.flaggy *= f_mult
        self.exp *= 1

    def get_values(self) -> Tuple[int, int, int]:
        return self.build, self.flaggy, self.exp
    
    def __str__(self) -> str:
        return 'c'

    def info(self) -> str:
        return ''.join([self.__str__(), \
            '(bb=', str(self._base_build), \
            ', bf=', str(self._base_flaggy), \
            ', be=', str(self._base_exp), \
            ', b=', str(self.build), \
            ', f=', str(self.flaggy), \
            ', e=', str(self.exp), ')'])

class EmptyCog(Cog):
    def __init__(self) -> None:
        super().__init__(0, 0, 0)

    def apply_boost(self, b_mult: float = 1, f_mult: float = 1, e_mult: float = 1) -> None:
        return None
    
    def __str__(self) -> str:
        return '.'

class Player(Cog):
    def __init__(self, name:str ,build: int = 0, flaggy: int = 0, exp: int = 0) -> None:
        super().__init__(build, flaggy, exp)
        self.name = name

    def apply_boost(self, b_mult: float = 1, f_mult: float = 1, e_mult: float = 1) -> None:
        assert b_mult >= 1 and f_mult >= 1 and e_mult >= 1, "Multipliers should be greater or equal one!"
        self.build *= b_mult
        self.flaggy *= f_mult
        self.exp *= e_mult

    def get_values(self) -> Tuple[int, int, int]:
        return self.build, self.flaggy, 0

    def __str__(self) -> str:
        return 'p'

    def info(self) -> str:
        return ''.join([str(self.name), \
            '(bb=', str(self._base_build), \
            ', bf=', str(self._base_flaggy), \
            ', be=', str(self._base_exp), \
            ', b=', str(self.build), \
            ', f=', str(self.flaggy), \
            ', e=', str(self.exp), ')']) 

