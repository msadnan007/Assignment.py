def calculate_grade(score):
    if 0 <= score <= 100:
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'
    else:
        return 'Error: Score out of range (0-100)'

try:
    score = int(input("Enter a score between 0 and 100: "))
    grade = calculate_grade(score)
    print(f"Grade: {grade}")
except :
    print("Error, Please enter a numeric input between 0 and 100")