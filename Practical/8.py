class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

employee = Employee("ahmad", 50000)
manager = Manager("moahed", 100000, "HR")

print(manager.name)