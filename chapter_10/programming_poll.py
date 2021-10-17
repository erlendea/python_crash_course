filename = 'poll.txt'

print("Write why you love programming (if you want to exit, type 'q')")

while True:
    text_python = input("Text / exit: ")
    
    if text_python !='q':
        with open(filename, 'a') as file_object:
            file_object.write(f"{text_python}\n")
    else:
        break


