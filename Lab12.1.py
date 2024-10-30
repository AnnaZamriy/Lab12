import math


a = float(input("Введіть значення 'a':"))
b = float(input("Введіть значення 'b':"))
c = float(input("Введіть значення 'c':"))


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

rt = s(a, b, c)
print(rt)


#Біквадратне рівняння

def sb(a, b, c):
    quadratic_roots = s(a, b, c)
    if isinstance(quadratic_roots, str):
        return quadratic_roots
    biquadratic_roots = []
    for y in quadratic_roots:
        if y >= 0:
            biquadratic_roots.append(math.sqrt(y))
            biquadratic_roots.append(-math.sqrt(y))
    return biquadratic_roots if biquadratic_roots else "Немає дійсних коренів"

rtb = sb(a, b, c)
print(rtb)