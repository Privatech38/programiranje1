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

intervali = [tuple(int(x) for x in vrstica.split("-")) for vrstica in open("intervali112.txt")]

intervali = sorted(intervali)

# Združi intervale
def combine_intervals():
    was_modified = False
    i = 0
    while i < len(intervali) - 1:
        if intervali[i + 1][0] - intervali[i][1] <= 1:
            novi_interval = (intervali[i][0], max(intervali[i + 1][1], intervali[i][1]))
            intervali.remove(intervali[i + 1])
            intervali[i] = novi_interval
            was_modified = True
        else:
            i += 1
    if not was_modified:
        return
    combine_intervals()
    print(len(intervali))

combine_intervals()
# Preštej vmesna števils

dovoljena_stevila = 0

i = 0
while i < len(intervali) - 1:
    kolicina = intervali[i + 1][0] - intervali[i][1] - 1
    if kolicina > 0:
        dovoljena_stevila += kolicina
    i += 1

print(dovoljena_stevila)