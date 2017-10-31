# -*- encoding: utf-8 -*-

def tupleToString(t):
    return reduce(lambda x, y: str(x) +" "+ str(y), t)

def stringToTuple(s):
    return tuple(s.split(" "))