# -*- coding: utf-8 -*-

from File_Serialization import File_serialization
import threading
import multiprocessing

class File_Sync(File_serialization):
    def __init__(self, processes):
        File_serialization.__init__(self)
        self.lock = None
        self.semaphore = None
        if not processes:
            self.semaphore = threading.BoundedSemaphore(10)
            self.lock = threading.Lock()

    def set_value(self, key, val):
        self.lock.acquire()
        x = 0
        while x < 10:
            self.semaphore.acquire()
        File_serialization.set_value(key, val)
        while x < 10:
            self.semaphore.release()
        self.lock.


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()