# -*- coding: utf-8 -*-


class DataBase:
    def __init__(self):
        self.db = {}

    def set_value(self, key, val):
        if key not in self.db:
            self.db[key] = val
            return True
        else:
            print "can't add value or key alredy exist"
            return False

    def get_value(self, key):
        if key in self.db:
            return self.db[key]
        return "invalid key"

    def delete_value(self, key):
        if key in self.db:
            return self.db.pop(key)
        return "invalid key"

    def set_obj(self, obj):
        self.db = obj


if __name__ == '__main__':
    a = DataBase()
    assert a.set_value("a", 11)
    assert a.set_value("b", 22)
    assert a.get_value("a") == 11
    assert a.get_value("b") == 22
    assert a.delete_value("a") == 11