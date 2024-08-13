class Student:
    def __init__(self, name = "", grade = 0, age = 0):
        self._name = name
        self._grade = grade
        self._age = age
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_grade(self):
        return self._grade
    def set_grade(self, grade):
        self._grade = grade

    def get_age(self):
        return self._age
    def set_age(self, age):
        self._age = age

student = Student("moahed", 100, 19)

print(student.get_name())