i = 1
while i < 101:
    if i % 7 == 0 or '7' in str(i):
        print("BUM")
    else:
        print(i)
    i += 1