from Core.CoreException import CoreException
from Core.KeypressLookup import KeypressLookup
from Core.Keypress import Keypress


class Letter:

    def __init__(self, char: str):
        if len(char) != 1:
            raise CoreException("Letter has to be a single Char")
        self.__char = char

    def get_str_repr(self):
        return self.__char

    def get_keypresses(self, lookup: KeypressLookup) -> list[Keypress]:
        return lookup.get_keypresses(self.get_str_repr())
    