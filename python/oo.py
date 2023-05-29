from dataclasses import dataclass
from unittest import TestCase

class Dog:
    Age = 0  # class objects
    Name = ''

# subclass `Dog`
class FierceDog(Dog):
    def bark(self):
        print("Wang! Wang! My name is {}".format(self.Name))

class CuteDog(Dog):
    loveliness = 0

    # initialization method. automatically execute when creating an instance like `i = CuteDog(0, 0)`.
    def __init__(self, size, color):
        self.size, self.color = size, color  # instance objects

    def info(self):
        print('My color is {}, and size is {}'.format(self.color, self.size))

class FierceCuteDog(FierceDog, CuteDog):
    # override info() of `CuteDog`.
    def info(self):
        print('My color is {}, and size is {}. However, I can bark'.format(self.color, self.size))

@dataclass  # supported by 3.7+
class DogData:
    rank: int
    name: str

# you can imitate a dataclass by implementing two following methods.
class RegularDogData:
    def __init__(self, rank, name):
        self.rank = rank
        self.name = name

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, name={self.name!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.name) == (other.rank, other.name)

class TestDataClass(TestCase):
    def test_dataclass(self):
        d1 = DogData(10, 'Dog A')
        d2 = DogData(10, 'Dog A')
        self.assertIs(d1 == d2, True)
