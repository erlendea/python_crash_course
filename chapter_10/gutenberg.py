filename = 'siddhartha.txt'
find_word = 'the'

with open(filename, encoding='utf-8') as f:
    contents = f.read()

contents_lower = contents.lower()
word_list = contents_lower.split()
no_words = word_list.count(find_word)

print(no_words)