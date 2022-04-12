import random
import sys
from ScrambleImage import scramble

moves = ["U", "D", "F", "B", "R", "L"]
dir = ["", "'", "2"]
slen = random.randint(25, 28)

def gen_scramble():
    # Make array of arrays that represent moves ex. U' = ['U', "'"]
    s = valid([[random.choice(moves), random.choice(dir)] for x in range(slen)])
    cube = scramble(s, slen)

    # Formatear scramble a una cadena con movecount
    return ''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))) + "[" + str(slen) + "]"

def valid(ar):
    # Comprobar si Mover detrás o 2 atrás es lo mismo que el movimiento aleatorio
    # esto elimina 'R R2' o 'R L R2' o similar para todos los movimientos
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar
 
s = gen_scramble()
print(s)