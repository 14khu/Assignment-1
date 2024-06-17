n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = [0, 1]

for i in range(2, n):
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)
                        
print("The first numbers in the Fibonacci sequence are:")
for number in fib_sequence:
    print(number, end=" ")