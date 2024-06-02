import time
from multiprocessing import Queue
from Printing.PrinterThread import PrinterThread
from Utils.Formatter import DefaultFormatter, OpenAiFormatter

DEVICE: str = "COM10"
BAUDRATE: int = 9600

class App:
    def __init__(self):
        self.__printer_queue = Queue()
        self.__printer_thread = PrinterThread(DEVICE, BAUDRATE, self.__printer_queue, DefaultFormatter())

    def run(self) -> int:
        time.sleep(3)

        with self.__printer_thread:

            while True:
                to_print = input()
                if to_print == "!exit": break
                self.__printer_queue.put(to_print)

            while self.__printer_thread.has_work():
                pass

        return 0


if __name__ == "__main__":
    app = App()
    exit_code = app.run()
    exit(exit_code)
