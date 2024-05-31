import re
import sys

from Core.CoreException import CoreException


class Keypress:
    def __init__(self, str_repr: str):
        if re.fullmatch("[10]{16}", str_repr) is None:
            raise CoreException("Keypress has to be 16 bits as string")
        self.__str_repr = str_repr

    def get_str_repr(self) -> str:
        return self.__str_repr

    def get_int_repr(self) -> int:
        return int(self.__str_repr, 2)

    def get_bytes_repr(self) -> bytes:
        return bytes([int(self.__str_repr[:8], 2), int(self.__str_repr[8:], 2)])

