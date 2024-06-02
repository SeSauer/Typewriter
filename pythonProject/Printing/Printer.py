from Printing.Connector import Connector
from Core.Letter import Letter
from Core.KeypressLookup import KeypressLookup
from Utils.Formatter import BaseFormatter
import Utils.Utils as Utils


class Printer:
    def __init__(self, device: str, baudrate: int, keypress_lookup=None) -> None:
        if keypress_lookup is None:
            self.__keypress_lookup = KeypressLookup()
        else:
            self.__keypress_lookup = keypress_lookup
        self.__connector: Connector = Connector(device, baudrate)

    def print(self, string: str, formatter: BaseFormatter) -> None:
        string = formatter.format(string)
        for char in string:
            letter: Letter = Letter(char)
            try:
                keypresses = letter.get_keypresses(self.__keypress_lookup)
            except KeyError:
                Utils.log(f"No keypress found for {letter.get_str_repr()}, Skipping", color=Utils.Colors.WARNING)
                continue
            for keypress in keypresses:
                self.__connector.write_letter(keypress)
                self.__connector.read_and_block(log=False)
        Utils.log(f"Finished printing {string}", max_length=75)

