while True:
    input_str = input("Please enter two words : ")
    
    if input_str == 'done' or not input_str:
        print("bye!")
        break
    
    words = input_str.split()
    
    if len(words) == 1:
        print(f"You entered only one word: {words[0]}")
    elif len(words) == 2:
        sorted_words = sorted(words)
        print(f"{sorted_words[0]} comes firts.")
    else:
        print("Please enter two words : ")


