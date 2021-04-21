class Dog:

    kind = 'Canine' # Class variable shared by all instances
    tricks = []

    def __init__(self, name):
        self.name = name # instance variable unique to each instance

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
f = Dog('we')
print(e.name)

d.add_trick('roll over')
e.add_trick('play dear')
f.add_trick('move slow')
print(d.tricks)      # unexpected