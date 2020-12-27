"""
ibrahimbas2079@gmail.com
Ibrahim Baş
Homework Project 25.12.2020 Friday 10.00 PM
Create a Simple Management System:
One student who enter name and surname correctly
should write "Welcome" on the screen with print. The student
has the right to enter his / her name and surname incorrectly 3 times.
For more than 3 incorrect entries, the system shuts down and
the message "Please try again later" should be printed on the screen.
5 courses should be created and these courses should be kept in a list.
All of these lessons should be taken from the user.
The student can take a minimum of 3 and a maximum of 5 lessons.
This student can not take less than 3 courses.
Otherwise, the message "You failed in class" should be returned
to the student by using the return statement.
The student must choose one of these courses and take an exam.
Add the grades from this course to a dictionary and
keep the student's grades in this dictionary as Midterm, Final, and
Project grades.
Example: "Midterm": 38, "Final": 66, "Project":89
Percentages for grades
Midterm Exam %100
Final %50
Project %20
Determine a course passing grade according to the grades received.
For notes:
If the grade is bigger than 90, the student should gets AA.
If 70 < grade < 90 BB
If 50 < grade < 70 CC
If 30 < grade < 50 DD
If the grade less than 30, the student should gets FF.
If the student has received FF, he / she should print
his / her failure on the screen.
"""
s = str()
d = {}
name = {"AHMET"}
surname = {"BAS"}
for i in range(3):
    i += 1
    name1 = str(input("Name  : "))
    surname1 = str(input("Surname: "))
    name2 = (name1.upper())
    surname2 = (surname1.upper())
    if name2 not in name and surname2 not in surname:
        print(f"Last your {3 - i} chance")
        continue
    else:
        print(f"Welcome '{name2}''{surname2}'")
        d["Name"] = name2
        d["Surname"] = surname2

    Checklist = ["LESSON LIST"]
    while True:
        x = input("How many lesson do you want to take? :")
        try:
            x = int(x)
            break
        except:
            print("Please enter a number")
    while True:
        if 3 > x or x > 5:
            print("You failed in class")
            print("Please write a number that between 3 and 5!")
            x = int(input("How many lesson do you want to take? :"))
            continue
        else:
            for j in range(x):
                j += 1
                c = str(input(f"Enter {j}. lesson:"))
                keys = [f"{j}. Lesson {c}"]
                Checklist.append(keys)
        for k in Checklist:
            print(*k)
        while True:
            lesson = (input("Please write lesson number that you want to choose :"))
            try:
                lesson = int(lesson)
                break
            except:
                print("Please enter a number")
        while True:
            if 1 > lesson or lesson > x:
                print(f"Enter a Lesson number from 1 to {x}")
                lesson = int(input("Please write lesson number : "))
            else:
                print(f"{Checklist[lesson]}")

                while True:
                    Midterm = (input("Please enter the result of Midterm Exam : "))
                    try:
                        Midterm = int(Midterm)
                        break
                    except:
                        print("Please enter a number")
                while True:
                    Final = (input("Please enter the result of Final Exam   : "))
                    try:
                        Final = int(Final)
                        break
                    except:
                        print("Please enter a number")
                while True:
                    Project = (input("PLease enter the Result of Project      : "))
                    try:
                        Project = int(Project)
                        break
                    except:
                        print("Please enter a number")
                while True:
                    while True:
                        if not 0 <= Midterm <= 100:
                            print("Please enter a Midterm note is between 0 and 100")
                            Midterm = int(input("Please enter the result of Midterm Exam   : "))
                        break
                    while True:
                        if not 0 <= Final <= 100:
                            print("Please enter a Final note is between 0 and 100")
                            Final = int(input("Please enter the result of Final Exam : "))
                        break
                    while True:
                        if not 0 <= Project <= 100:
                            print("Please enter a Project note is between 0 and 100")
                            Project = int(input("PLease enter the Result of Project    : "))
                        break
                    break
                AvgNote = Midterm * 0.3 + Final * 0.5 + Project * 0.2
                if 90 <= AvgNote < 100:
                    s = "AA"
                elif 70 <= AvgNote < 90:
                    s = "BB"
                elif 50 <= AvgNote < 70:
                    s = "CC"
                elif 30 <= AvgNote < 50:
                    s = "DD"
                elif AvgNote < 30:
                    s = "FF, you failed!"
                d["Lesson"] = Checklist[lesson]
                d["Midterm"] = Midterm
                d["Final"] = Final
                d["Project"] = Project
                d["AvgNote"] = AvgNote
                d["Letter Grade"] = s
                print(d)

                break

        break

    break
else:
    print("Please try again later")
