from Printer.Connector import Connector
from Core.Letter import Letter
from Core.KeypressLookup import KeypressLookup


class Printer:
    def __init__(self, device: str, baudrate: int, keypress_lookup=None) -> None:
        if keypress_lookup is None:
            self.__keypress_lookup = KeypressLookup()
        else:
            self.__keypress_lookup = keypress_lookup
        self.__connector: Connector = Connector(device, baudrate)

    def print(self, string: str) -> None:
        for char in string:
            letter: Letter = Letter(char)
            try:
                keypresses = letter.get_keypresses(self.__keypress_lookup)
            except KeyError:
                print(f"\033[93m No keypress found for {letter.get_str_repr()}, Skipping \033[0m")
                continue
            for keypress in keypresses:
                self.__connector.write_letter(keypress)
                self.__connector.read_and_block(log=False)
        print(f"Finished printing {string}")
