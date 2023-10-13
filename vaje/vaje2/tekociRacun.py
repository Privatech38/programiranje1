stanje = 0
while 1:
    stanje += float(input("Sprememba: "))
    print("Stanje: ", stanje)
    if stanje <= -100:
        print("Bankrot")
        break