import csv

filename = 'output.csv'

data = [
    ['name', 'age', 'city'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

with open(filename, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    csv_writer.writerows(data)

print("The data has been written to",filename)