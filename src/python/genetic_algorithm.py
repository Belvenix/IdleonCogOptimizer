
class Idleon_Genetic_Algorithm:
    """Genetic Algorithm for cogs placement in game Legends of Idleon.

    The way the algorithm works:

        1. You provide it with the possible cogs that you have.
        2. You provide it with the unlocked places on board.
        3. You run it
        4. It initializes population of N Individuals. Each of them has their own cogs placement

    """
    def __init__(self) -> None:
        self.__possible_cogs