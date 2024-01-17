Name = input()
roll_no = int(input())
No_of_courses = eval(input())

student_data = [
    {
        "Name":"Sakshi",
        "roll_no":10,
        "age":20,
        "courses":["python", "SQL", "Java"]
    },
    {
        "Name":"Purva",
        "roll_no":30,
        "age":24,
        "courses":["HTML", "CSS", "C++"]
    }
]

def add_new_student(name,rollno,age,course_opted):
    new_student={}
    new_student["Name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["courses"]=course_opted
    student_data.append(new_student)

# add_new_student("Divya",40,15,"Javascript")
# print(student_data)
add_new_student(Name, roll_no, No_of_courses, course_opted=["python", "SQL", "Java"])
print(f"My Name is {student_data[2]['Name']}. My Roll no is {student_data[2]['roll_no']}.")
print(f"My New courses are {student_data[2]['courses'][0]}")