print("PERSONAL POCKET CGPA CALCULATOR")

name = input("Student Name: ")

tcu = 0
tgp = 0

# First Semester
first = int(input("\nNumber of First Semester Courses: "))

print("\nFIRST SEMESTER")
for i in range(first):
    unit = int(input("Course Unit: "))
    grade = input("Grade (A-F): ").upper()

    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    else:
        point = 0

    tcu += unit
    tgp += unit * point

# Second Semester
second = int(input("\nNumber of Second Semester Courses: "))

print("\nSECOND SEMESTER")
for i in range(second):
    unit = int(input("Course Unit: "))
    grade = input("Grade (A-F): ").upper()

    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    else:
        point = 0

    tcu += unit
    tgp += unit * point

cgpa = tgp / tcu

print("\nStudent:", name)
print("CGPA =", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class: First Class")
elif cgpa >= 3.50:
    print("Class: Second Class Upper")
elif cgpa >= 2.40:
    print("Class: Second Class Lower")
elif cgpa >= 1.50:
    print("Class: Third Class")
elif cgpa >= 1.00:
    print("Class: Pass")
else:
    print("Class: Fail")