import time
from itertools import islice

# Na tem problemu sem porabil ~ 4 ure
# Izziv mi je bil izredno všeč
# Za števila manjša od 1000 porabi ~15 sekund,
# za 10E3 in 10E4 mi ni uspelo dobiti rezultata v manj kot minuti

numbers = [1, 2]  # dvoumna stevila

unavailable_numbers = set()

start_time = time.time() * 1000  # in milliseconds

while numbers[len(numbers) - 1] < 2000:
    candidates = []
    # loop trough numbers
    for first_number in numbers:
        for second_number in islice(numbers, numbers.index(first_number) + 1, None):
            if first_number == second_number:
                continue
            current_value = first_number + second_number
            # print(first_number, "+", second_number, "=", current_value)
            if current_value in numbers:
                continue
            if current_value in unavailable_numbers:
                continue
            # unique number was successfully found
            if current_value in candidates:
                candidates.remove(current_value)
                unavailable_numbers.add(current_value)
            else:
                candidates.append(current_value)

    if len(candidates) > 0:
        candidates.sort()
        numbers.append(candidates[0])

end_time = time.time() * 1000

# print numbers
print(numbers)

# print time taken
print("It took ", round(end_time - start_time, 2), "ms to complete")
