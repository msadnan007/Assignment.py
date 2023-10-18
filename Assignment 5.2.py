input_str = input("Enter a string: ")
length = len(input_str)
index = length - 1

while index >= 0:
    character = input_str[index]
    print(character)
    index -= 1

