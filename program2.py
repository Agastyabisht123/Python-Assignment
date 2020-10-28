'''
Define a class Person and its two child classes: Male and Female. All classes have a method "get_gender" which can print "Male" for Male class and "Female" for Female Class.
'''
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):
    def get_gender(self):
        print('Male')

class Female(Person):
    def get_gender(self):
        print('Female')
#generates error
#person = Person()
#person.get_gender()

person = Male()
person.get_gender()
