# File: Ant_coherence_trx.py
# Purpose:
# Notice:



""" расчета ФНЧ """
from prettytable import PrettyTable
td = [...]
tg = [...]

import itertools
import math
p = math.pi

print("введи частоту в мГц")
Fr = int(input())

print("введите сопротивление 50/75 ом")                         
R = int(input())

def tablic(td):
    tg = ['к-во витков', 'д.провода', 'д.каркаса']
    columns = len(tg)
    table = PrettyTable(tg)
    while td:
        table.add_row(td[:columns])
        td = td[columns:]
    print(table)

def witki(L):
    t = []
    D = [0.6, 0.8, 1.0, 1.6]
    for d in D:
        av = (L * 1.96)/d
        aw = (math.sqrt(av)) * 10
        j = ((d * 1.5) * 10) / aw
        aw = str(round(aw, 1))
        j = str(round(j, 2))

        interlist=[aw, j, d]
        t.append(interlist)
    return t

Fc = 1.2 * Fr
L1 = R/(p * Fc)
C1 = 1000000/(2 * p * Fc * R)

t = witki(L1)
td = list(itertools.chain(*t))
print("таблица значений для L1")
tablic(td)

Fg = Fr * 2
Fe = 1 - ((Fc / Fg) * (Fc / Fg))
m = math.sqrt(Fe)
L2 = m * L1
C3 = m * C1
C3 = str(round(C3, 0))
C5 = (1 - ((m * m) * C1)) / (2 * m)
C5 = str(round(C5, 0))

t = witki(L2)
td = list(itertools.chain(*t))
print("таблица значений для L2")
tablic(td)

C1 = str(round(C1, 0))
L1 = str(round(L1, 1))
L2 = str(round(L2, 1))
print("C1=C2 =",C1)
print("C3=C4 =",C3)
print("C5 =",C5)
print("L1 =",L1)
print("L2 =",L2)
