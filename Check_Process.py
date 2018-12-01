# -*- coding: utf-8 -*-
"""
author: Yotam Levit
project: DataBase Readers and Writers sync
"""
from Sync import *
from Service_Func import *


def process_final_check(sync):
    """
    runing the final testing with 30 processes
    ;sync: the lock and the semaphores
    """
    process_fill(sync)
    time.sleep(5)
    process = []
    action = ['set', 'get', 'get', 'get', 'get', 'get', 'get', 'get', 'get',
              'get', 'set', 'set', 'get', 'get', 'get', 'get', 'get', 'get',
              'get', 'get', 'get', 'set', 'get', 'get', 'get', 'get', 'get',
              'get', 'get', 'get', 'get']
    args = [(5, 'e'), 1, 2, 3, 4, 1, 2, 3, 4, 5, (6, 'f'), (7, 'g'), 1, 2, 3,
            4, 5, 6, 7, 3, 4, (8, 'h'), 1, 2, 3, 4, 5, 6, 7, 8, 1]
    for i in range(len(args)):
        p = multiprocessing.Process(target=worker, name='Process-' + str(i+1),
                                    args=(sync, action[i], args[i]))
        process.append(p)
        p.start()
    time.sleep(0.5)
    print "THe databse is:"
    File_serialization.data()


def process_fill(sync):
    """
    fill the database with 4 values
    ;sync: the lock and the semaphores
    """
    File_serialization.erase_data()
    process = []
    action = ['set', 'set', 'set', 'set']
    args = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    for i in range(4):
        p = multiprocessing.Process(target=worker, name='Process-' + str(i+1),
                                    args=(sync, action[i], args[i]))
        process.append(p)
    for i in range(4):
        process[i].start()
    time.sleep(5)
    print "THe databse is:"
    File_serialization.data()