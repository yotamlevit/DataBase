# -*- coding: utf-8 -*-

from File_Serialization import File_serialization
import threading

class File_Sync(File_serialization):
    def __init__(self, processes):
        super(File_Sync, self).__init__()
        self.lock = None
        self.semaphore = None
        if not processes:
            self.semaphore = threading.BoundedSemaphore(10)
            self.lock = threading.Lock()

    def set_value(self, key, val):
        self.lock.acquire()
        self.lock.locked()
        x = 0
        while x < 10:
            self.semaphore.acquire()
            x+=1
        ans = super(File_Sync, self).set_value(key, val)
        x = 0
        while x < 10:
            self.semaphore.release()
            x+=1
        self.lock.release()
        if ans:
            return "Value was added"
        return "can't add value or key alredy exist"

    def get_value(self, key):
        self.semaphore.acquire()
        val = super(File_Sync, self).get_value(key)
        self.semaphore.release()
        if val != "invalid key":
            return 'the value is - ' + val
        return val

    def delete_value(self, key):
        self.lock.acquire()
        x = 0
        while x < 10:
            self.semaphore.acquire()
        ans = super(File_Sync, self).delete_value(key)
        while x < 10:
            self.semaphore.release()
        self.lock.release()
        return ans


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()