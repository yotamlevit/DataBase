# -*- coding: utf-8 -*-


class DataBase:
    def __init__(self):
        self.__dic = {}

    def set_value(self, key, val):
        if key not in self.__dic:
            self.__dic[key] = val
            return True
        else:
            print "can't add value"
            return False

    def get_value(self, key):
        if key in self.__dic:
            return self.__dic[key]
        return "invalid key"

    def delete_value(self, key):
        if key in self.__dic:
            return self.__dic.pop(key)
        return "invalid key"

    def set_obj(self, obj):
        self.__dic = obj


if __name__ == '__main__':
    a = DataBase()
    assert a.set_value("a", 11)
    assert a.set_value("b", 22)
    assert a.get_value("a") == 11
    assert a.get_value("b") == 22
    assert a.delete_value("a") == 11