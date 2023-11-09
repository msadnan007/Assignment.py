file_name = 'mbox.txt'  

try:
    with open(file_name, 'r') as file:
        sender_count = 0
        for line in file:
            if line.startswith('From '):
                sender_count += 1
                words = line.split()
                email = words[1]
                print(email)

        print(f"Number of rows found: {sender_count}")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
