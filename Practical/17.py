class school:
    def __init__(self, name):
        self.name = name
        self.student = []
    
    def add_student(self, student):
        self.student.append(student)

    def remove_student(self, student):
        if student in self.student:
            self.student.remove(student)
        else:
            print('student not found')

myschool = school("oroog")

myschool.add_student('moahed')
print(myschool.student)