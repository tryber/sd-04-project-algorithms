
def find_duplicate(numbers):
    for i, current_number in enumerate(numbers):
        for next_number in numbers[i + 1:]:
            if type(current_number) is str or current_number < 0:
                return False
            if current_number == next_number:
                return current_number
    return False
