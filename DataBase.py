# -*- coding: utf-8 -*-


class DataBase:
    def __init__(self):
        self.dic = {}

    def set_value(self, key, val):
        if self.is_key(key):
            self.dic[key] = val
            return True
        else:
            return False

    def get_value(self, key):
        if self.is_key(key):
            return self.dic[key]
        return "invalid key"

    def delete_value(self, key):
        if key in self.dic:
            return self.dic.pop(key)
        return "invalid key"

    def is_key(self, key):
        if type(key) == str or type(key) == tuple or type(key) == int:
            return True
        return False


class File_Data:
    def __init__(self):
        self.file = "C:/Users/cyber/Documents/GitHyb/DataBase"

if __name__ == '__main__':
    a = DataBase()
    assert a.set_value("a", 11)
    assert a.set_value("b", 22)
    assert a.get_value("a") == 11
    assert a.get_value("b") == 22
    assert a.delete_value("a") == 11
    assert a.is_key("b")