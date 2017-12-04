# -*- coding: utf-8 -*-
import tools
import sunfish
import re

A1, H1, A8, H8 = 91, 98, 21, 28
def parse(c):
    fil, rank = ord(c[0]) - ord('a'), int(c[1]) - 1
    return A1 + fil - 10*rank

def render(i):
    rank, fil = divmod(i - A1, 10)
    return chr(fil + ord('a')) + str(-rank + 1)

def brender(i):
    return render(119-i)
