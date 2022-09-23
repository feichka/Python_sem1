# AB = √(xb - xa)2 + (yb - ya)2
import math

a = float(input('Введите значение точки х1: '))
b = float(input('Введите значение точки y1: '))
c = float(input('Введите значение точки х2: '))
d = float(input('Введите значение точки y2: '))
dis = math.sqrt(math.pow((c - a), 2) + math.pow((d - b), 2))
e = round(dis,2)
print('Расстояние между точками равно ', e)

