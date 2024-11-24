class Vowel:
    __slots__ = set(list('aouiey'))
    answer = 42
    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    @property
    def full(self):
        return len([getattr(self, i) for i in 'aeiouy' if hasattr(self, i)]) == 6

    @full.setter
    def full(self, arg):
        return
    def __str__(self):
        return ', '.join([f'{i}: {str(getattr(self, i))}' for i in 'aeiouy' if hasattr(self, i)])

import sys
exec(sys.stdin.read())
