def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

num_list = [1, 2, 3, 4, 5]
result = calculate_sum(num_list)
print(f"The sum of numbers {num_list} is: {result}")