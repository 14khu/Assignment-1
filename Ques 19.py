def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    no_punctuation_string = ""
    
    for char in input_string:
        if char not in punctuation:
            no_punctuation_string += char
    
    return no_punctuation_string

input_string = "Hello, world! This is a test string with punctuation."
clean_string = remove_punctuation(input_string)
print(clean_string)