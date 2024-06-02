import serial
from Core.Keypress import Keypress
import Utils.Utils as Utils


class Connector:
    def __init__(self, device: str, baudrate: int = 9600):
        self.__serial = serial.Serial(device, baudrate, timeout=5)
        Utils.log(f"Connected to serial port '{device}'", color=Utils.Colors.OKGREEN)

    def write_letter(self, keypress: Keypress):
        self.__serial.write(keypress.get_bytes_repr())
        Utils.log(f"Printed letter {keypress.get_str_repr()}",1)

    def read_and_block(self, length=1, log: bool = True):
        output = str(self.__serial.read(length))
        if output == "": raise ConnectionError("Serial response timed out")
        if log:
            Utils.log(output, 2)
