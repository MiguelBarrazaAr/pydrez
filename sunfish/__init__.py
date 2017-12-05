# -*- coding: utf-8 -*-
import tools
import sunfish
import re

A1, H1, A8, H8 = 91, 98, 21, 28
def parse(c, t='w'):
    fil, rank = ord(c[0]) - ord('a'), int(c[1]) - 1
    if t=='b':
        return (rank+2)*10+(8-fil)
    else:
        return A1 + fil - 10*rank

def render(i):
    rank, fil = divmod(i - A1, 10)
    return chr(fil + ord('a')) + str(-rank + 1)

def brender(i):
    return render(119-i)


def positionInitial():
    return tools.parseFEN(tools.FEN_INITIAL)

def parseFen(fen):
    return tools.parseFEN(fen)

def search(position, secs=1):
    return sunfish.Searcher().search(position, secs)