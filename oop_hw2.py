from abc import abstractmethod, ABC

"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
class Animals:
    Parent class, should have eat, sleep
class Animal1(Animal):
    Some of the animal with 1-2 extra methods related to this animal
"""


class Animals:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def eating(self):
        print(f'I am {self.name} and i eating {self.eat} ')

    def sleeping(self):
        print(f'I sleeping {self.sleep} hour')


class Dog(Animals):
    def bark(self):
        print(f'{self.__class__.__name__} {self.name} Bark')


class Bird(Animals):
    def fly(self):
        print(f'{self.__class__.__name__} {self.name} Flying')


class Horse(Animals):
    def fast_running(self):
        print(f'{self.__class__.__name__} {self.name}Fast running ')


class Snake(Animals):
    def crawling(self):
        print(f'{self.__class__.__name__} {self.name} Crawling')


class Cow(Animals):
    def give_milk(self):
        print(f'{self.__class__.__name__} {self.name} Give milk')


dog = Dog('Muhtar', 'meat', 5)
bird = Bird('Pary', 'worm', 4)
horse = Horse('Amy', 'grass', 6)
snake = Snake('Ash', 'anything', 2)
cow = Cow('Zirka', 'grass', 6)
anmls = (dog, bird, horse, snake, cow)

for i in anmls:
    i.eating()
    i.sleeping()

for i in anmls:
    print(isinstance(i, Animals))

print('~~#1a~~')
"""
1.a.Create a new class Human and use multiple inheritance to create Centaur class,
create an instance of Centaur class and call the common method of these classes and unique.
class Human:
      Human class, should have eat, sleep, study, work
class Centaur(..   , ..):
    Centaur class should be inherited from Human and Animal and has unique method related to it.
"""


class Human:
    def __init__(self, name):
        self._name_ = name

    def eat(self):
        print(f"{self._name_} eat some food")

    def sleep(self):
        print(f"{self._name_} 15 hours")

    def study(self):
        print(f"{self._name_}  studying")

    def work(self):
        print(f"{self._name_} hard work")


class Centaur(Human, Animals):
    def fight(self):
        print(f"{self.name} fighting")


def cent():
    centaur = Centaur("Barbous")
    centaur.fight()
    centaur.sleep()
    centaur.eat()
    centaur.work()
    centaur.study()


#2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
#a
class Person:
 def __init__(self):
        arm_1 = Arm('Left hand')
        arm_2 = Arm('Right hand')
        self.arms = [arm_1, arm_2]
     # Make the class with composition.
class Arm:
    def __init__(self, arm1):
        self.hand = arm1

arm1_ = Person()
for arm_1 in arm1_.arms:
    print(arm_1.hand)
#b

class CellPhone:
   # Make the class with aggregation
    def __init__(self, system):
        self.system = system

class System:
    def __init__(self, sys_type):
        self.sys_type = sys_type

phone = System('Android')
phone_name = CellPhone(phone)
print(phone.sys_type)
print(phone_name.system.sys_type)



"""
3  Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
"""

class Profile:


    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.info = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday]

    def __str__(self):
        return f'my info: {self.info}'

prof = Profile('Andriy', 'May', '093000000', 'Lviv city', 'anmay@gmail.com', '16.12.1998', 22, 'male')
print(prof)



"""
4
Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics 
and create an HPLaptop class by using your interface.
"""

class Laptop(ABC):
    @abstractmethod
    def Screen(self):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def WebCam(self):
        raise NotImplementedError

    @abstractmethod
    def Ports(self):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError

