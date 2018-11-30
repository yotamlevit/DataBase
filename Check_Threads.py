# -*- coding: utf-8 -*-
import threading
import logging
import time
from File_Sync import *
logging.basicConfig(filename='logging.log',level=logging.DEBUG, format='(%(threadName) -10s) %(asctime)s %(levelname)-8s %(message)s')

def worker(action, args):
    logging.debug('starting - ' + 'args: ' + str(args))
    data = File_Sync(False)
    if action is 'set':
        print data.set_value(args[0], args[1])
    elif action is 'get':
        print data.get_value(args)
    elif action is 'delete':
        print data.delete_value(args)
    time.sleep(2)
    logging.debug('Exiting')


class Check_Threads:
    def __init__(self):
        self.threads = []
        self.action = []
        self.args = []

    def check_3(self):
        self.threads = []
        self.action = ['set', 'get', 'set']
        self.args = [(1, 'a'), 1, (2, 'b')]
        for i in range(10):
            t = threading.Thread(target=worker, name='Thread-' + str(i), args=(self.action[i], self.args[i]))
            self.threads.append(t)
            t.start()

    def check_3333333333(self):
        File_serialization.erase_data()
        self.threads = []
        self.action = ['set', 'get', 'set']
        self.args = [(1, 'a'), 1, (2, 'b')]
        for i in range(3):
            t = threading.Thread(target=worker, name='Thread-' + str(i), args=(self.action[i], self.args[i]))
            self.threads.append(t)
            t.start()

    def check_2(self):
        self.threads = []
        self.action = ['get', 'get', 'get', 'get']
        self.args = [1, 2, 3, 4]
        for i in range(4):
            t = threading.Thread(target=worker, name='Thread-' + str(i), args=(self.action[i], self.args[i]))
            self.threads.append(t)
            t.start()

    def check_1(self):
        File_serialization.erase_data()
        self.threads = []
        self.action = ['set', 'set', 'set', 'set']
        self.args = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
        for i in range(4):
            t = threading.Thread(target=worker, name='Thread-' + str(i), args=(self.action[i], self.args[i]))
            self.threads.append(t)
            t.start()
            time.sleep(0.05)
        time.sleep(0.25)
        print "THe databse is:"
        File_serialization.data()

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()