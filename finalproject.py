class Course:
    course_id = 1

    def __init__(self, name, level):
        self.course_id = Course.course_id
        self.course_name = name
        self.course_level = level
        Course.course_id += 1

    def get_course_details(self):
        print('ID:', str(self.course_id) + "\tname:" + self.course_name + "\tlevel:" + self.course_level)


class Student:
    student_id_add = 1

    def __init__(self, name, level):
        self.student_id = Student.student_id_add
        self.student_name = name
        self.student_level = level
        self.student_courses = []
        Student.student_id_add += 1

    def add_course(self, course):
        if course.course_level == self.student_level:
            if course in self.student_courses:
                print(f'the course {course.course_name} is exists befor')
                return
            else:
                self.student_courses.append(course)
                print(f"Course {course.course_name} added to {self.student_name}'s courses")
        else:
            print(
                f"The {course.course_name} can't be added to {self.student_name}'s courses. Course level is not compatible with student level.")

    def display_details(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.student_name}")
        print(f"Level: {self.student_level}")
        if len(self.student_courses) == 0:
            print('Courses :')
            return
        print("Courses:")
        for i, course in enumerate(self.student_courses):
            print(course.course_name)


students_list = []
courses_list = []

while True:
    print('\n----------------------------\n')
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display all students")
    print("5. Create new Course")
    print("6. Add Course to student")
    print("0. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 0:
        exit()


    elif choice == 1:
        name = input("Enter student name:")
        while True:
            level = input("Select level (A-B-C):")
            if level not in ["A", "B", "C", 'a', 'b', 'c']:
                print("Invalid level , Please select again")
            else:
                break
        student = Student(name, level.upper())
        students_list.append(student)
        print("Student saved successfully")




    elif choice == 2:
        if len(students_list) == 0:
            print('There is no student in list')
        else:
            print('All student :')
            for student in students_list:
                student.display_details()

            student_id = int(input("Enter student id:"))
            for student in students_list:
                if student.student_id == student_id:
                    students_list.remove(student)
                    print("Delete done successfully")
                    break
            else:
                print("Student not exist")




    elif choice == 3:
        student_id = int(input("Enter student id :"))
        for student in students_list:
            if student.student_id == student_id:
                name = input("Enter new name :")
                while True:
                    level = input("Select new level (A-B-C):")
                    if level not in ["A", "B", "C", 'a', 'b', 'c']:
                        print("Invalid level , Please select again")
                    else:
                        student.student_name = name
                        student.student_level = level.upper()
                        print("Edit done successfully")
                        break
                break
        else:
            print("Student not exist")





    elif choice == 4:
        if len(students_list) == 0:
            print('There is no student in list')
        else:
            print('All student :')
            for student in students_list:
                student.display_details()





    elif choice == 5:
        name = input("Enter course name:")
        while True:
            level = input("Select course level (A-B-C):")
            if level not in ["A", "B", "C", 'a', 'b', 'c']:
                print("Invalid level , Please select again")
            else:
                break
        course = Course(name, level.upper())
        courses_list.append(course)
        print("Course created successfully")



    elif choice == 6:
        student_id = int(input("Enter student id :"))
        for student in students_list:
            if student.student_id == student_id:
                course_id = int(input("Enter course id :"))
                for course in courses_list:
                    if course.course_id == course_id:
                        student.add_course(course)
                        break
                else:
                    print("Course not exist")
                break
        else:
            print("Student not exist")


