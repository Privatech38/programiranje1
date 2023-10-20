filmi = [
    ('Poletje v skoljki 2', 6.1),
    ('Ne cakaj na maj', 7.3),
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1),
    ('Poletje v skoljki', 7.2),
    ('To so gadi', 7.7),
]

first_7_film = True
najboljsi_film = ("", 0.0)
amount = 0
print("imena vseh filmov z oceno vsaj 7.0")
for film in filmi:
    amount += film[1]
    if film[1] > 7.0:
        print(film[0])
        if first_7_film:
            print("Prvi film z oceno 7.0:", film[0])
            first_7_film = False
    if najboljsi_film[1] < film[1]:
        najboljsi_film = film
    if '2' in film[0]:
        print("Film z drugim delom", film[0])
print("ime filma z najvišjo oceno:", najboljsi_film[0])
print("Povprečna ocena:", amount / len(filmi))


