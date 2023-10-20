intervali = [tuple(int(x) for x in vrstica.split("-")) for vrstica in open("intervali.txt")]

intervali = sorted(intervali)

# Združi intervale
i = 0
while i < len(intervali) - 1:
    if intervali[i + 1][0] - intervali[i][1] <= 1:
        novi_interval = (intervali[i][0], max(intervali[i + 1][1], intervali[i][1]))
        intervali.remove(intervali[i + 1])
        intervali[i] = novi_interval
    else:
        i += 1
# Preštej vmesna števils

dovoljena_stevila = 0

i = 0
while i < len(intervali) - 1:
    kolicina = intervali[i + 1][0] - intervali[i][1] - 1
    if kolicina > 0:
        dovoljena_stevila += kolicina
    i += 1

print(dovoljena_stevila)