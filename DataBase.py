# -*- coding: utf-8 -*-
"""
author: Yotam Levit
project: DataBase Readers and Writers sync
"""


class DataBase(object):
    """
    A DataBase class type - dictionary
    """
    def __init__(self):
        """
        class initializer
        """
        self.db = {}

    def set_value(self, key, val):
        """
        sets a value and it`s key in the dictionary
        ;key: the value`s key in the dictionary
        ;val: the key`s value in the dictionary
        ;return: True if succeed False if not
        """
        if key not in self.db:
            self.db[key] = val
            return True
        else:
            return False

    def get_value(self, key):
        """
        ;key: the key of the wanted value
        ;return: the key`s value if found
        if not returns invalid key
        """
        if key in self.db:
            return self.db[key]
        return "invalid key"

    def delete_value(self, key):
        """
        deletes a key and it`s value from the dictionary
        ;key: the key that is going to be deleted
        ;return: the value of the key if the key and the
        value were deleted and invalid key if not
        """
        if key in self.db:
            return self.db.pop(key)
        return "invalid key"


if __name__ == '__main__':
    a = DataBase()
    assert a.set_value("a", 11)
    assert a.set_value("b", 22)
    assert a.get_value("a") == 11
    assert a.get_value("b") == 22
    assert a.delete_value("a") == 11