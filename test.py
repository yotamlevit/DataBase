# -*- coding: utf-8 -*-

import sys

path_to_tool = sys.argv[0].split("/")
path_to_tool.pop()
temp = ""
for word in path_to_tool:
    temp += word + "/"
path_to_tool = temp[:-1]
path_to_tool += "/"

DATA_FILE = path_to_tool + "File_Data.txt"


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()