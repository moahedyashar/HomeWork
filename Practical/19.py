class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)

    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
        else:
            print('employee not found')
my_company = Company('Apple')

my_company.add_employee('moahed yashar')
print(my_company.employees)
        
