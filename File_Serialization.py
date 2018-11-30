# -*- coding: utf-8 -*-

from DataBase import *
import pickle
import sys
import os

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
        super(File_serialization, self).__init__()

    def set_value(self, key, val):
        if os.stat(DATA_FILE).st_size != 0:
            with open(DATA_FILE, "rb") as file_data:
                self.db = pickle.load(file_data)
        ans = super(File_serialization, self).set_value(key, val)
        if ans:
            with open(DATA_FILE, "wb") as file_data:
                pickle.dump(self.db, file_data)
        return ans

    def get_value(self, key):
        answer = "Empty database"
        try:
            if os.stat(DATA_FILE).st_size != 0:
                with open(DATA_FILE, "rb") as file_data:
                    self.db = pickle.load(file_data)
                ret = super(File_serialization, self).get_value(key)
                answer = ret
        finally:
            return answer

    def delete_value(self, key):
        if os.stat(DATA_FILE).st_size != 0:
            with open(DATA_FILE, "rb") as file_data:
                self.db = pickle.load(file_data)
            ans = super(File_serialization, self).delete_value(key)
            with open(DATA_FILE, "wb") as file_data:
                pickle.dump(self.db, file_data)
            return ans
        else:
            return "Empty database"

    @staticmethod
    def erase_data():
        print "After the OK there is no turn back!!!!"
        b = False
        while not b:
            res = raw_input("Are you sure you want to erase all data ? (yes to erase, no to keep data)")
            if res == "yes":
               open(DATA_FILE, 'w').close()
               print "Database is clear"
               b = True
            elif res == "no":
                print "Action cancelled"
                b = True
    @classmethod
    def data(self):
        answer = "Empty database"
        try:
            if os.stat(DATA_FILE).st_size != 0:
                with open(DATA_FILE, "rb") as file_data:
                    self.db = pickle.load(file_data)
                answer = self.db
        finally:
            print answer




def main():
    """
    Add Documentation here
    """
    o = File_serialization()
    o.set_value(5, "a")
    o.set_value(7, "b")
    o.data()
    print o.get_value(5)
    o.delete_value(5)
    o.data()

if __name__ == '__main__':
    main()