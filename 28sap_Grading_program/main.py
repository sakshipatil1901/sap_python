student_marks = {
    "Purva" : 91,
    "Mahesh" : 78,
    "Vivek" : 56,
    "Kranti" : 41,
    "Abhishek" : 99,
    "Prem" : 34
}

student_grades={}

for student in student_marks:
    score = student_marks[student]
    if score > 90:
        student_grades[student]="A+"
    elif score > 80:
        student_grades[student]="A"
    elif score > 70:
        student_grades[student]="B+"
    elif score > 60:
        student_grades[student]="B"
    elif score > 50:
        student_grades[student]="C"
    elif score > 40:
        student_grades[student]="D"
    else:
        student_grades[student]="F"
print(student_grades)