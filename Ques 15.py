import csv

filename = 'output.csv'

with open(filename, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        print(row)