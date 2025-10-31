class Student:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Location: {self.location}"
    
class Classroom:
    def __init__(self, *students_info):
        self.students = []
        for info in students_info:
            self.add_student(*info)

    def add_student(self, name, age, location):
        student = Student(name, age, location)
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(student)


#첫번째 교실 생성
classroom1 = Classroom()
classroom1.add_student("이상욱", 47, "서울")
classroom1.add_student("성화정", 16, "길음")

#두번째 교실 생성
classroom2 = Classroom()
classroom2.add_student("박영희", 17, "인천")
classroom2.add_student("오은교", 15, "인천")
classroom2.add_student("이찬주", 23, "신촌")

#classroom1&2에 있는 학생들의 목록을 출력
classroom1.list_students()
classroom2.list_students()

