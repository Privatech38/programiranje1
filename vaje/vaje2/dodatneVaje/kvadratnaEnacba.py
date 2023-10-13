from math import sqrt

a = int(input("Vpiši a: "))
b = int(input("Vpiši b: "))
c = int(input("Vpiši c: "))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("Enačba ima dve realni rešitvi:", x1, "in", x2)
elif d == 0:
    x = (-b + sqrt(d)) / (2 * a)
    print("Enačba ima eno realno rešitev:", x)
else:
    print("Enačba nima realnih rešitev.")
