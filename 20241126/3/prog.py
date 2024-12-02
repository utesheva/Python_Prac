import io
import sys
import struct
import os

try:
    file = io.BytesIO(sys.stdin.buffer.read())
    if len(file.getvalue()) < 44:
        raise AttributeError('NO')
    file.seek(4)
    size, marker = struct.unpack('i4s', file.read(8))
    if marker != 'WAVE':
        raise AttributeError('NO')
    file.seek(20)
    tp, chan, sample = struct.unpack('hhi', file.read(8))
    file.seek(34)
    b_p_s = struct.unpack('h', file.read(2))[0]
    file.seek(40)
    data = struct.unpack('i', file.read(4))[0]
    print(f'Size={size}, Type={tp}, Channels={chan}, Rate={sample}, Bits={b_p_s}, Data size={data}')
except AttributeError as e:
    print(e)
