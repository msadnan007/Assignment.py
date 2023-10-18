def count_characters(input_str):
    num_count = 0
    upper_count = 0
    lower_count = 0
    other_count = 0

    for char in input_str:
        if char.isnumeric():
            num_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        else:
            other_count += 1

    return num_count, upper_count, lower_count, other_count

input_str = input("Please enter string: ")
num_count, upper_count, lower_count, other_count = count_characters(input_str)

print(f"uppercase letters: {upper_count}")
print(f"lowercase letters: {lower_count}")
print(f"Numbers: {num_count}")
print(f"other characters: {other_count}")
