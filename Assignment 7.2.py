file_name = 'romeo.txt'

try:
    with open(file_name, 'r') as file:
        unique_words = []
        for line in file:
            words_in_line = line.split()
            for word in words_in_line:
                if word not in unique_words:
                    unique_words.append(word)

        unique_words.sort()
        for word in unique_words:
            print(word)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
