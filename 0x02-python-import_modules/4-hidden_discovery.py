#!/usr/bin/python3
import marshal, dis, sys

header_sizes = [
    (8,  (0, 9, 2)),
    (12, (3, 6)),
    (16, (3, 7)),
]
header_size = next(s for s, v in reversed(header_sizes) if sys.version_info >= v)
f = open("hidden_4.pyc", "rb")
meta = f.read(header_size)
code = marshal.load(f)
dis.dis(code)
print(code.co_varnames)
