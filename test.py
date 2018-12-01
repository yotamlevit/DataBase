# -*- coding: utf-8 -*-
"""
author: Yotam Levit
project: DataBase Readers and Writers sync
"""
from Check_Process import *
from Check_Threads import *


def main():
    """
    the main python file testing the sync with
    readers and writers - threads and process
    """
    ####################################
    #testing the threads synchronization
    ####################################
    sync = Sync(False)
    thread_final_check(sync)
    ####################################
    #testing the process synchronization
    ####################################
    sync1 = Sync(True)
    process_final_check(sync1)


if __name__ == '__main__':
    main()