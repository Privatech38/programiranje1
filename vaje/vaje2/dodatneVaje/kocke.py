stevilo_kock = int(input("Vpiši število kock: "))
skatla = 1
sirina = 1
while skatla < stevilo_kock:
    sirina += 1
    skatla = sirina ** 2
print("Potrebujemo škatlo širine", sirina, "v kateri je prostora še za", skatla - stevilo_kock, "kock")