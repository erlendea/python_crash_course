glossary = {
    'dictionary': 'A dictionary in Python is a collection of key-value pairs.',
    'key': 'A key’s value can be a number, a string, a list, or even another dictionary',
    'sum': 'Sum of numbers in the list is required everywhere',
    'del': 'If you know the position of the item you want to remove from a list, you can use the del statement',
    'remove': 'f you only know the value of the item you want to remove, you can use the remove() method.'
}

for word, explanation in glossary.items():
    print(f"{word.title()}:")   
    print(f"\tMeans: {explanation}")