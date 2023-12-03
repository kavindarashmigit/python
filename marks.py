marks = []

for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter the mark {i + 1}: "))
            if 0 <= mark <= 100:  
                marks.append(mark)
                break
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Please enter a valid numerical mark.")

grades = []

for mark in marks:
    if mark > 75:
        grades.append("A")
    elif 65 <= mark <= 75:
        grades.append("B")
    elif 55 <= mark <= 64:
        grades.append("C")
    elif 45 <= mark <= 54:
        grades.append("S")
    else:
        grades.append("F")

for i in range(5):
    print(f"Mark {marks[i]} is graded as: {grades[i]}")
