print("Typing 'done' will exit the programm")
numbers = []
while True:
    user_input = input("Please enter an integer: ")

    if user_input.lower() == 'done':
        print("__________Bye!__________")
        break

    try:
        number = int(user_input)
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print(f"[{numbers}], average: {average}")
    except ValueError:
        print("Please enter a valid integer or 'done' to exit.")

print("List of numbers:", numbers)
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Final average: {average}")
else:
    print("No numbers entered.")
