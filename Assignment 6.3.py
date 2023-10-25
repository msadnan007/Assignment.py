
file_name =input("Enter the file name: ")
total = 0
count = 0
try:
    with open(file_name, 'r') as fhand:
        for line in fhand:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    confidence = float(line.split(":")[1])
                    total += confidence
                    count += 1
                except:
                    print(f"Invalid number format in line: {line}")
        if count > 0:
            average = total / count
            print(f"Average spam confidence: {average:.4f}")
        else:
            print("No lines with 'X-DSPAM-Confidence' found in the file.")
except:
    print(f"File '{file_name}' not found.")