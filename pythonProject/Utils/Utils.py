

def add_newlines_to_string(string, max_line_length=75) -> str:
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
