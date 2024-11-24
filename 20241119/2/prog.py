class Num:
    def __get__(self, obj, cls):
        if self.key not in obj.__dict__:
            obj.__dict__[self.key] = 0
        return obj.__dict__[self.key]

    def __set__(self, obj, val):
        if type(val) == int:
            obj.__dict__[self.key] = val
        else:
            obj.__dict__[self.key] = len(val)

    def __set_name__(self, owner, name):
        self.key = name

    def __delete__(self, obj):
        obj._value = None

import sys
exec(sys.stdin.read())
