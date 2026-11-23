# List of 10 numbers
numbers = [9, 8, 3, 4, 3, 6, 8, 8, 9, 18]


# FUNCTION 1: Calculate Sum
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# FUNCTION 2: Calculate Average/Mean
def calculate_average(numbers):
    total = calculate_sum(numbers)
    average = total / len(numbers)
    return average


# FUNCTION 3: Calculate Median and Mode
def calculate_median_mode(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        median = (sorted_numbers[middle - 1] +
                  sorted_numbers[middle]) / 2
    else:
        median = sorted_numbers[middle]

    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    highest = max(frequency.values())
    mode = [num for num, count in frequency.items()
            if count == highest and count > 1]

    if not mode:
        mode = "No mode"

    return median, mode


# DISPLAY RESULTS
print("Numbers:", numbers)
print("Sum:", calculate_sum(numbers))
print("Average:", calculate_average(numbers))

median, mode = calculate_median_mode(numbers)
print("Median:", median)
print("Mode:", mode)
