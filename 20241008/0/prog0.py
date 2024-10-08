from decimal import *
from fractions import *

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(multiplier('1.34', '1.53', float))
print(multiplier("1/6", "2/3", Fraction))
print(multiplier("1.34", "1.53", Decimal))
