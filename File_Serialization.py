# -*- coding: utf-8 -*-

from DataBase import *
import pickle
import sys

path_to_tool = sys.argv[0].split("/")
path_to_tool.pop()
temp = ""
for word in path_to_tool:
    temp += word + "/"
path_to_tool = temp[:-1]
path_to_tool += "/"

DATA_FILE = path_to_tool + "File_Data.txt"


class File_serialization(DataBase):
    def __init__(self):
        DataBase.__init__(self)
        print DATA_FILE
        with open(DATA_FILE, "rb") as file_data:
            self.db = pickle.load(file_data)

    def write_to_file(self):
        with open(DATA_FILE, "wb") as file_data:
            pickle.dump(self.db, file_data)



def main():
    """
    Add Documentation here
    """
    o = File_serialization()
    o.set_value(1, "a")
    o.set_value(2, "b")
    o.write_to_file()


if __name__ == '__main__':
    main()