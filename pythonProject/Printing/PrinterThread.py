from Printing.Printer import Printer
from Utils.Formatter import BaseFormatter, DefaultFormatter
import Utils.Utils as Utils
from multiprocessing import Queue
import threading
import time


class PrinterThread():
    def __init__(self, device: str, baudrate: int, printer_queue: "Queue[str]", formatter: BaseFormatter) -> None:
        self.__printer = Printer(device, baudrate)
        self.__thread = threading.Thread(target=self.__run, name="PrinterThread")
        self.__shutdown_event = threading.Event()
        self.__time_of_last_job: float = time.time()
        self.__time_lock: threading.Lock = threading.Lock()
        self.__printer_queue: "Queue[str]" = printer_queue
        self.__formatter: BaseFormatter = formatter

    def __run(self) -> None:
        while not self.__shutdown_event.is_set():
            if not self.__printer_queue.empty():
                with self.__time_lock:
                    self.time_since_last_job: float = time.time()
                string_to_print: str = self.__printer_queue.get(block=False)
                self.__printer.print(string_to_print, self.__formatter)

    def has_work(self) -> bool:
        with self.__time_lock:
            return time.time() - self.__time_of_last_job < 5

    def start(self) -> None:
        self.__shutdown_event.clear()
        self.__thread.start()
        Utils.log("[PrinterThread] Started", color=Utils.Colors.OKCYAN)

    def stop(self) -> None:
        self.__shutdown_event.set()
        self.__thread.join()
        Utils.log("[PrinterThread] Stopped", color=Utils.Colors.OKCYAN)

    def __enter__(self) -> None:
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.stop()
        return False
