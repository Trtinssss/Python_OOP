class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f'Courses: {", ".join(self.courses)}')


student1 = Student("Le Trung Tin", "22521478")
course = []
while True:
     course_input = input("Nhập tên 1 khóa học ")
     if course_input  == "q": # Nếu là q thì k nhập nữa
         break
     else:
         course.append(course_input)
   

student1.display_info()
print(course)