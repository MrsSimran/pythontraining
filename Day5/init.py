class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show_details(self):
        print("Student Name:", self.name)
        print("Course Enrolled:", self.course)

# Creating object
s1 = Student("Simran", "QA Automation")
s1.show_details()
