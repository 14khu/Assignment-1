from datetime import datetime

current_year = datetime.now().year

birth_year_str = input("Enter your birth year: ")

if birth_year_str.isdigit():
    birth_year = int(birth_year_str)
    
    age = current_year - birth_year
    
    print("Your age is:",age)
else:
    print("Please enter a valid year (e.g., 1990).")