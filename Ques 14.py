lines = []

while True:
    line = input("Enter a line (press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

if lines:
    print("\nLines entered:")
    for line in lines:
        print(line)
else:
    print("No lines entered.")
   