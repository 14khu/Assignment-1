user_input = input("Enter the text you want to write to the file: ")

with open('user_input.txt', 'w') as file:
    file.write(user_input)

print("The text has been written to 'user_input.txt'")