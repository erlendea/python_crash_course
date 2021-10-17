def count_words(filename):
    """Count the approximate number of words in a text file."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"The file you try to read, {filename}, is not available.")
        #pass
    else:
        words = content.split()
        print(f"The file {filename} contains approximately {len(words)} of words.")