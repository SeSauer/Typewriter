import serial
from Core.Keypress import Keypress


class Connector:
    def __init__(self, device: str, baudrate: int = 9600):
        self.__serial = serial.Serial(device, baudrate, timeout=None)
        print(f"Connected to serial port '{device}'")

    def write_letter(self, keypress: Keypress):
        self.__serial.write(keypress.get_bytes_repr())
        print(f"Printed letter {keypress.get_str_repr()}")

    def read_and_block(self, length=1, log: bool = True):
        output = str(self.__serial.read(length))
        if log:
            print(output)
