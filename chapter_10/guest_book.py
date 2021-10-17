filename = 'guest_book.txt'

print("Write your username (if you want to exit, type 'q')")

while True:
    name = input("Username / exit: ")
    
    if name !='q':
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
    else:
        break


