# -*- coding: utf-8 -*-
"""
author: Yotam Levit
project: DataBase Readers and Writers sync
"""
import threading
import multiprocessing


class Sync:
    """
    the sync class
    """
    def __init__(self, processes):
        """
        class initializer
        ;processes: if the sync should be for processes
        or for threads
        the initializer creates lock and a semaphore
        """
        self.lock = None
        self.semaphore = None
        if not processes:
            self.semaphore = threading.BoundedSemaphore(10)
            self.lock = threading.Lock()
        else:
            self.semaphore = multiprocessing.BoundedSemaphore(10)
            self.lock = multiprocessing.Lock()

    def lock_release(self):
        """
        releases the lock
        """
        self.lock.release()

    def lock_acquire(self):
        """
        acquire the lock
        """
        self.lock.acquire()

    def semaphore_acquire(self):
        """
        acquire the semaphore
        """
        self.semaphore.acquire()

    def semaphore_release(self):
        """
        releases the semaphore
        """
        self.semaphore.release()