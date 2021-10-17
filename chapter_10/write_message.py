filename = 'programming.txt'

pi = 3.14

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("\nI love programming also.")
    file_object.write(f"\nI love pi {str(pi)}.")
    file_object.write(f"\n\t{str(pi)}")
    