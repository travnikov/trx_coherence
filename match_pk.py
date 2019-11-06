# File:
# Purpose: расчёт п-контура в режиме соглосования сопротивлений 50/заданное ом
# Notice: упращённый расчёт, требует подгонки.

import math
from prettytable import PrettyTable
tg = []

print("введи частоту в мгц:  ")
F = float(input())
print("введи сопротивление нагрузки в ом:  ")
O = float(input())
A = []

def ras_t(f, o):
    x = 0
    while x < 5:
        k = math.sqrt(o)
        p = math.pi * 2
        L = k / (p * f)
        C = 1000 / (p * f) * k
        f1 = f + 0.0001
        L = str(round(L, 2))
        C = str(round(C, 0))
        f1 = str(round(f1, 1))
        A.append(L)
        A.append(C)
        A.append(f1)
        f = f + 0.2
        x += 1
    return A

o = O * 50
f = F - 0.2
A = ras_t(f, o)
#print(A)

tg = ['индуктивность L1', 'С1 = С2 пифорат', 'частота мГц']
columns = len(tg)
table = PrettyTable(tg)
while A:
    table.add_row(A[:columns])
    A = A[columns:]
print(table)









