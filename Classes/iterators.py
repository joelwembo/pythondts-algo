element1 = [12,23,1,3,30]
element2 = (32,34,22,1,3)

element3 = {32,34,22,1,3}


for i in element1:
   # print(i)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('Wembo')

print(iter(rev))


