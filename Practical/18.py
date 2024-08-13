class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
        else:
            print('member not found')

my_team = Team('oroog')

my_team.add_member('moahed')
my_team.add_member('yashar')

print(my_team.members)

