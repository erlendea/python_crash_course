filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("\nI add some lines.")
    file_object.write("\nI add some more lines.")