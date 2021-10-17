f_names = ['alice.txt', 'siddhartha.txt',
'moby_dick.txt', 'little_women.txt']
for f_name in f_names:
# Report the length of each file found.
    try:
        with open(f_name) as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Just move on to the next file.
        pass
    else:
        num_lines = len(lines)
        msg = f"{f_name} has {num_lines}"
        msg += " lines."
        print(msg)