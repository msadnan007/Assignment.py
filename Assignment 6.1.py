def convert_file_to_uppercase(file_name):
    try:
        file=open(file_name, 'r') 
        for line in file:
                print(line.upper(), end='')

    except:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    file_name = input("Enter the name of the file: ")
    convert_file_to_uppercase(file_name)
