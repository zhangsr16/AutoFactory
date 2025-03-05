from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

    def move(self):
        return "Run"

class Cat(Animal):
    def sound(self):
        return "Meow"

    def move(self):
        return "Jump"

# 试图实例化抽象基类会引发错误
try:
    animal = Animal()
except TypeError as e:
    print(e)  # "Can't instantiate abstract class Animal with abstract methods move, sound"

# 正确实例化子类
dog = Dog()
print(dog.sound())  # "Woof"
print(dog.move())   # "Run"

cat = Cat()
print(cat.sound())  # "Meow"
print(cat.move())   # "Jump"
