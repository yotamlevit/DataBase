"""
author: Yotam Levit
project: DataBase Readers and Writers sync
"""
import logging
from File_Sync import *
import time

###############
#logging config
###############
logging.basicConfig(filename='logging.log', level=logging.DEBUG,
                    format='(%(threadName) -10s) %(asctime)s %(levelname)-8s '
                           '%(message)s')


def worker(sync, action, args):
    """
    the main or hub function that the process
    and the threads are targeted to, the function
    logging the activity of the process of the thread
    ;sync: the sync object
    ;action: the action that the process
    or the threads should do
    ;args: the needed arguments for the action
    """
    logging.debug('starting')
    data = File_Sync()
    if action == 'set':
        set1(sync, data, args)
    elif action == 'get':
        get(sync, data, args)
    elif action == 'delete':
        delete(sync, data, args)
    time.sleep(2)
    logging.debug('Exiting')


def set1(sync, data, args):
    """
    running the set value action with the loggers
    and the sync using a sync object
    ;sync: the sync object
    ;data: the database object that controls
    the database
    ;args: the key and the value for the database
    """
    sync.lock_acquire()
    logging.debug('SET - lock acquire')
    x = 0
    while x < 10:
        sync.semaphore_acquire()
        logging.debug('SET - semphore acquire')
        x += 1
    ans = data.set_value(args[0], args[1])
    logging.debug('answer - ' + str(ans))
    x = 0
    while x < 10:
        sync.semaphore_release()
        logging.debug('SET - semphore release')
        x += 1
    sync.lock_release()
    logging.debug('SET - lock relese')


def get(sync, data, args):
    """
    running the get value action with the loggers
    and the sync using a sync object
    ;sync: the sync object
    ;data: the database object that controls
    the database
    ;args: the key to find the value
    """
    sync.semaphore_acquire()
    logging.debug('GET - semphore acquire')
    ans = data.get_value(args)
    sync.semaphore_release()
    logging.debug('GET - semphore release')
    logging.debug('answer - ' + str(ans))


def delete(sync, data, args):
    """
    running the delete value action with the loggers
    and the sync using a sync object
    ;sync: the sync object
    ;data: the database object that controls
    the database
    ;args: the key to find the value and delete it
    """
    sync.lock_acquire()
    logging.debug('DEL - lock acquire')
    x = 0
    while x < 10:
        sync.semaphore_acquire()
        logging.debug('DEL - semphore acquire')
        x += 1
    ans = data.delete_value(args)
    logging.debug('answer - ' + str(ans))
    x = 0
    while x < 10:
        sync.semaphore_release()
        logging.debug('DEL - semphore release')
        x += 1
    sync.lock_release()
    logging.debug('DEL - lock relese')