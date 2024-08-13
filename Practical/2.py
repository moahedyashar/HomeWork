class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age 

    def greet(self):
        print(f'hello {self.name}')

person = person('moahed', 20)

person.greet()