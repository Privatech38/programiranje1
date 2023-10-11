import time
from itertools import islice

numbers = [1, 2]  # dvoumna stevila

unavailable_numbers = []

start_time = time.time() * 1000  # in milliseconds



while len(numbers) < 20:
    length = len(numbers)
    last_unique_number = 0
    candidates = []
    first_loop = True
    # loop trough numbers
    for first_number in numbers:
        for second_number in islice(numbers, numbers.index(first_number) + 1, None):
            if first_number == second_number:
                continue
            current_value = first_number + second_number
            # print(first_number, "+", second_number, "=", current_value, "First loop:", first_loop)
            if current_value in numbers:
                continue
            if current_value in unavailable_numbers:
                continue
            #if not first_loop and current_value > last_unique_number:
            #    break
            # unique number was successfully found
            first_loop = False
            if current_value in candidates:
                candidates.remove(current_value)
                last_unique_number = 0
                first_loop = True
                unavailable_numbers.append(current_value)
            else:
                candidates.append(current_value)

    if len(candidates) > 0:
        numbers.append(candidates[0])
        # print("Added", candidates[0])

end_time = time.time() * 1000

# print numbers
print(numbers)

# print time taken
print("It took ", end_time - start_time, "ms to complete")
