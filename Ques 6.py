filename = 'user_input.txt'

with open(filename, 'r') as file:
    content = file.read()
    
    print("File content:")
    print(content)