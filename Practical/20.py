class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print('animal not found')
my_zoo = Zoo('kabul zoo')
my_zoo.add_animal("lion")

print(my_zoo.animals)