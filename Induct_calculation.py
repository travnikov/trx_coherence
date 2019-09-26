# File: Induct_calculation.py 
# Purpose :программа для расчёта количества витков при разных диаметрах каркаса соотношение l/D == 0.5 (максимум добротности).
# Notice: часть программы " Ant_coherence_trx.py "


import math
from prettytable import PrettyTable

td = [...]
tg = [...]

print("введи индуктивность")
L = int(input())
A = [1, 1.6, 2, 3.2, 4, 5, 6.3] # диаметры каркаса в см
tt = []
tg = []

for D in A:
    z = (L * 0.96) / D
    a = math.sqrt(z)
    w = 10 * a
    j = (D * 0.5) * 10 / w
    w = str(round(w, 1))
    j = str(round(j, 2))

    innerlist = [w, j, D]
    tt.append(innerlist)
    
for sublist in tt:
    for item in sublist:
        tg.append(item)

#print(tg)
    
td = ['к-во витков', 'д. провода мм', 'д.каркаса см']
columns = len(td)
table = PrettyTable(td)
while tg:
    table.add_row(tg[:columns])
    tg = tg[columns:]
print("сводная таблица значений катушки с максимальной добротность")
print(table)



