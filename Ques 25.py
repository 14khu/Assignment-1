source_file = 'user_input.txt'
destination_file = 'destination.txt'

source = open(source_file,'r')
content = source.read()
source.close()

destination = open(destination_file, 'w')
destination.write(content)
destination.close()

print("Contents of user_input.txt have been copied to destination.txt.")