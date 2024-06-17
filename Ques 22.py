def find_min_max(numbers):
    if not numbers:
        return None, None  
    
    min_value = numbers[0]
    max_value = numbers[0]
    
    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    return min_value, max_value

num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = find_min_max(num_list)
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")