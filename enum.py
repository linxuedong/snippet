from enum import Enum

a = {'NORTH': 0, 'SOUTH': 180, 'EAST': 90}


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return a.get(name) or 0


class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


list(Ordinal)
