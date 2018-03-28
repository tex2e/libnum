#-*- coding:utf-8 -*-

import binascii


def s2n(s):
    """
    String to number.
    """
    if not len(s):
        return 0
    # return int(s.encode("hex"), 16)
    return int(binascii.hexlify(s.encode()), 16)


def n2s(n):
    """
    Number to string.
    """
    s = hex(n)[2:].rstrip("L")
    if len(s) % 2 != 0:
        s = "0" + s
    # return s.decode("hex")
    # return bytes.fromhex(s).decode("utf-8")
    return binascii.unhexlify(s.encode()).decode("utf-8", "backslashreplace")


def s2b(s):
    """
    String to binary.
    """
    ret = []
    for c in s:
        ret.append(bin(ord(c))[2:].zfill(8))
    return "".join(ret)


def b2s(b):
    """
    Binary to string.
    """
    ret = []
    for pos in range(0, len(b), 8):
        ret.append(chr(int(b[pos:pos + 8], 2)))
    return "".join(ret)
