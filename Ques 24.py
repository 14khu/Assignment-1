def calculate(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"
    
    return result

def main():
    print("Simple Calculator")
    print("=================")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = calculate(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()