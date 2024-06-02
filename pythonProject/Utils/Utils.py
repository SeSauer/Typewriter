import sys
from enum import Enum


class Colors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def add_newlines_to_string(string, max_line_length=65) -> str:
    chars_since_newline: int = 0
    out: str = ""
    for i in range(len(string)):
        if string[i] == "\n":
            chars_since_newline = 0
        else:
            chars_since_newline += 1
            if chars_since_newline >= max_line_length:
                out = out + "\n"
                chars_since_newline = 0
        out = out + string[i]
    return out


def log(message: str, level: int = 0, color: Colors=None, max_length=-1) -> None:
    """:parameter message: message to log
    :parameter level: only messages of level < sys.argv[1] will be logged
    :parameter max_length messages will be truncated to this length. -1 means no limit"""
    if level <= (int(sys.argv[1]) if len(sys.argv) > 1 else 0):

        if max_length != -1 and len(message) > max_length:
            message = message[:(max_length-3)] + "..."

        message = message.strip("\n")
        message = message.replace("\n", "\\n")

        if color is not None:
            message = color.value + message + Colors.ENDC.value
        print(message)
