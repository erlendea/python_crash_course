def open_file(filename):

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"\nThe file {filename} does not exist.")
        #pass
    else:            
        print(f"\nOpening file {filename} with the content:\n")
        print(contents)

filenames = ['cat.txt', 'text_files/dogs.txt']


for filename in filenames:
    open_file(filename)