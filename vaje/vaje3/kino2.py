filmi = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ocene = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]

for film in zip(filmi, ocene):
    if film[0].count(' ') == 2:
        print(film[0], "(", film[1], ")")