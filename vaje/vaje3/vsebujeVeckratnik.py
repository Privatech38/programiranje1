xs = [5, 4, -7, 12, -3, -4, 11, 42, 2]

count_42 = False

for num in xs:
    if num % 42 == 0:
        count_42 = True

print(count_42)