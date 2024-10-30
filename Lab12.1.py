import math


#Квадратне рівняння

def s (a, b, c):
    dis = b**2 - 4*a*c
    if dis > 0:
        r1 = (-b + math.sqrt(dis)) / (2*a)
        r2 = (-b - math.sqrt(dis)) / (2*a)
        return r1, r2
    elif dis == 0:
        r = -b / (2*a)
        return r,
    else:
        return "Немає дійсних коренів"

a = float(input("Введіть значення 'a':"))
b = float(input("Введіть значення 'b':"))
c = float(input("Введіть значення 'c':"))

rt = s(a, b, c)
print(rt)


#Біквадратне рівняння

def sb(a, b, c):
    qr = s(a, b, c)
    if isinstance(qr, str):
        return qr
    biqr = []
    for y in qr:
        if y >= 0:
            biqr.append(math.sqrt(y))
            biqr.append(-math.sqrt(y))
    return biqr if biqr else "Немає дійсних коренів"

rtb = sb(a, b, c)
print(rtb)