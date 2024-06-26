
DEFAULT_KEYS: dict[str, str] = {
    "1": ["0010 0000  1000 0000"],
    "2": ["0010 0000  0100 0000"],
    "3": ["0001 0000  1000 0000"],
    "4": ["0001 0000  0100 0000"],
    "5": ["0000 0100  1000 0000"],
    "6": ["0000 0100  0100 0000"],
    "7": ["0000 1000  1000 0000"],
    "8": ["0000 1000  0100 0000"],
    "9": ["0000 0001  1000 0000"],
    "0": ["0000 0001  0100 0000"],
    "ß": ["0000 0010  1000 0000"],
    "´": ["0000 0010  0100 0000"],
    "q": ["0100 0000  0010 0000"],
    "w": ["0100 0000  0000 1000"],
    "e": ["0010 0000  0010 0000"],
    "r": ["0010 0000  0000 1000"],
    "t": ["0001 0000  0010 0000"],
    "z": ["0001 0000  0000 1000"],
    "u": ["0000 0100  0010 0000"],
    "i": ["0000 0100  0000 1000"],
    "o": ["0000 1000  0010 0000"],
    "p": ["0000 1000  0000 1000"],
    "ü": ["1000 0000  0010 0000"],
    "+": ["1000 0000  0000 1000"],
    "a": ["0100 0000  0000 0100"],
    "s": ["0000 1000  0001 0000"],
    "d": ["0000 1000  0000 0100"],
    "f": ["0010 0000  0001 0000"],
    "g": ["0010 0000  0000 0100"],
    "h": ["0001 0000  0001 0000"],
    "j": ["0001 0000  0000 0100"],
    "k": ["0000 0100  0001 0000"],
    "l": ["0000 0100  0000 0100"],
    "ö": ["1000 0000  0001 0000"],
    "ä": ["1000 0000  0000 0100"],
    "#": ["0100 0000  0100 0000"],
    "y": ["0100 0000  0001 0000"],
    "x": ["0000 0010  0001 0000"],
    "c": ["0000 0001  0001 0000"],
    "v": ["0000 0001  0010 0000"],
    "b": ["0000 0001  0000 1000"],
    "n": ["0000 0010  0010 0000"],
    "m": ["0000 0010  0000 1000"],
    ",": ["1000 0000  1000 0000"],
    ".": ["1000 0000  0100 0000"],
    "-": ["0100 0000  1000 0000"],

    "!": ["CAPS", "1", "SHIFT"],
    "\"": ["CAPS", "2", "SHIFT"],
    "§": ["CAPS", "3", "SHIFT"],
    "$": ["CAPS", "4", "SHIFT"],
    "%": ["CAPS", "5", "SHIFT"],
    "&": ["CAPS", "6", "SHIFT"],
    "/": ["CAPS", "7", "SHIFT"],
    "(": ["CAPS", "8", "SHIFT"],
    ")": ["CAPS", "9", "SHIFT"],
    "=": ["CAPS", "0", "SHIFT"],
    "?": ["CAPS", "ß", "SHIFT"],
    "`": ["CAPS", "´", "SHIFT"],
    "Q": ["CAPS", "q", "SHIFT"],
    "W": ["CAPS", "w", "SHIFT"],
    "E": ["CAPS", "e", "SHIFT"],
    "R": ["CAPS", "r", "SHIFT"],
    "T": ["CAPS", "t", "SHIFT"],
    "Z": ["CAPS", "z", "SHIFT"],
    "U": ["CAPS", "u", "SHIFT"],
    "I": ["CAPS", "i", "SHIFT"],
    "O": ["CAPS", "o", "SHIFT"],
    "P": ["CAPS", "p", "SHIFT"],
    "Ü": ["CAPS", "ü", "SHIFT"],
    "*": ["CAPS", "+", "SHIFT"],
    "A": ["CAPS", "a", "SHIFT"],
    "S": ["CAPS", "s", "SHIFT"],
    "D": ["CAPS", "d", "SHIFT"],
    "F": ["CAPS", "f", "SHIFT"],
    "G": ["CAPS", "g", "SHIFT"],
    "H": ["CAPS", "h", "SHIFT"],
    "J": ["CAPS", "j", "SHIFT"],
    "K": ["CAPS", "k", "SHIFT"],
    "L": ["CAPS", "l", "SHIFT"],
    "Ö": ["CAPS", "ö", "SHIFT"],
    "Ä": ["CAPS", "ä", "SHIFT"],
    "'": ["CAPS", "#", "SHIFT"],
    "Y": ["CAPS", "Y", "SHIFT"],
    "X": ["CAPS", "x", "SHIFT"],
    "C": ["CAPS", "c", "SHIFT"],
    "V": ["CAPS", "v", "SHIFT"],
    "B": ["CAPS", "b", "SHIFT"],
    "N": ["CAPS", "n", "SHIFT"],
    "M": ["CAPS", "m", "SHIFT"],
    ";": ["CAPS", ",", "SHIFT"],
    ":": ["CAPS", ".", "SHIFT"],
    "_": ["CAPS", "-", "SHIFT"],

    "@": ["a", "BACK", "Q"],

    " ": ["1000 0000  0000 0010"],
    "\n": ["0100 0000  0000 0010"],
    "CAPS": ["0100 0000  0000 0001"],
    "SHIFT": ["1000 0000  0000 0001"],
    "BACK": ["0000 0100  0000 0010"]
}