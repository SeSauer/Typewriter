import sys
import time
from multiprocessing import Queue
from Printer.PrinterThread import PrinterThread
from Utils.Utils import add_newlines_to_string

DEVICE: str = "COM10"
BAUDRATE: int = 9600

STRING_TO_PRINT: str = "Hello World!"

class App:
    def __init__(self):
        self.__printer_queue = Queue()
        self.__printer_thread = PrinterThread(DEVICE, BAUDRATE, self.__printer_queue)

    def run(self) -> int:
        time.sleep(3)

        self.__printer_thread.start()
        self.__printer_queue.put(add_newlines_to_string(STRING_TO_PRINT))
        while self.__printer_thread.has_work():
            pass
        self.__printer_thread.stop()

        return 0


if __name__ == "__main__":
    app = App()
    exit_code = app.run()
    sys.exit(exit_code)