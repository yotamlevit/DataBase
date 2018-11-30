# -*- coding: utf-8 -*-

from File_Sync import *
from Check_Threads import *
import sys
import time
import logging
logging.basicConfig(filename='logging.log', level=logging.DEBUG, format='(%(threadName) -10s) %(asctime)s %(levelname)-8s %(message)s')
action_dic = {}

path_to_tool = sys.argv[0].split("/")
path_to_tool.pop()
temp = ""
for word in path_to_tool:
    temp += word + "/"
path_to_tool = temp[:-1]
path_to_tool += "/"

DATA_FILE = path_to_tool + "File_Data.txt"

def check_4():
    File_serialization.erase_data()


def worker(action, args):
    logging.debug('starting')
    data = File_Sync(False)
    if action is 'set':
        print data.set_value(args[0], args[1])
    elif action is 'get':
        print data.get_value(args)
    elif action is 'delete':
        print data.delete_value(args)
    time.sleep(2)
    logging.debug('Exiting')

def test():
    a = File_Sync(False)
    a.set_value(1, "a")
    a.set_value(2, "b")
    a.set_value(3, "c")
    a.set_value(4, "d")
    print a.get_value(1)
    print a.get_value(2)
    print a.get_value(3)
    print a.get_value(4)

def main():
    """
    Add Documentation here
    """
    check = Check_Threads()
    check.check_1()
    check.check_2()





if __name__ == '__main__':
    main()