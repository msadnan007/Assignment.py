count = 0
total = 0

while True:
    user_input = input(("Enter a number:"))
    
    if user_input =="done":
        break
    
    try:
        user_input = int(user_input)

    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")
        continue
    total = total + user_input
    count = count + 1

average = total / count
print("Sum:", total)
print("Count:", count)
print("Average:", average)
