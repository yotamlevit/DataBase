# -*- coding: utf-8 -*-
"""
author: Yotam Levit
project: DataBase Readers and Writers sync
"""
from File_Serialization import File_serialization


class File_Sync(File_serialization):
    """
    closest stage from the sync
    the class converts the answers from the database to the log
    """
    def __init__(self):
        """
        class initializer
        son`s of the File_serialization class
        """
        super(File_Sync, self).__init__()

    def set_value(self, key, val):
        """
        sets a value and it`s key in the database
        ;key: the value`s key in the database
        ;val: the key`s value in the database
        ;return: Value was added if succeed can't
         add value or key alredy exist if not
        """
        ans = super(File_Sync, self).set_value(key, val)
        if ans:
            return "Value was added"
        return "can't add value or key alredy exist"

    def get_value(self, key):
        """
        ;key: the key of the wanted value
        ;return: the key`s value if found
        if not returns Warning - Empty database or invalid value
        """
        val = super(File_Sync, self).get_value(key)
        if val != "invalid key":
            return 'the value is - ' + val
        return val

    def delete_value(self, key):
        """
        deletes a key and it`s value from the database
        ;key: the key that is going to be deleted
        ;return: the value of the key if the key and the
        value were deleted and invalid key if not
        if the database is empty returns Empty database
        """
        return super(File_Sync, self).delete_value(key)