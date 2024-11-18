import collections

class DivStr(collections.UserString):
    def __init__(self, data=''):
        super().__init__(data)

    def __floordiv__(self, n):
        l = len(self.data) // n
        for i in range(n):
            yield self.data[l * i:l * i + l]

    def __mod__(self, n):
        l = len(self.data) // n
        return DivStr(self.data[l * n: len(self.data)])

import sys
exec(sys.stdin.read())
