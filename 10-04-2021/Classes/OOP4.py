
class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = 10000
        self._num_bugs_solved = 0

swe = SoftwareEngineer("Max", 23)
print(swe.age, swe.name, swe._salary)
