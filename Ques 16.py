def count_character_frequency(input_string):
    frequency_dict = {}

    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

test_string = "hello world"
frequency = count_character_frequency(test_string)

for char, count in frequency.items():
    print(f"'{char}': {count}")