# File: colcu_pf_test.py
# Purpose: расчёт полосового фильтра с максимальной добротностью l/D=0.5 и добротностью Q>150 при l/D=1
# Notice:

import math
import itertools
from prettytable import PrettyTable
tg = [...]

print("введи частоту в мГц")
F = float(input())
if F >= 7:
    f = F/7
    L = 6.0/f
else:
    f = 7/F
    L = 6.0 * f

a = 159.1/F
C = (a * a)/L
C = str(round(C, 0))

tt = []
A = [0.8, 1, 2, 3] #диаметр каркаса в см
for D in A:
    z1 = (L * 0.96) / D
    w1 = 10 * (math.sqrt(z1))
    j1 = (D * 0.5) * 10 / w1
    z2 = (L * 1.46) / D
    w2 = 10 * (math.sqrt(z2))
    j2 = (D * 10)/ w2
    w1 = str(round(w1, 1))
    j1 = str(round(j1, 2))
    w2 = str(round(w2, 1))
    j2 = str(round(j2, 2))
    innerlist = [w1, j1, w2, j2,  D]
    tt.append(innerlist)

tr = list(itertools.chain(*tt))
L = str(round(L, 2))
print("L1=L2 =",L)
print("C1=C2 =",C)
#print(tr)

tg = ['к.вит.l/D=0.5','Д.пров.l/D=0.5','к.вит.l/D=1','Д.пров.l/D=1','Д.каркаса(см)']
columns = len(tg)
table = PrettyTable(tg)
while tr:
    table.add_row(tr[:columns])
    tr = tr[columns:]
print(table)







