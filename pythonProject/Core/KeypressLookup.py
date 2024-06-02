from Core.Keypress import Keypress
from Core.LookupNew import DEFAULT_KEYS
import Utils.Utils as Utils
import re


def is_valid_bitstring(bitstring: str) -> bool:
    input = bitstring.replace(" ", "")
    return re.fullmatch("[01]{16}", input) is not None


class KeypressLookup:
    def __init__(self, lookup_table: dict[str, list[str]] = DEFAULT_KEYS):
        self.lookup_table = lookup_table

    def get_keypresses(self, char: str) -> list[Keypress]:
        out: list[Keypress] = []
        self.add_results_to_list_recursive([char], out)
        return out

    def add_results_to_list_recursive(self, working_list, result_list: list[Keypress]):
        for key in working_list:
            value = self.lookup_table[key]
            if len(value) == 1 and is_valid_bitstring(value[0]):
                result_list.append(Keypress(value[0].replace(" ", "")))
            else:
                self.add_results_to_list_recursive(value, result_list)

if __name__ == "__main__":
    lookup = KeypressLookup()
    get_keypresses = lookup.get_keypresses("A")
    for keypress in get_keypresses:
        Utils.log(keypress.get_str_repr(), 0)
