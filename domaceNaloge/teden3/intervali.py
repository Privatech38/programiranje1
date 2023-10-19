intervali = [
    (12, 18),
    (2, 5),
    (3, 8),
    (0, 4),
    (15, 19),
    (6, 9),
    (13, 17),
    (4, 8)
]

intervali = [tuple(int(x) for x in vrstica.split("-")) for vrstica in open("intervali.txt")]

intervali = sorted(intervali)

dovoljena_stevila = 0

i = 0
while i < len(intervali) - 1:
    kolicina = intervali[i + 1][0] - intervali[i][1] - 1
    if kolicina > 0:
        dovoljena_stevila += kolicina
    i += 1

print(dovoljena_stevila)