# -*- coding: utf-8 -*-
"""
author: Yotam Levit
project: DataBase Readers and Writers sync
"""
from Sync import *
from Service_Func import *


def thread_final_check(sync):
    """
    runing the final testing with 30 threads
    ;sync: the lock and the semaphores
    """
    thread_fill(sync)
    time.sleep(5)
    threads = []
    action = ['set', 'get', 'get', 'get', 'get', 'get', 'get', 'get', 'get',
              'get', 'set', 'set', 'get', 'get', 'get', 'get', 'get', 'get',
              'get', 'get', 'get', 'set', 'get', 'get', 'get', 'get', 'get',
              'get', 'get', 'get', 'get']
    args = [(5, 'e'), 1, 2, 3, 4, 1, 2, 3, 4, 5, (6, 'f'), (7, 'g'), 1, 2, 3,
            4, 5, 6, 7, 3, 4, (8, 'h'), 1, 2, 3, 4, 5, 6, 7, 8, 1]
    for i in range(len(args)):
        t = threading.Thread(target=worker, name='Thread-' + str(i),
                             args=(sync, action[i], args[i]))
        threads.append(t)
        t.start()
    time.sleep(0.5)
    print "THe databse is:"
    File_serialization.data()


def thread_fill(sync):
    """
    fill the database with 4 values
    ;sync: the lock and the semaphores
    """
    File_serialization.erase_data()
    threads = []
    action = ['set', 'set', 'set', 'set']
    args = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    for i in range(4):
        t = threading.Thread(target=worker, name='Thread-' + str(i+1),
                             args=(sync, action[i], args[i]))
        threads.append(t)
    for i in range(4):
        threads[i].start()
    time.sleep(5)
    print "THe databse is:"
    File_serialization.data()


