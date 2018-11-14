# -*- coding: utf-8 -*-

from File_Serialization import File_serialization
import threading
import multiprocessing

class File_Sync(File_serialization):
    def __init__(self, processes):
        if not processes:
            semaphore = threading.BoundedSemaphore(10)

    def a

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()