def objcount(cls):
    class objcnt(cls):
        counter = 0
        def __init__(self, *args):
            super().__init__(*args)
            self.__class__.counter += 1

        def __del__(self):
            for i in self.__class__.mro():
                if i != self.__class__ and hasattr(i, '__del__'):
                    super().__del__()
            self.__class__.counter -= 1
    return objcnt

import sys
exec(sys.stdin.read())
