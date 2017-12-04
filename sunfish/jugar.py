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

print("bienvenido a esta prueba")

pos = tools.parseFEN(tools.FEN_INITIAL)
#pos=pos.rotate()
secs=1

while True:
    #print(' '.join(pos.board))
    print("escriba su movimiento")
    print("-->")
    comando = raw_input()
    if comando == "salir":
        print("gracias por jugar")
        break
    else:
        match = re.match('([a-h][1-8])'*2, comando)
        m = parse(match.group(1)), parse(match.group(2))
        pos = pos.move(m)
        print("las blancas mueven: ", render(m[0]), render(m[1]))
        #print(pos.board)
        m, _ = sunfish.Searcher().search(pos, secs=2)
        pos = pos.move(m)
        print(m)
        #print("las negras mueven: ", tools.mrender(pos, m))
        print("las negras mueven :", brender(m[0]) + brender(m[1]))
