number = input("Enter a number: ")

sum_of_digits = 0

for digit in number:
    sum_of_digits += int(digit)

print("The sum of the digits of number is:",sum_of_digits)