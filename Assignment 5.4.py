while True:
    input_str = input("Please enter string : ")

    if input_str == 'done':
        print("Bye!")
        break
    special_characters = ",.!:?"
    processed_str = ''.join(char for char in input_str if char not in special_characters)
    processed_str = processed_str.upper()
    print("Processed string: " + processed_str)


