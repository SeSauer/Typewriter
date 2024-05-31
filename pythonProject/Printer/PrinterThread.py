from Printer.Printer import Printer
from multiprocessing import Queue
import threading
import time


class PrinterThread():
    def __init__(self, device: str, baudrate: int, printer_queue: "Queue[str]") -> None:
        self.__printer = Printer(device, baudrate)
        self.__thread = threading.Thread(target=self.__run, name="PrinterThread")
        self.__shutdown_event = threading.Event()
        self.__time_of_last_job: float = time.time()
        self.__time_lock: threading.Lock = threading.Lock()
        self.__printer_queue: "Queue[str]" = printer_queue

    def __run(self) -> None:
        while not self.__shutdown_event.is_set():
            if not self.__printer_queue.empty():
                with self.__time_lock:
                    self.time_since_last_job: float = time.time()
                string_to_print: str = self.__printer_queue.get(block=False)
                self.__printer.print(string_to_print)

    def has_work(self) -> bool:
        with self.__time_lock:
            return time.time() - self.__time_of_last_job < 5


    def start(self) -> None:
        self.__shutdown_event.clear()
        self.__thread.start()
        print("[PrinterThread] Started")

    def stop(self) -> None:
        self.__shutdown_event.set()
        self.__thread.join()
        print("[PrinterThread] Stopped")